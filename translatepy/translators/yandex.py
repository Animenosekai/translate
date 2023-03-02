"""
Yandex Translate

This implementation was made specifically for translatepy from 'Zhymabek Roman', based on 'Anime no Sekai' version.
"""

import uuid
import typing
from translatepy import models, exceptions
from translatepy.language import Language
from translatepy.translators.base import (BaseTranslateException,
                                          BaseTranslator, C)
from translatepy.utils import request


class YandexTranslateException(BaseTranslateException):
    """
    Default Yandex Translate exception
    """

    error_codes = {
        401: "ERR_KEY_INVALID",
        402: "ERR_KEY_BLOCKED",
        403: "ERR_DAILY_REQ_LIMIT_EXCEEDED",
        404: "ERR_DAILY_CHAR_LIMIT_EXCEEDED",
        408: "ERR_MONTHLY_CHAR_LIMIT_EXCEEDED",
        413: "ERR_TEXT_TOO_LONG",
        422: "ERR_UNPROCESSABLE_TEXT",
        501: "ERR_LANG_NOT_SUPPORTED",
        503: "ERR_SERVICE_NOT_AVAIBLE",
    }


class YandexTranslate(BaseTranslator):
    """
    Yandex Translation Implementation
    """

    _api_url = "http://translate.yandex.net/api/v1/tr.json/{endpoint}"
    _supported_languages = {'af', 'am', 'ar', 'auto', 'az', 'ba', 'be', 'bg', 'bn', 'bs', 'ca', 'ceb', 'cs', 'cv', 'cy', 'da',
                            'de', 'el', 'emj', 'en', 'eo', 'es', 'et', 'eu', 'fa', 'fi', 'fr', 'ga', 'gd', 'gl', 'gu', 'he', 'hi',
                            'hr', 'ht', 'hu', 'hy', 'id', 'is', 'it', 'ja', 'jv', 'ka', 'kazlat', 'kk', 'km', 'kn', 'ko', 'ky',
                            'la', 'lb', 'lo', 'lt', 'lv', 'mg', 'mhr', 'mi', 'mk', 'ml', 'mn', 'mr', 'mrj', 'ms', 'mt', 'my', 'ne',
                            'nl', 'no', 'pa', 'pap', 'pl', 'pt', 'ro', 'ru', 'sah', 'si', 'sjn', 'sk', 'sl', 'sq', 'sr', 'su', 'sv',
                            'sw', 'ta', 'te', 'tg', 'th', 'tl', 'tr', 'tt', 'udm', 'uk', 'ur', 'uz', 'uzbcyr', 'vi', 'xh', 'yi', 'zh', 'zu'}

    def __init__(self, session: typing.Optional[request.Session] = None):
        super().__init__(session)
        self.session.headers["User-Agent"] = "ru.yandex.translate/22.11.8.22364114 (samsung SM-A505GM; Android 12)"  # TODO: generate random telephone model

        uuid_v4 = str(uuid.uuid4())
        self.session_ucid = uuid_v4.replace("-", "")
        self.session_request_id = 0

    def _ucid(self, session_state: bool = False) -> str:
        """
        Generates UUID (UCID / (U)SID) for Yandex Translate API requests

        Returns
        -------
        str
            Yandex UUID value
        """

        if session_state:
            request_id = self.session_request_id
            self.session_request_id += 1
            return "{ucid}-{request_id}-0".format(ucid=self.session_ucid, request_id=request_id)

        return self.session_ucid

    def _translate(self: C, text: str, dest_lang: typing.Any, source_lang: typing.Any) -> models.TranslationResult[C]:
        if source_lang == "auto":
            source_lang = self._language_to_code(self.language(text).language)

        url = self._api_url.format(endpoint="translate")
        params = {"sid": self._ucid(session_state=True), "srv": "android", "format": "text"}
        data = {"text": text, "lang": source_lang + "-" + dest_lang}
        request = self.session.post(url, params=params, data=data)
        response = request.json()

        if request.status_code != 200 and response["code"] != 200:
            raise YandexTranslateException(response["code"])

        try:
            _detected_language = str(response["lang"]).split("-")[0]
        except Exception:
            _detected_language = source_lang

        return models.TranslationResult(source_lang=_detected_language, translation=response["text"][0], raw=response)

    def _transliterate(self: C, text: str, dest_lang: typing.Any, source_lang: typing.Any) -> models.TransliterationResult[C]:
        if source_lang == "auto":
            source_lang = self._language_to_code(self.language(text).language)

        url = "https://translate.yandex.net/translit/translit"
        data = {'text': text, 'lang': source_lang + "-" + dest_lang}
        request = self.session.post(url, data=data)

        if request.status_code != 200:
            raise YandexTranslateException(request.status_code)

        # `raw` is not really needed is it ?
        return models.TransliterationResult(source_lang=source_lang, transliteration=request.text[1:-1])

    def _spellcheck(self: C, text: str, source_lang: typing.Any) -> typing.Union[models.SpellcheckResult[C], models.RichSpellcheckResult[C]]:
        if source_lang == "auto":
            source_lang = self._language_to_code(self.language(text).language)

        url = "https://speller.yandex.net/services/spellservice.json/checkText"
        params = {"sid": self._ucid(), "srv": "android"}
        data = {"text": text, "lang": source_lang, "options": 8 + 4}
        request = self.session.post(url, params=params, data=data)

        if request.status_code != 200:
            raise YandexTranslateException(request.status_code)
        response = request.json()

        for correction in response:
            if correction["s"]:
                # TODO: I don't remember the exact response, but I feel like this might be suitable for `RichSpellcheckResult`
                word = correction['word']
                suggestion = correction['s'][0]
                text = text.replace(word, suggestion)
        return models.SpellcheckResult(source_lang=source_lang, corrected=text)

    def _language(self: C, text: str) -> models.LanguageResult[C]:
        url = self._api_url.format(endpoint="detect")
        params = {"sid": self._ucid(), "srv": "android"}
        data = {'text': text, 'hint': "en"}
        request = self.session.get(url, params=params, data=data)
        response = request.json()

        if request.status_code != 200 and response["code"] != 200:
            raise YandexTranslateException(response["code"])

        return models.LanguageResult(language=response["lang"])

    def _example(self: C, text: str, source_lang: typing.Any) -> typing.Union[models.ExampleResult[C], typing.List[models.ExampleResult[C]]]:
        if source_lang == "auto":
            source_lang = self._language_to_code(self.language(text).language)

        dest_lang = source_lang  # ?

        url = "https://dictionary.yandex.net/dicservice.json/queryCorpus"
        params = {"sid": self._ucid(), "srv": "android", "src": text, "ui": "en", "lang": source_lang + "-" + dest_lang, "flags": 7}
        request = self.session.get(url, params=params)

        if request.status_code != 200:
            raise YandexTranslateException(request.status_code)

        response = request.json()

        results = []

        for examples_group in response["result"]:
            for sentence in examples_group["examples"]:
                _sentence_result = sentence["dst"]
                _sentence_result = _sentence_result.replace("<", "").replace(">", "")
                results.append(_sentence_result)

        return [models.ExampleResult(source_lang=source_lang, example=sentence) for sentence in results]

    def _dictionary(self: C, text: str, source_lang: typing.Any) -> typing.Union[typing.Union[models.DictionaryResult[C], models.RichDictionaryResult[C]], typing.List[typing.Union[models.DictionaryResult[C], models.RichDictionaryResult[C]]]]:
        # TODO: Need to reimplement
        raise exceptions.UnsupportedMethod("Need to reimplement")

        if source_lang == "auto":
            source_lang = self._language_to_code(self.language(text).language)

        dest_lang = source_lang  # ?

        url = "https://dictionary.yandex.net/dicservice.json/lookupMultiple"
        params = {"sid": self._ucid(), "srv": "android", "text": text, "ui": "en", "dict": source_lang + "-" + dest_lang, "flags": 7, "dict_type": "regular"}
        request = self.session.get(url, params=params)

        if request.status_code != 200:
            raise YandexTranslateException(request.status_code)
        response = request.json()

        results = []

        for word in response["{}-{}".format(source_lang, dest_lang)]["regular"]:
            _word_result = word["tr"][0]["text"]
            results.append(_word_result)

        return source_lang, results

    def _language_to_code(self, language: Language) -> typing.Union[str, typing.Any]:
        if language.id == "zho":
            return "zh"
        elif language.id == "srd":
            return "sjn"
        return language.alpha2

    def _code_to_language(self, code: typing.Union[str, typing.Any]) -> Language:
        language_code = str(code).lower()
        if language_code in {"zh", "zh-cn"}:
            return Language("zho")
        elif language_code == "sjn":
            return Language("srd")
        return Language(language_code)

    def __str__(self) -> str:
        return "Yandex"
