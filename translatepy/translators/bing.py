"""
This implementation was made specifically for translatepy from 'Zhymabek Roman', based on 'Anime no Sekai' version.
"""

import json
import os
import re
import time
from safeIO import JSONFile

from translatepy.exceptions import UnsupportedMethod
from translatepy.language import Language
from translatepy.translators.base import BaseTranslateException, BaseTranslator
from translatepy.utils.request import Request
from translatepy.utils.annotations import Callable, Dict

HOME_DIR = os.path.abspath(os.path.dirname(__file__))


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
    def __init__(self, request: Request, captcha_callback: Callable[[str], str] = None):
        self.session = request
        self._auth_session_file = JSONFile(os.path.join(HOME_DIR, ".bing_translatepy"), blocking=False)
        with self._auth_session_file as _auth_session:
            _auth_session_data = _auth_session.read()
        self.ig, self.iid, self.key, self.token, self.cookies = _auth_session_data.get("id"), _auth_session_data.get("iid"), _auth_session_data.get("key"), _auth_session_data.get("token"), _auth_session_data.get("cookies")
        self.captcha_callback = captcha_callback
        if not _auth_session_data:
            self._parse_authorization_data()

    def _parse_authorization_data(self):
        for _ in range(3):
            _request = self.session.get("https://www.bing.com/translator")
            _page = _request.text
            _parsed_IG = re.findall('IG:"(.*?)"', _page)
            _parsed_IID = re.findall('data-iid="(.*?)"', _page)
            _parsed_helper_info = re.findall("params_AbusePreventionHelper = (.*?);", _page)

            if not _parsed_helper_info:
                continue

            break
        else:
            raise BingTranslateException(message="Can't parse the authorization data, try again later or use MicrosoftTranslate")

        _normalized_key = json.loads(_parsed_helper_info[0])[0]
        _normalized_token = json.loads(_parsed_helper_info[0])[1]

        self.ig = _parsed_IG[0]
        self.iid = _parsed_IID[0]
        self.key = _normalized_key
        self.token = _normalized_token
        self.cookies = _request.cookies

    def send(self, url, data):
        # Try 2 times to make a request
        for _ in range(2):
            _params = {'IG': self.ig, 'IID': self.iid, "isVertical": 1}
            _data = {'token': self.token, 'key': self.key, "isAuthv2": True}
            _data.update(data)

            request = self.session.post(url, params=_params, data=_data, cookies=self.cookies)
            response = request.json()

            # Sometimes the Bing Translate API returns the response status code 200 along with the request, even if there is some kind of error.
            # It returns the error itself in the body of the request itself as "statusCode", lol.
            # Because of this, we have to predict where the real status of the response is.

            # We check the current response from the server, whether it is a dictionary. If yes, then we are trying to get the status code from the request itself, if there is no status code in the request body, then we simply take the status code in the response.
            if isinstance(response, Dict):
                status_code = response.get("statusCode", request.status_code)
            else:
                status_code = request.status_code

            # 200 - success
            # 400 - if the authorization tokens is expired, need to re-parse
            # 429 - if the service detects a lot of requests, it requires solving the captcha
            if status_code == 200:
                return response
            elif status_code == 400:
                try:
                    self._parse_authorization_data()
                except Exception:
                    raise BingTranslateException(status_code)
                else:
                    continue
            elif status_code == 429:
                # TODO
                # if response.get("ShowCaptcha", False):
                #     if self.captcha_callback:
                #         for _ in range(2):
                #             captcha, region, captcha_type, challenge_id = self._fetch_captcha()
                #             captcha_solution = self.captcha_callback(captcha)
                #             self._verify_captcha(captcha_solution, region, captcha_type, challenge_id)
                raise BingTranslateException(status_code)
            else:
                raise BingTranslateException(status_code)
        raise BingTranslateException(400)

    # def _fetch_captcha():
    #     pass

    # def _verify_captcha(solution: str, region: str, captcha_type: str, challenge_id: str):
    #     pass

class BingTranslate(BaseTranslator):
    """
    A Python implementation of Microsoft Bing Translation's APIs
    """

    _supported_languages = {'auto-detect', 'af', 'sq', 'am', 'ar', 'hy', 'as', 'az', 'bn', 'bs', 'bg', 'my', 'ca', 'ca', 'zh-Hans', 'cs', 'da', 'nl', 'nl', 'en', 'et', 'fj', 'fil', 'fil', 'fi', 'fr', 'fr-ca', 'de', 'ga', 'el', 'gu', 'ht', 'ht', 'he', 'hi', 'hr', 'hu', 'is', 'iu', 'id', 'it', 'ja', 'kn', 'kk', 'km', 'ko', 'ku', 'lo', 'lv', 'lt', 'ml', 'mi', 'mr', 'ms', 'mg', 'mt', 'ne', 'nb', 'nb', 'or', 'pa', 'pa', 'fa', 'pl', 'pt', 'ps', 'ps', 'ro', 'ro', 'ro', 'ru', 'sk', 'sl', 'sm', 'es', 'es', 'sr-Cyrl', 'sw', 'sv', 'ty', 'ta', 'te', 'th', 'ti', 'tlh-Latn', 'tlh-Latn', 'to', 'tr', 'uk', 'ur', 'vi', 'cy', 'zh-Hans', 'zh-Hant', 'yue', 'prs', 'mww', 'tlh-Piqd', 'kmr', 'pt-pt', 'otq', 'sr-Cyrl', 'sr-Latn', 'yua'}

    def __init__(self, request: Request = Request()):
        self.session_manager = BingSessionManager(request)
        self.session = request

    def _translate(self, text: str, destination_language: str, source_language: str) -> str:
        response = self.session_manager.send("https://www.bing.com/ttranslatev3", data={'text': text, 'fromLang': source_language, 'to': destination_language})
        try:
            _detected_language = response[0]["detectedLanguage"]["language"]
        except Exception:
            _detected_language = source_language
        return _detected_language, response[0]["translations"][0]["text"]

    def _example(self, text, destination_language, source_language) -> str:
        if source_language == "auto-detect":
            source_language = self._language(text)

        _detected_language, translation = self._translate(text, destination_language, source_language)

        response = self.session_manager.send("https://www.bing.com/texamplev3", data={'text': text.lower(), 'from': source_language, 'to': destination_language, 'translation': translation.lower()})
        return _detected_language, [BingExampleResult(example) for example in response[0]["examples"]]

    def _spellcheck(self, text: str, source_language: str) -> str:
        if source_language == "auto-detect":
            source_language = self._language(text)

        response = self.session_manager.send("https://www.bing.com/tspellcheckv3", data={'text': text, 'fromLang': source_language})
        result = response["correctedText"]
        if result == "":
            return source_language, text
        return source_language, result

    def _language(self, text: str) -> str:
        response = self.session_manager.send("https://www.bing.com/ttranslatev3", data={'text': text, 'fromLang': "auto-detect", 'to': "en"})
        return response[0]["detectedLanguage"]["language"]

    def _transliterate(self, text: str, destination_language: str, source_language: str):
        response = self.session_manager.send("https://www.bing.com/ttranslatev3", data={'text': text, 'fromLang': source_language, 'to': destination_language})
        # XXX: Not a predictable response from Bing Translate
        try:
            return source_language, response[1]["inputTransliteration"]
        except IndexError:
            try:
                return source_language, response[0]["translations"][0]["transliteration"]["text"]
            except Exception:
                return source_language, text

    def _dictionary(self, text: str, destination_language: str, source_language: str):
        if source_language == "auto-detect":
            source_language = self._language(text)

        response = self.session_manager.send("https://www.bing.com/tlookupv3", data={'text': text, 'from': source_language, 'to': destination_language})
        _result = []
        for _dictionary in response[0]["translations"]:
            _dictionary_result = _dictionary["displayTarget"]
            _result.append(_dictionary_result)
        return source_language, _result

    def _text_to_speech(self, text: str, speed: int, gender: str, source_language: str):
        raise BingTranslateException(status_code=719, message="DEPRECATED! Use Microsoft Translate's text to spech method")

    def _language_normalize(self, language):
        _language = Language(language)
        if _language.id == "auto":
            return "auto-detect"
        elif language.id == "zho":
            return "zh-Hans"
        elif language.id == "och":
            return "zh-Hant"
        return _language.alpha2

    def _language_denormalize(self, language_code):
        if str(language_code) == "auto-detect":
            return Language("auto")
        elif str(language_code).lower() in {"zh-cn", "zh-hans"}:
            return Language("zho")
        elif str(language_code).lower() == "zh-tw":
            return Language("och")
        return Language(language_code)

    def __str__(self) -> str:
        return "Microsoft Bing"
