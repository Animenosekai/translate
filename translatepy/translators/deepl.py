"""
DeepL Implementation for translatepy

Copyright
---------
Marocco2
    Original implementation
    Refer to Animenosekai/translate#7
Animenosekai
    Arrangements, optimizations
ZhymabekRoman
    Co-Author
"""

import re
import time
import uuid
import enum
import random
import secrets
import typing

from bs4 import BeautifulSoup

from translatepy import models, exceptions
from translatepy.language import Language
from translatepy.translators.base import BaseTranslateException, BaseTranslator, C
from translatepy.translators.base_aggregator import BaseTranslatorAggregator
from translatepy.utils import request

SENTENCES_SPLITTING_REGEX = re.compile('(?<=[.!:?]) +')


class DeeplFormality(enum.Enum):
    formal = "formal"
    informal = "informal"


class DeeplTranslate(BaseTranslatorAggregator):
    def __init__(self, session: request.Session = None, *args, **kwargs) -> None:
        super().__init__([DeeplTranslateV1, DeeplTranslateV2], session, *args, **kwargs)


class DeeplTranslateException(BaseTranslateException):
    """
    Default DeepL Translate exception
    """

    error_codes = {
        1042911: "Too many requests."
    }


class GetClientState:
    """
    DeepL Translate state manager
    """

    def __init__(self, session: request.Session):
        self.id_number = random.randint(1000, 9999) * 10000
        self.session = session

    def dump(self) -> dict:
        self.id_number += 1
        data = {
            'jsonrpc': '2.0',
            'method': 'getClientState',
            'params': {
                'v': '20180814',
                'clientVars': {},
            },
            'id': self.id_number,
        }
        return data

    def get(self) -> int:
        """
        Returns a new Client State ID
        """
        request = self.session.post("https://w.deepl.com/web", params={'request_type': 'jsonrpc', 'il': 'E', 'method': 'getClientState'}, json=self.dump())
        response = request.json()
        return response["id"]


class JSONRPCRequest:
    """
    JSON RPC Request Sender for DeepL
    """

    def __init__(self, session: request.Session) -> None:
        self.client_state = GetClientState(request)
        try:
            self.id_number = self.client_state.get()
        except Exception:
            self.id_number = (random.randint(1000, 9999) * 10000) + 1  # ? I didn't verify the range, but it's better having only DeepL not working than having Translator() crash for only one service
        self.session = session
        self.last_access = 0

    def dump(self, method: str, params: dict):
        self.id_number += 1
        data = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params,
            "id": self.id_number
        }
        return data

    def send_jsonrpc(self, method: str, params: dict) -> dict:
        # Take a break 3 sec between requests, so as not to get a block by the IP address
        if time.time() - self.last_access < 3:
            distance = 3 - (time.time() - self.last_access)
            time.sleep((distance if distance >= 0 else 0))

        request = self.session.post("https://www2.deepl.com/jsonrpc", json={"method": method, "params": params}, params={"client": "chrome-extension,1.6.1"})
        self.last_access = time.time()
        response = request.json()
        if request.status_code == 200:
            return response["result"]
        else:
            raise DeeplTranslateException(response["error"]["code"], response["error"]["message"])


class DeeplTranslateV1(BaseTranslator):
    _supported_languages: dict = {'AUTO', 'BG', 'CS', 'DA', 'DE', 'EL', 'EN', 'ES', 'ET', 'FI', 'FR', 'HU', 'IT', 'JA', 'LT', 'LV', 'NL', 'PL', 'PT', 'RO', 'RU', 'SK', 'SL', 'SV', 'ZH', 'TR', 'ID', 'UK'}

    def __init__(self, session: request.Session = None, preferred_langs: typing.List = ["EN", "RU"]) -> None:
        super().__init__(session)
        self.session.headers["User-Agent"] = "DeepLBrowserExtension/1.6.1 Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
        self.session.get("https://static.deepl.com/img/illustrations/pro-features-3x1.svg")  # we need to get some security cookies from Cloudflare
        self.jsonrpc = JSONRPCRequest(self.session)
        self.user_preferred_langs = preferred_langs

    def _split_into_sentences(self: C, text: str, dest_lang: typing.Any, source_lang: typing.Any) -> typing.Tuple[typing.List[str], str]:
        """
        Split a string into sentences using the DeepL API.\n
        Fallbacks to a simple Regex splitting if an error occurs or no result is found

        Returned typing.Tuple: (Result, Computed Language (None if same as source_lang))
        """
        REGEX_SPLIT = True

        if REGEX_SPLIT is True:
            SENTENCES_SPLITTING_REGEX.split(text), None

        params = {
            "texts": [text.strip()],  # What for need strip there?
            "lang": {
                "lang_user_selected": source_lang,
                "user_preferred_langs": list(set(self.user_preferred_langs + [dest_lang]))
            }
        }
        resp = self.jsonrpc.send_jsonrpc("LMT_split_into_sentences", params)

        return resp["splitted_texts"][0], resp["lang"]

    def _translate(self: C, text: str, dest_lang: typing.Any, source_lang: typing.Any) -> models.TranslationResult[C]:
        priority = 1
        quality = ""

        # splitting the text into sentences
        sentences, computed_lang = self._split_into_sentences(text, dest_lang, source_lang)

        # building the a job per sentence
        jobs = self._build_jobs(sentences, quality)

        # time.timestamp generation
        i_count = 1
        for sentence in sentences:
            i_count += sentence.count("i")
        ts = int(time.time() * 10) * 100 + 1000

        # params building
        params = {
            "jobs": jobs,
            "lang": {
                "target_lang": dest_lang,
                "user_preferred_langs": [dest_lang]
            },
            "priority": priority,
            "time.timestamp": ts + (i_count - ts % i_count)
        }

        if source_lang == "auto":
            params["lang"]["source_lang_computed"] = computed_lang
            params["lang"]["user_preferred_langs"].append(computed_lang)
        else:
            params["lang"]["source_lang_user_selected"] = source_lang

        results = self.jsonrpc.send_jsonrpc("LMT_handle_jobs", params)

        try:
            _detected_language = results["source_lang"]
        except Exception:
            _detected_language = source_lang

        if results is not None:
            translations = results["translations"]
            return models.TranslationResult(source_lang=_detected_language, translation=" ".join(obj["beams"][0]["postprocessed_sentence"] for obj in translations if obj["beams"]))

    def _language(self: C, text: str) -> models.LanguageResult[C]:
        priority = 1
        quality = ""

        # splitting the text into sentences
        sentences, computed_lang = self._split_into_sentences(text, "EN", "AUTO")

        # building the a job per sentence
        jobs = self._build_jobs(sentences, quality)

        # time.timestamp generation
        i_count = 1
        for sentence in sentences:
            i_count += sentence.count("i")
        ts = int(time.time() * 10) * 100 + 1000

        # params building
        params = {
            "jobs": jobs,
            "lang": {
                "target_lang": "EN",
                "user_preferred_langs": ["EN"]
            },
            "priority": priority,
            "time.timestamp": ts + (i_count - ts % i_count)
        }

        if computed_lang is not None:
            params["lang"]["source_lang_computed"] = computed_lang
            params["lang"]["user_preferred_langs"].append(computed_lang)
        else:
            params["lang"]["source_lang_user_selected"] = "AUTO"

        results = self.jsonrpc.send_jsonrpc("LMT_handle_jobs", params)

        if results is not None:
            return models.LanguageResult(language=results["source_lang"])

    def _dictionary(self: C, text: str, source_lang: typing.Any) -> typing.Union[typing.Union[models.DictionaryResult[C], models.RichDictionaryResult[C]], typing.List[typing.Union[models.DictionaryResult[C], models.RichDictionaryResult[C]]]]:
        # TODO: Need to reimplement
        raise exceptions.UnsupportedMethod("Need to reimplement this")
        if source_lang == "AUTO":
            source_lang = self._language_to_code(self.language(text).language)

        dest_lang = ""
        dest_lang = Language(dest_lang).name.lower()
        source_lang = Language(source_lang).name.lower()

        request = self.session.post("https://dict.deepl.com/" + source_lang + "-" + dest_lang + "/search?ajax=1&source=" + source_lang + "&onlyDictEntries=1&translator=dnsof7h3k2lgh3gda&delay=800&jsStatus=0&kind=full&eventkind=keyup&forleftside=true", data={"query": text})
        if request.status_code < 400:
            response = BeautifulSoup(request.text, "html.parser")
            _result = []
            for element in response.find_all("a"):
                if element.has_attr('class'):
                    if "dictLink" in element["class"]:
                        _result.append(element.text.replace("\n", ""))
                        # if "featured" in element["class"]:
                        #     results["featured"].append(element.text.replace("\n", ""))
                        # else:
                        #     results["less_common"].append(element.text.replace("\n", ""))
            return source_lang, _result

    def _build_jobs(self, sentences: typing.List, quality: typing.Optional[str] = None):
        """
        Builds a job for each sentence for DeepL
        """
        jobs = []
        for index, sentence in enumerate(sentences):
            if index == 0:
                try:
                    before = []
                    after = [sentences[index + 1]]
                except IndexError:  # index == len(sentences) - 1
                    before = []
                    after = []
            else:
                if len(before) > 4:
                    before.pop(0)  # the "before" array cannot be more than 5 elements long i guess?
                before.extend([sentences[index - 1]])
                if index > len(sentences) - 2:
                    after = []
                else:
                    after = [sentences[index + 1]]

            job = {
                "kind": "default",
                "raw_en_context_after": after.copy(),
                "raw_en_context_before": before.copy(),
                "raw_en_sentence": sentence,
            }
            if quality is not None:
                job["quality"] = quality
            jobs.append(job)

        return jobs

    def _language_to_code(self, language: Language) -> typing.Union[str, typing.Any]:
        if language.id == "zho":
            return "ZH"
        return language.alpha2.upper()

    def _code_to_language(self, code: typing.Union[str, typing.Any]) -> Language:
        if str(code).lower() in {"zh", "zh-cn"}:
            return Language("zho")
        return Language(code)

    def __str__(self) -> str:
        return "DeepL Web"


class DeeplTranslateV2(BaseTranslator):
    _client_id: str = "f02c852d-109d-448c-a9fb-5a805000f8cb"
    _device_name: str = secrets.token_hex(16)
    _user_agent = f"DeepL/2.4(69) Android 11 ({_device_name};aarch64)"

    def __init__(self, session: request.Session = None) -> None:
        super().__init__(session)
        self.session.headers["User-Agent"] = self._user_agent
        self.id_number = (random.randint(1000, 9999) * 10000) + 1  # ? I didn't verify the range, but it's better having only DeepL not working than having Translator() crash for only one service

    def _translate(self, text: str, dest_lang: typing.Any, source_lang: typing.Any, formality: typing.Optional[DeeplFormality] = None) -> models.TranslationResult:
        timestamp = int(time.time() * 10) * 100 + 1000

        trace_id = str(uuid.uuid4()).replace("-", "")

        random_bytes = secrets.token_bytes(8)
        random_hex = secrets.token_hex(len(random_bytes))

        headers = {
            "referer": "https://www.deepl.com/",
            "traceparent": f"00-{trace_id}-{random_hex}-01",
            "x-trace-id": trace_id,
            "x-instance": self._client_id,
            "client-id": self._client_id,
            "x-app-os-name": "Android",
            "x-app-os-version": "11",
            "x-app-version": "2.4",
            "x-app-build": "69",
            "x-app-device": self._device_name,
            "x-app-instance-id": self._client_id,
            "accept-encoding": "gzip"
        }

        data = {
            "params": {
                "texts": [{"text": text, "requestAlternatives": 3}],
                "splitting": "newlines",
                "commonJobParams": {"wasSpoken": False, "formality": formality},
                "lang": {"target_lang": dest_lang, "source_lang_user_selected": source_lang},
                "timestamp": timestamp
            },
            "id": self.id_number,
            "jsonrpc": "2.0",
            "method": "LMT_handle_texts"
        }

        request = self.session.post("https://www2.deepl.com/jsonrpc", headers=headers, json=data)

        if request.status_code != 200:
            raise DeeplTranslateException(request.status_code, request.text)

        response = request.json()

        self.id_number += 1

        source_lang = response["result"]["lang"]
        dest_lang = list(response["result"]["detectedLanguages"])[0]

        return models.TranslationResult(source_lang=source_lang, dest_lang=dest_lang, translation=response["result"]["texts"][0]["text"])

    def _language_to_code(self, language: Language) -> typing.Union[str, typing.Any]:
        if language.id == "zho":
            return "ZH"
        elif language.id == "auto":
            return ""
        return language.alpha2.upper()

    def _code_to_language(self, code: typing.Union[str, typing.Any]) -> Language:
        if str(code).lower() in {"zh", "zh-cn"}:
            return Language("zho")
        elif str(code) == "":
            return Language("auto")
        return Language(code)

    def __str__(self: C) -> str:
        return "DeepL Android"
