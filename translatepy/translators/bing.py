"""
This implementation was made specifically for translatepy from 'Zhymabek Roman', based on 'Anime no Sekai' version.
"""

import json
import re
import typing

import cain
import cain.types

from translatepy import models
from translatepy.__info__ import __translatepy_dir__
from translatepy.exceptions import UnsupportedMethod
from translatepy.language import Language
from translatepy.translators.base import BaseTranslateException, BaseTranslator
from translatepy.utils import request


class BingTranslateException(BaseTranslateException):
    error_codes = {
        429: "Too many requests"
    }


class BingSessionData(cain.types.Object):
    """Bing session data holder"""
    ig: str
    iid: str
    key: str
    token: str
    cookies_keys: typing.List[str]
    cookies_values: typing.List[str]


class BingSessionManager():
    """
    Creates and manages a Bing session
    """

    def __init__(self, session: request.Session, captcha_callback: typing.Callable[[str], str] = None):
        self.session = session
        self._auth_session_file = __translatepy_dir__ / "sessions" / "bing.cain"
        try:
            with self._auth_session_file.open("rb") as file:
                _auth_session_data = cain.load(file, BingSessionData)
            self.ig = _auth_session_data.ig
            self.iid = _auth_session_data.iid
            self.key = _auth_session_data.key
            self.token = _auth_session_data.token
            self.cookies = {key: _auth_session_data.cookies_values[index] for index, key in enumerate(_auth_session_data.cookies_keys)}
            self.captcha_callback = captcha_callback
        except Exception:
            self._parse_authorization_data()
            _auth_session_data = BingSessionData({
                "ig": self.ig,
                "iid": self.iid,
                "key": self.key,
                "token": self.token,
                "cookies_keys": list(self.cookies.keys()),
                "cookies_values": list(self.cookies.values())
            })
            self._auth_session_file.mkdir(parents=True, exist_ok=True)
            with self._auth_session_file.open("wb") as file:
                cain.dump(_auth_session_data, file, BingSessionData)

    def _parse_authorization_data(self):
        for _ in range(3):
            _request = self.session.get("https://www.bing.com/translator")
            _page = _request.text
            _parsed_ig = re.findall('IG:"(.*?)"', _page)
            _parsed_iid = re.findall('data-iid="(.*?)"', _page)
            _parsed_helper_info = re.findall("params_AbusePreventionHelper = (.*?);", _page)
            if not _parsed_helper_info:
                continue
            break
        else:
            raise BingTranslateException(message="Can't parse the authorization data, try again later or use MicrosoftTranslate")

        _normalized_key = json.loads(_parsed_helper_info[0])[0]
        _normalized_token = json.loads(_parsed_helper_info[0])[1]

        self.ig = _parsed_ig[0]
        self.iid = _parsed_iid[0]
        self.key = _normalized_key
        self.token = _normalized_token
        self.cookies = _request.cookies

    def send(self, url, data):
        """Sends requestts to the API"""
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
            if isinstance(response, typing.Dict):
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

    _supported_languages = {'ur', 'hy', 'fil', 'th', 'nl', 'auto-detect', 'gu', 'sr-Latn', 'ar', 'lo', 'da', 'my', 'ja', 'otq', 'ms',
                            'is', 'sl', 'zh-Hans', 'tr', 'pt-pt', 'mt', 'bn', 'sk', 'el', 'ti', 'ty', 'sv', 'yue', 'lv', 'fr-ca', 'ca',
                            'he', 'fi', 'it', 'nb', 'mi', 'prs', 'ps', 'az', 'sm', 'es', 'ko', 'tlh-Piqd', 'pt', 'iu', 'bs', 'zh-Hant',
                            'mww', 'pa', 'km', 'as', 'en', 'id', 'am', 'sw', 'cy', 'ne', 'ta', 'de', 'hu', 'sq', 'ro', 'kmr', 'kk', 'hi',
                            'hr', 'tlh-Latn', 'ga', 'fr', 'te', 'ht', 'lt', 'fa', 'or', 'mr', 'vi', 'pl', 'fj', 'to', 'kn', 'yua', 'uk',
                            'sr-Cyrl', 'et', 'af', 'bg', 'ku', 'cs', 'ml', 'ru', 'mg'}

    def __init__(self, session=None):
        super().__init__(session)
        self.session_manager = BingSessionManager(self.session)

    def _translate(self, text: str, dest_lang: typing.Any, source_lang: typing.Any):
        response = self.session_manager.send("https://www.bing.com/ttranslatev3", data={'text': text, 'fromLang': source_lang, 'to': dest_lang})
        try:
            lang = response[0]["detectedLanguage"]["language"]
        except Exception:
            lang = None
        return models.TranslationResult(source_lang=lang, translation=response[0]["translations"][0]["text"])

    def _example(self, text: str, source_lang: typing.Any):
        if source_lang == "auto-detect":
            source_lang = self._language_to_code(self.language(text).language)

        # source_lang to source_lang ?
        response = self.session_manager.send("https://www.bing.com/texamplev3", data={'text': text.lower(), 'from': source_lang, 'to': source_lang, 'translation': text.lower()})
        results = []
        for example in response[0]["examples"]:
            try:
                example = dict(example)
                # sourceTerm or targetTerm ?
                final = "".join([example.get("sourcePrefix", ""), example.get("sourceTerm", ""), example.get("sourceSuffix", "")])
                results.append(models.ExampleResult(
                    source_lang=source_lang,
                    example=final,
                    raw=example
                ))
            except Exception:
                continue
        return results

    def _spellcheck(self, text: str, source_lang: typing.Any):
        if source_lang == "auto-detect":
            source_lang = self._language_to_code(self.language(text).language)

        response = self.session_manager.send("https://www.bing.com/tspellcheckv3", data={'text': text, 'fromLang': source_lang})
        result = response["correctedText"]
        if result == "":
            return models.SpellcheckResult(raw=response, corrected=result, source_lang=source_lang)
        return models.SpellcheckResult(raw=response, corrected=result, source_lang=source_lang)

    def _language(self, text: str):
        response = self.session_manager.send("https://www.bing.com/ttranslatev3", data={'text': text, 'fromLang': "auto-detect", 'to': "en"})
        return models.LanguageResult(raw=response, language=response[0]["detectedLanguage"]["language"])

    def _transliterate(self, text: str, dest_lang: typing.Any, source_lang: typing.Any):
        response = self.session_manager.send("https://www.bing.com/ttranslatev3", data={'text': text, 'fromLang': source_lang, 'to': dest_lang})
        # Note: Not a predictable response from Bing Translate
        try:
            return models.TransliterationResult(raw=response, transliteration=response[1]["inputTransliteration"])
        except IndexError:
            try:
                return models.TransliterationResult(raw=response, transliteration=response[0]["translations"][0]["transliteration"]["text"])
            except Exception:
                raise UnsupportedMethod("Bing couldn't return a suitable response")

    def _dictionary(self, text: str, source_lang: typing.Any):
        raise UnsupportedMethod
        if source_lang == "auto-detect":
            source_lang = self._language(text)

        response = self.session_manager.send("https://www.bing.com/tlookupv3", data={'text': text, 'from': source_lang, 'to': source_lang})
        _result = []
        for _dictionary in response[0]["translations"]:
            _dictionary_result = _dictionary["displayTarget"]
            _result.append(_dictionary_result)
        # TODO
        return source_lang, _result

    def _text_to_speech(self, text: str, speed: int, gender: models.Gender, source_lang: typing.Any):
        raise BingTranslateException(status_code=719, message="DEPRECATED! Use Microsoft Translate's text to spech method")

    def _language_to_code(self, language: Language):
        if language.id == "auto":
            return "auto-detect"
        elif language.id == "zho":
            return "zh-Hans"
        elif language.id == "och":
            return "zh-Hant"
        return language.alpha2

    def _code_to_language(self, code: typing.Union[str, typing.Any]) -> Language:
        language_code = str(code).lower()
        if language_code == "auto-detect":
            return Language("auto")
        elif language_code.lower() in {"zh-cn", "zh-hans"}:
            return Language("zho")
        elif language_code.lower() == "zh-tw":
            return Language("och")
        return Language(language_code)

    def __str__(self) -> str:
        return "Microsoft Bing"
