"""
Yandex Translate

This implementation was made specifically for translatepy from 'Zhymabek Roman', based on 'Anime no Sekai' version.
"""

import uuid

from translatepy.exceptions import UnsupportedMethod
from translatepy.language import Language
from translatepy.translators.base import BaseTranslateException, BaseTranslator
from translatepy.utils.request import Request


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
    _supported_languages = {'auto', 'af', 'sq', 'am', 'ar', 'hy', 'az', 'ba', 'eu', 'be', 'bn', 'bs', 'bg', 'my', 'ca', 'ca', 'ceb', 'zh', 'cv', 'cs', 'da', 'nl', 'nl', 'en', 'eo', 'et', 'fi', 'fr', 'ka', 'de', 'gd', 'gd', 'ga', 'gl', 'el', 'gu', 'ht', 'ht', 'he', 'hi', 'hr', 'hu', 'is', 'id', 'it', 'jv', 'ja', 'kn', 'kk', 'km', 'ky', 'ky', 'ko', 'lo', 'la', 'lv', 'lt', 'lb', 'lb', 'mk', 'ml', 'mi', 'mr', 'ms', 'mg', 'mt', 'mn', 'mrj', 'mhr', 'ne', 'no', 'pa', 'pa', 'pap', 'fa', 'pl', 'pt', 'ro', 'ro', 'ro', 'ru', 'sah', 'si', 'si', 'sk', 'sl', 'es', 'es', 'sr', 'sjn', 'su', 'sw', 'sv', 'ta', 'tt', 'te', 'tg', 'tl', 'th', 'tr', 'udm', 'uk', 'ur', 'uz', 'vi', 'cy', 'xh', 'yi', 'zu', 'kazlat', 'uzbcyr', 'emj'}

    def __init__(self, request: Request = Request()):
        self.session = request
        self.session.header = {"User-Agent": "ru.yandex.translate/22.11.8.22364114 (samsung SM-A505GM; Android 12)"}  # TODO: generate random telephone model

        uuid_v4 = str(uuid.uuid4())
        self.session_ucid = uuid_v4.replace("-", "")
        self.session_request_id = 0

    def _ucid(self, session_state: bool = False) -> str:
        """
        Generates UUID (UCID / (U)SID) for Yandex Translate API requests

        Args:

        Returns:
            str --> Yandex UUID value
        """

        if session_state:
            request_id = self.session_request_id
            self.session_request_id += 1
            return "{ucid}-{request_id}-0".format(ucid=self.session_ucid, request_id=request_id)

        return self.session_ucid

    def _translate(self, text: str, destination_language: str, source_language: str) -> str:
        if source_language == "auto":
            source_language = self._language(text)

        url = self._api_url.format(endpoint="translate")
        params = {"sid": self._ucid(session_state=True), "srv": "android", "format": "text"}
        data = {"text": text, "lang": source_language + "-" + destination_language}
        request = self.session.post(url, params=params, data=data)
        response = request.json()

        if request.status_code != 200 and response["code"] != 200:
            raise YandexTranslateException(response["code"])

        try:
            _detected_language = str(data["lang"]).split("-")[0]
        except Exception:
            _detected_language = source_language

        return _detected_language, response["text"][0]

    def _transliterate(self, text: str, destination_language: str, source_language: str) -> str:
        if source_language == "auto":
            source_language = self._language(text)

        url = "https://translate.yandex.net/translit/translit"
        data = {'text': text, 'lang': source_language + "-" + destination_language}
        request = self.session.post(url, data=data)

        if request.status_code != 200:
            raise YandexTranslateException(request.status_code)

        return source_language, request.text[1:-1]

    def _spellcheck(self, text: str, source_language: str) -> str:
        if source_language == "auto":
            source_language = self._language(text)

        url = "https://speller.yandex.net/services/spellservice.json/checkText"
        params = {"sid": self._ucid(), "srv": "android"}
        data = {"text": text, "lang": source_language, "options": 8 + 4}
        request = self.session.post(url, params=params, data=data)
        response = request.json()

        if request.status_code != 200:
            raise YandexTranslateException(request.status_code)

        for correction in response:
            if correction["s"]:
                word = correction['word']
                suggestion = correction['s'][0]
                text = text.replace(word, suggestion)
            return source_language, text

    def _language(self, text: str):
        url = self._api_url.format(endpoint="detect")
        params = {"sid": self._ucid(), "srv": "android"}
        data = {'text': text, 'hint': "en"}
        request = self.session.get(url, params=params, data=data)
        response = request.json()

        if request.status_code != 200 and response["code"] != 200:
            raise YandexTranslateException(response["code"])

        return response["lang"]

    def _example(self, text: str, destination_language: str, source_language: str):
        if source_language == "auto":
            source_language = self._language(text)

        url = "https://dictionary.yandex.net/dicservice.json/queryCorpus"
        params = {"sid": self._ucid(), "srv": "android", "src": text, "ui": "en", "lang": source_language + "-" + destination_language, "flags": 7}
        request = self.session.get(url, params=params)

        if request.status_code != 200:
            raise YandexTranslateException(request.status_code)

        response = request.json()

        _result = []

        for examples_group in response["result"]:
            for sentense in examples_group["examples"]:
                _sentense_result = sentense["dst"]
                _sentense_result = _sentense_result.replace("<", "").replace(">", "")
                _result.append(_sentense_result)

        return source_language, _result

    def _dictionary(self, text: str, destination_language: str, source_language: str):
        if source_language == "auto":
            source_language = self._language(text)

        url = "https://dictionary.yandex.net/dicservice.json/lookupMultiple"
        params = {"sid": self._ucid(), "srv": "android", "text": text, "ui": "en", "dict": source_language + "-" + destination_language, "flags": 7, "dict_type": "regular"}
        request = self.session.get(url, params=params)

        if request.status_code != 200:
            raise YandexTranslateException(request.status_code)
        response = request.json()

        _result = []

        for word in response["{}-{}".format(source_language, destination_language)]["regular"]:
            _word_result = word["tr"][0]["text"]
            _result.append(_word_result)

        return source_language, _result

    def _language_normalize(self, language):
        if language.id == "zho":
            return "zh"
        elif language.id == "srd":
            return "sjn"
        return language.alpha2

    def _language_denormalize(self, language_code):
        if str(language_code).lower() in {"zh", "zh-cn"}:
            return Language("zho")
        elif str(language_code).lower() == "sjn":
            return Language("srd")
        return Language(language_code)

    def __str__(self) -> str:
        return "Yandex"
