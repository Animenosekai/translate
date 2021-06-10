"""
This implementation was made specifically for translatepy from 'Zhymabek Roman', based on 'Anime no Sekai' version.
"""

import re
import json
import requests
import pyuseragents

from translatepy.translators.base import BaseTranslator, BaseTranslateException
from translatepy.exceptions import UnsupportedMethod
from translatepy.utils.request import Request

HEADERS = {
    # "Host": "www.bing.com",
    "User-Agent": pyuseragents.random(),
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    # "Referer": "https://www.bing.com/",
    "Content-Type": "application/x-www-form-urlencoded",
    "Connection": "keep-alive"
}

# TODO: read documentation: https://docs.microsoft.com/ru-ru/azure/cognitive-services/translator/language-support


class BingTranslateException(BaseTranslateException):
    error_codes = {
        429: "Too many requests"
    }


class BingExampleResult():

    class SourceExample():
        """The source for an example"""
        def __init__(self, data) -> None:
            self._data = data
            self.prefix = self._data.get("sourcePrefix", "")
            self.term = self._data.get("sourceTerm", "")
            self.suffix = self._data.get("sourceSuffix", "")
            self.example = self.prefix + self.term + self.suffix

        def __repr__(self) -> str:
            return str(self.example)

    class DestinationExample():
        """The target language example"""
        def __init__(self, data) -> None:
            self._data = data
            self.prefix = self._data.get("targetPrefix", "")
            self.term = self._data.get("targetTerm", "")
            self.suffix = self._data.get("targetSuffix", "")
            self.example = self.prefix + self.term + self.suffix

        def __repr__(self) -> str:
            return str(self.example)

    def __init__(self, data) -> None:
        self._data = data
        self.source = self.SourceExample(self._data)
        self.destination = self.DestinationExample(self._data)

    def __repr__(self) -> str:
        return str(self.source)


class BingSessionManager():
    def __init__(self, request: Request):
        self.session = request
        self._parse_authorization_data()

    def _parse_authorization_data(self):
        _page = requests.get("https://www.bing.com/translator").text
        _parsed_IG = re.findall('IG:"(.*?)"', _page)
        _parsed_IID = re.findall('data-iid="(.*?)"', _page)
        _parsed_helper_info = re.findall("params_RichTranslateHelper = (.*?);", _page)

        _normalized_key = json.loads(_parsed_helper_info[0])[0]
        _normalized_token = json.loads(_parsed_helper_info[0])[1]

        self.ig = _parsed_IG[0]
        self.iid = _parsed_IID[0]
        self.key = _normalized_key
        self.token = _normalized_token

    def send(self, url, data):
        # Try 5 times to make a request
        for _ in range(5):
            _params = {'IG': self.ig, 'IID': self.iid, "isVertical": 1}
            _data = {'token': self.token, 'key': self.key}
            _data.update(data)

            request = requests.post(url, params=_params, data=_data, headers=HEADERS)
            response = request.json()

            if isinstance(response, dict):
                status_code = response.get("statusCode", 200)
            else:
                status_code = request.status_code

            if status_code == 200:
                return response
            # elif status_code == 400:
            #     self._parse_authorization_data()
            else:
                raise BingTranslateException(status_code)


class BingTranslate(BaseTranslator):
    """
    A Python implementation of Microsoft Bing Translation's APIs
    """

    def __init__(self, request: Request = Request()):
        self.session_manager = BingSessionManager(request)

    def _translate(self, text: str, destination_language: str, source_language: str) -> str:
        response = self.session_manager.send("https://www.bing.com/ttranslatev3", data={'text': text, 'fromLang': source_language, 'to': destination_language})
        return response[0]["translations"][0]["text"]

    def _example(self, text, destination_language, source_language) -> str:
        if source_language == "auto-detect":
            source_language = self._language(text)

        translation = self._translate(text, destination_language, source_language)

        response = self.session_manager.send("https://www.bing.com/texamplev3", data={'text': text.lower(), 'from': source_language, 'to': destination_language, 'translation': translation.lower()})
        return [BingExampleResult(example) for example in response[0]["examples"]]

    def _spellcheck(self, text: str, source_language: str) -> str:
        if source_language == "auto-detect":
            source_language = self._language(text)

        response = self.session_manager.send("https://www.bing.com/tspellcheckv3", data={'text': text, 'fromLang': source_language})
        result = response["correctedText"]
        if result == "":
            return text
        return result

    def _language(self, text: str) -> str:
        response = self.session_manager.send("https://www.bing.com/ttranslatev3", data={'text': text, 'fromLang': "auto-detect", 'to': "en"})
        return response[0]["detectedLanguage"]["language"]

    def _transliterate(self, text: str, destination_language: str, source_language: str):
        # TODO: alternative api endpoint won't work
        # response = self.session_manager.send("https://www.bing.com/ttransliteratev3", data={'text': text, 'language': source_language, 'toScript': destination_language})
        response = self.session_manager.send("https://www.bing.com/ttranslatev3", data={'text': text, 'fromLang': source_language, 'to': destination_language})
        # XXX: Not a predictable response from Bing Translate
        try:
            return response[1]["inputTransliteration"]
        except IndexError:
            try:
                return response[0]["translations"][0]["transliteration"]["text"]
            except Exception:
                return text

    def _dictionary(self, text: str, destination_language: str, source_language: str):
        if source_language == "auto-detect":
            source_language = self._language(text)

        response = self.session_manager.send("https://www.bing.com/tlookupv3", data={'text': text, 'from': source_language, 'to': destination_language})
        _result = []
        for _dictionary in response[0]["translations"]:
            _dictionary_result = _dictionary["displayTarget"]
            _result.append(_dictionary_result)
        return _result

    def _text_to_speech(self, text: str, source_language: str):
        # TODO: Implement
        raise UnsupportedMethod("Bing Translate doesn't support this method")

    def _language_normalize(self, language):
        # TODO

        _normalized_language_code = language.alpha2

        if _normalized_language_code == "auto":
            return "auto-detect"
        elif _normalized_language_code == "no":
            return "nb"
        elif _normalized_language_code == "pt":
            return "pt-pt"
        elif _normalized_language_code == "zh-cn":
            return "zh-Hans"
        elif _normalized_language_code == "zh-tw":
            return "zh-Hant"
        else:
            return _normalized_language_code

    def __repr__(self) -> str:
        return "Microsoft Bing Translator"
