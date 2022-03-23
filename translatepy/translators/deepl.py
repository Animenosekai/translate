"""
DeepL

About the translation and the language endpoints:
    This implementation of DeepL follows Marocco2's implementation of DeepL's JSONRPC API\n
    Arrangements and optimizations have been made\n
    Refer to Issue Animenosekai/translate#7 on GitHub for further details

© Anime no Sekai — 2021
"""

from time import time, sleep
from re import compile
from random import randint
from bs4 import BeautifulSoup

from translatepy.language import Language
from translatepy.translators.base import BaseTranslator, BaseTranslateException
from translatepy.utils.annotations import Tuple, List
from translatepy.utils.request import Request

SENTENCES_SPLITTING_REGEX = compile('(?<=[.!:?]) +')


class DeeplTranslateException(BaseTranslateException):
    """
    Default DeepL Translate exception
    """

    error_codes = {
        1042911: "Too many requests."
    }


class GetClientState():
    """
    DeepL Translate state manager
    """
    def __init__(self, request: Request):
        self.id_number = randint(1000, 9999) * 10000
        self.session = request

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


class JSONRPCRequest():
    """
    JSON RPC Request Sender for DeepL
    """
    def __init__(self, request: Request) -> None:
        self.client_state = GetClientState(request)
        try:
            self.id_number = self.client_state.get()
        except Exception:
            self.id_number = (randint(1000, 9999) * 10000) + 1  # ? I didn't verify the range, but it's better having only DeepL not working than having Translator() crash for only one service
        self.session = request
        self.last_access = 0

    def dump(self, method, params):
        self.id_number += 1
        data = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params,
            "id": self.id_number
        }
        return data

    def send_jsonrpc(self, method, params):
        # Take a break 3 sec between requests, so as not to get a block by the IP address
        if time() - self.last_access < 3:
            distance = 3 - (time() - self.last_access)
            sleep((distance if distance >= 0 else 0))

        request = self.session.post("https://www2.deepl.com/jsonrpc", json=self.dump(method, params))
        self.last_access = time()
        response = request.json()
        if request.status_code == 200:
            return response["result"]
        else:
            raise DeeplTranslateException(response["error"]["code"])


class DeeplTranslate(BaseTranslator):

    _supported_languages = {'AUTO', 'BG', 'ZH', 'CS', 'DA', 'NL', 'NL', 'EN', 'ET', 'FI', 'FR', 'DE', 'EL', 'HU', 'IT', 'JA', 'LV', 'LT', 'PL', 'PT', 'RO', 'RO', 'RO', 'RU', 'SK', 'SL', 'ES', 'ES', 'SV'}

    def __init__(self, request: Request = Request(), preferred_langs: List = ["EN", "RU"]) -> None:
        self.session = request
        self.jsonrpc = JSONRPCRequest(request)
        self.user_preferred_langs = preferred_langs

    def _split_into_sentences(self, text: str, destination_language: str, source_language: str) -> Tuple[List[str], str]:
        """
        Split a string into sentences using the DeepL API.\n
        Fallbacks to a simple Regex splitting if an error occurs or no result is found

        Returned tuple: (Result, Computed Language (None if same as source_language))
        """
        REGEX_SPLIT = True

        if REGEX_SPLIT is True:
            SENTENCES_SPLITTING_REGEX.split(text), None

        params = {
            "texts": [text.strip()],  # What for need strip there?
            "lang": {
                "lang_user_selected": source_language,
                "user_preferred_langs": list(set(self.user_preferred_langs + [destination_language]))
            }
        }
        resp = self.jsonrpc.send_jsonrpc("LMT_split_into_sentences", params)

        return resp["splitted_texts"][0], resp["lang"]

    def _translate(self, text: str, destination_language: str, source_language: str) -> str:
        priority = 1
        quality = ""

        # splitting the text into sentences
        sentences, computed_lang = self._split_into_sentences(text, destination_language, source_language)

        # building the a job per sentence
        jobs = self._build_jobs(sentences, quality)

        # timestamp generation
        i_count = 1
        for sentence in sentences:
            i_count += sentence.count("i")
        ts = int(time() * 10) * 100 + 1000

        # params building
        params = {
            "jobs": jobs,
            "lang": {
                "target_lang": destination_language,
                "user_preferred_langs": [destination_language]
            },
            "priority": priority,
            "timestamp": ts + (i_count - ts % i_count)
        }

        if source_language == "auto":
            params["lang"]["source_lang_computed"] = computed_lang
            params["lang"]["user_preferred_langs"].append(computed_lang)
        else:
            params["lang"]["source_lang_user_selected"] = source_language

        results = self.jsonrpc.send_jsonrpc("LMT_handle_jobs", params)

        try:
            _detected_language = results["source_lang"]
        except:
            _detected_language = source_language

        if results is not None:
            translations = results["translations"]
            return _detected_language, " ".join(obj["beams"][0]["postprocessed_sentence"] for obj in translations if obj["beams"])

    def _language(self, text: str) -> str:
        priority = 1
        quality = ""

        # splitting the text into sentences
        sentences, computed_lang = self._split_into_sentences(text, "EN", "AUTO")

        # building the a job per sentence
        jobs = self._build_jobs(sentences, quality)

        # timestamp generation
        i_count = 1
        for sentence in sentences:
            i_count += sentence.count("i")
        ts = int(time() * 10) * 100 + 1000

        # params building
        params = {
            "jobs": jobs,
            "lang": {
                "target_lang": "EN",
                "user_preferred_langs": ["EN"]
            },
            "priority": priority,
            "timestamp": ts + (i_count - ts % i_count)
        }

        if computed_lang is not None:
            params["lang"]["source_lang_computed"] = computed_lang
            params["lang"]["user_preferred_langs"].append(computed_lang)
        else:
            params["lang"]["source_lang_user_selected"] = "AUTO"

        results = self.jsonrpc.send_jsonrpc("LMT_handle_jobs", params)

        if results is not None:
            return results["source_lang"]

    def _dictionary(self, text: str, destination_language: str, source_language: str) -> str:
        if source_language == "AUTO":
            source_language = self._language(text)

        destination_language = Language(destination_language).name.lower()
        source_language = Language(source_language).name.lower()

        request = self.session.post("https://dict.deepl.com/" + source_language + "-" + destination_language + "/search?ajax=1&source=" + source_language + "&onlyDictEntries=1&translator=dnsof7h3k2lgh3gda&delay=800&jsStatus=0&kind=full&eventkind=keyup&forleftside=true", data={"query": text})
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
            return source_language, _result

    def _build_jobs(self, sentences, quality=""):
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
            if quality != "":
                job["quality"] = quality
            jobs.append(job)

        return jobs

    def _language_normalize(self, language):
        if language.id == "zho":
            return "ZH"
        return language.alpha2.upper()

    def _language_denormalize(self, language_code):
        if str(language_code).lower() in {"zh", "zh-cn"}:
            return Language("zho")
        return Language(language_code)

    def __str__(self) -> str:
        return "DeepL"
