"""
This implementation was made specifically for translatepy by 'Zhymabek Roman'.
"""

import json
import re
import os
import uuid
import time
from safeIO import JSONFile

from translatepy.exceptions import UnsupportedMethod
from translatepy.language import Language
from translatepy.translators.base import BaseTranslateException, BaseTranslator
from translatepy.utils.request import Request
from translatepy.utils.annotations import Callable, Dict
from translatepy.translators.bing import BingSessionManager, BingExampleResult

HOME_DIR = os.path.abspath(os.path.dirname(__file__))


class MicrosoftException(BaseTranslateException):
    error_codes = {
        429: "Too many requests"
    }


class MicrosoftSessionManager():
    def __init__(self, request: Request):
        self.session = request
        self.bing_session = BingSessionManager(request)

        self._auth_session_file = JSONFile(os.path.join(HOME_DIR, ".microsoft_translatepy"), blocking=False)
        with self._auth_session_file as _auth_session:
            _auth_session_data = _auth_session.read()
        self._region, self._token, self._token_expiries = _auth_session_data.get("region"), _auth_session_data.get("token"), _auth_session_data.get("token_expiries", 0)
        self._parse_authorization_data()

    def _parse_authorization_data(self, force: bool = False):
        if not self._token or time.time() > self._token_expiries or force:
            # authentication token is valid for 10 minutes
            token_response = self.bing_session.send("https://www.bing.com/tfetspktok", data={})
            token_status = token_response.get("statusCode", 200)

            if token_status != 200:
                raise MicrosoftException(token_status, "Error during token request from the server")

            self._token, self._region = token_response.get("token"), token_response.get("region")
            self._token_expiries = time.time() + (int(token_response.get("expiryDurationInMS", 600000)) - 1000) / 1000

            self._auth_session_file.write({"token": self._token, "region": self._region, "token_expiries": self._token_expiries})

    def send(self, url, data, params: Dict = {}):
        # Try 2 times to make a request
        for _ in range(2):
            headers = {
                'Authorization': 'Bearer {token}'.format(token=self._token),
                'Content-type': 'application/json',
                'X-ClientTraceId': str(uuid.uuid4())
            }
            _params = {'api-version': '3.0'}
            _params.update(params)

            request = self.session.post(url, params=_params, json=data, headers=headers)
            response = request.json()

            if request.status_code != 200:
                error = response.get("error", {})
                if error.get("code", request.status_code) == 401000:
                    self._parse_authorization_data(force=True)
                    continue
                raise MicrosoftException(status_code=error.get("code"), message=error.get("message", "Unknown"))

            return response

class MicrosoftTranslate(BaseTranslator):
    """
    A Python implementation of Microsoft Translation's APIs
    """

    _supported_languages = {'auto', 'af', 'sq', 'am', 'ar', 'hy', 'as', 'az', 'bn', 'bs', 'bg', 'my', 'ca', 'ca', 'zh-Hans', 'cs', 'da', 'nl', 'nl', 'en', 'et', 'fj', 'fil', 'fil', 'fi', 'fr', 'fr-ca', 'de', 'ga', 'el', 'gu', 'ht', 'ht', 'he', 'hi', 'hr', 'hu', 'is', 'iu', 'id', 'it', 'ja', 'kn', 'kk', 'km', 'ko', 'ku', 'lo', 'lv', 'lt', 'ml', 'mi', 'mr', 'ms', 'mg', 'mt', 'ne', 'nb', 'nb', 'or', 'pa', 'pa', 'fa', 'pl', 'pt', 'ps', 'ps', 'ro', 'ro', 'ro', 'ru', 'sk', 'sl', 'sm', 'es', 'es', 'sr-Cyrl', 'sw', 'sv', 'ty', 'ta', 'te', 'th', 'ti', 'tlh-Latn', 'tlh-Latn', 'to', 'tr', 'uk', 'ur', 'vi', 'cy', 'zh-Hans', 'zh-Hant', 'yue', 'prs', 'mww', 'tlh-Piqd', 'kmr', 'pt-pt', 'otq', 'sr-Cyrl', 'sr-Latn', 'yua'}

    def __init__(self, request: Request = Request()):
        self.session_manager = MicrosoftSessionManager(request)
        self.session = request

    def _translate(self, text: str, destination_language: str, source_language: str) -> str:
        if source_language == "auto":
            source_language = self._language(text)

        response = self.session_manager.send("https://api.cognitive.microsofttranslator.com/translate", params={'from': source_language, 'to': destination_language}, data=[{"text": text}])
        return source_language, response[0]["translations"][0]["text"]

    def _example(self, text, destination_language, source_language) -> str:
        source_language, translation = self._translate(text, destination_language, source_language)

        response = self.session_manager.send("https://api.cognitive.microsofttranslator.com/dictionary/examples", params={'from': source_language, 'to': destination_language}, data=[{'Text': text.lower(), 'Translation': translation.lower()}])
        return source_language, [BingExampleResult(example) for example in response[0]["examples"]]

    def _language(self, text: str) -> str:
        response = self.session_manager.send("https://api.cognitive.microsofttranslator.com/detect", data=[{"text": text}])
        return response[0]["language"]

    # def _transliterate(self, text: str, destination_language: str, source_language: str):
        # TODO: Implement

    def _dictionary(self, text: str, destination_language: str, source_language: str):
        source_language = self._language(text)

        response = self.session_manager.send("https://api.cognitive.microsofttranslator.com/dictionary/lookup", data=[{'text': text}], params={'from': source_language, 'to': destination_language})
        _result = []
        for _dictionary in response[0]["translations"]:
            _dictionary_result = _dictionary["displayTarget"]
            _result.append(_dictionary_result)
        return source_language, _result

    def _text_to_speech(self, text: str, speed: int, gender: str, source_language: str):
        if source_language == "auto":
            source_language = self._language(text)

        gender = gender.capitalize()

        _supported_langs_url = "https://{region}.tts.speech.microsoft.com/cognitiveservices/voices/list".format(region=self.session_manager._region)
        _supported_langs_list = self.session_manager.send(_supported_langs_url)

        # all locals list: {('zh-HK', 'zh-HK'), ('de', 'de-DE'), ('da', 'da-DK'), ('id', 'id-ID'), ('ko', 'ko-KR'), ('en', 'en-NZ'), ('el', 'el-GR'), ('ms', 'ms-MY'), ('es', 'es-AR'), ('ro', 'ro-RO'), ('pl', 'pl-PL'), ('it', 'it-IT'), ('hr', 'hr-HR'), ('pt', 'pt-PT'), ('hu', 'hu-HU'), ('sw', 'sw-KE'), ('en', 'en-GB'), ('mt', 'mt-MT'), ('tr', 'tr-TR'), ('ar', 'ar-EG'), ('fr', 'fr-CA'), ('te', 'te-IN'), ('fr', 'fr-BE'), ('en', 'en-SG'), ('zh-CN', 'zh-CN'), ('fr', 'fr-FR'), ('en', 'en-PH'), ('cs', 'cs-CZ'), ('fi', 'fi-FI'), ('zh-TW', 'zh-TW'), ('de', 'de-CH'), ('nb', 'nb-NO'), ('bg', 'bg-BG'), ('he', 'he-IL'), ('en', 'en-CA'), ('en', 'en-HK'), ('es', 'es-MX'), ('en', 'en-AU'), ('th', 'th-TH'), ('pt', 'pt-BR'), ('mr', 'mr-IN'), ('sk', 'sk-SK'), ('ru', 'ru-RU'), ('nl', 'nl-NL'), ('en', 'en-US'), ('ta', 'ta-IN'), ('hi', 'hi-IN'), ('cy', 'cy-GB'), ('ar', 'ar-SA'), ('ga', 'ga-IE'), ('nl', 'nl-BE'), ('de', 'de-AT'), ('ca', 'ca-ES'), ('uk', 'uk-UA'), ('es', 'es-CO'), ('es', 'es-ES'), ('es', 'es-US'), ('en', 'en-ZA'), ('ur', 'ur-PK'), ('sv', 'sv-SE'), ('lv', 'lv-LV'), ('lt', 'lt-LT'), ('vi', 'vi-VN'), ('et', 'et-EE'), ('en', 'en-IN'), ('en', 'en-IE'), ('ja', 'ja-JP'), ('fr', 'fr-CH'), ('gu', 'gu-IN'), ('sl', 'sl-SI')}
        _locals = {'zh-CN': 'zh-CN', 'mr': 'mr-IN', 'en': 'en-US', 'ru': 'ru-RU', 'el': 'el-GR', 'es': 'es-CO', 'id': 'id-ID', 'pt': 'pt-PT', 'ko': 'ko-KR', 'ta': 'ta-IN', 'te': 'te-IN', 'et': 'et-EE', 'pl': 'pl-PL', 'it': 'it-IT', 'ms': 'ms-MY', 'mt': 'mt-MT', 'ro': 'ro-RO', 'vi': 'vi-VN', 'bg': 'bg-BG', 'zh-TW': 'zh-TW', 'tr': 'tr-TR', 'de': 'de-CH', 'fr': 'fr-CH', 'nb': 'nb-NO', 'nl': 'nl-BE', 'uk': 'uk-UA', 'he': 'he-IL', 'ur': 'ur-PK', 'hi': 'hi-IN', 'ja': 'ja-JP', 'hr': 'hr-HR', 'sv': 'sv-SE', 'hu': 'hu-HU', 'sw': 'sw-KE', 'lt': 'lt-LT', 'sl': 'sl-SI', 'fi': 'fi-FI', 'lv': 'lv-LV', 'sk': 'sk-SK', 'da': 'da-DK', 'cy': 'cy-GB', 'gu': 'gu-IN', 'ga': 'ga-IE', 'th': 'th-TH', 'ar': 'ar-EG', 'ca': 'ca-ES', 'zh-HK': 'zh-HK', 'cs': 'cs-CZ'}
        _source_local = _locals.get(source_language)

        for _supported_lang in _supported_langs_list:
            if _supported_lang["Locale"] == _source_local and _supported_lang["Gender"] == gender:
                voice = _supported_lang["ShortName"]
                break
        else:
            raise UnsupportedMethod("Microsoft Translate doesn't support {source_lang} language".format(source_lang=source_language))

        speech_url = "https://{region}.tts.speech.microsoft.com/cognitiveservices/v1".format(region=self.session_manager._region)
        headers = {"authorization": "Bearer {token}".format(token=self.session_manager._token), "content-type": "application/ssml+xml", "x-microsoft-outputformat": "audio-48khz-192kbitrate-mono-mp3"}
        data = "<speak version='1.0' xml:lang='{local}'><voice xml:lang='{local}' xml:gender='{gender}' name='{voice}'><prosody rate='{speed}%'>{text}</prosody></voice></speak>".format(text=text, gender=gender, speed=float(speed - 100), local=_source_local, voice=voice)
        spech_result = self.session.post(speech_url, data=data.encode('utf-8'), headers=headers)
        return source_language, spech_result.content

    def _language_normalize(self, language):
        _language = Language(language)
        if language.id == "zho":
            return "zh-Hans"
        elif language.id == "och":
            return "zh-Hant"
        return _language.alpha2

    def _language_denormalize(self, language_code):
        if str(language_code).lower() in {"zh-cn", "zh-hans"}:
            return Language("zho")
        elif str(language_code).lower() == "zh-tw":
            return Language("och")
        return Language(language_code)

    def __str__(self) -> str:
        return "Microsoft Translate"
