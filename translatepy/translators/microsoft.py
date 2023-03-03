"""
This implementation was made specifically for translatepy by 'Zhymabek Roman'.
"""

import json
import os
import pathlib
import time
import typing
import uuid

from translatepy import exceptions, models
from translatepy.language import Language
from translatepy.translators.base import (BaseTranslateException,
                                          BaseTranslator, C)
from translatepy.translators.bing import BingSessionManager
from translatepy.utils import request

HOME_DIR = os.path.abspath(os.path.dirname(__file__))


class MicrosoftException(BaseTranslateException):
    error_codes = {
        429: "Too many requests"
    }


class MicrosoftSessionManager:
    """
    Manages `Microsoft` sessions
    """

    def __init__(self, request: request.Session):
        self.session = request
        self.bing_session = BingSessionManager(request)

        self._auth_session_file = pathlib.Path(__file__).parent / ".bing.translatepy"
        _auth_session_data = json.loads(self._auth_session_file.read_text())

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

            self._auth_session_file.write_text(json.dumps({"token": self._token, "region": self._region, "token_expiries": self._token_expiries}, ensure_ascii=False, separators=(",", ":")))

    def send(self, url, data, params: typing.Dict = {}):
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

    _supported_languages = {'af', 'am', 'ar', 'as', 'auto', 'az', 'bg', 'bn', 'bs', 'ca', 'cs', 'cy', 'da', 'de', 'el', 'en', 'es', 'et', 'fa',
                            'fi', 'fil', 'fj', 'fr', 'fr-ca', 'ga', 'gu', 'he', 'hi', 'hr', 'ht', 'hu', 'hy', 'id', 'is', 'it', 'iu', 'ja', 'kk',
                            'km', 'kmr', 'kn', 'ko', 'ku', 'lo', 'lt', 'lv', 'mg', 'mi', 'ml', 'mr', 'ms', 'mt', 'mww', 'my', 'nb', 'ne', 'nl', 'or',
                            'otq', 'pa', 'pl', 'prs', 'ps', 'pt', 'pt-pt', 'ro', 'ru', 'sk', 'sl', 'sm', 'sq', 'sr-Cyrl', 'sr-Latn', 'sv', 'sw', 'ta',
                            'te', 'th', 'ti', 'tlh-Latn', 'tlh-Piqd', 'to', 'tr', 'ty', 'uk', 'ur', 'vi', 'yua', 'yue', 'zh-Hans', 'zh-Hant'}

    def __init__(self, session: typing.Optional[request.Session] = None):
        super().__init__(session)
        self.session_manager = MicrosoftSessionManager(self.session)

    def _translate(self: C, text: str, dest_lang: typing.Any, source_lang: typing.Any) -> models.TranslationResult[C]:
        if source_lang == "auto":
            source_lang = self._language_to_code(self.language(text).language)

        response = self.session_manager.send("https://api.cognitive.microsofttranslator.com/translate", params={'from': source_lang, 'to': dest_lang}, data=[{"text": text}])
        return models.TranslationResult(source_lang=source_lang, raw=response, translation=response[0]["translations"][0]["text"])

    def _example(self: C, text: str, source_lang: typing.Any) -> typing.Union[models.ExampleResult[C], typing.List[models.ExampleResult[C]]]:
        # source_lang, translation = self._translate(text, source_lan, source_lang)

        response = self.session_manager.send("https://api.cognitive.microsofttranslator.com/dictionary/examples", params={'from': source_lang, 'to': source_lang}, data=[{'Text': text.lower(), 'Translation': text.lower()}])
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

    def _language(self: C, text: str) -> models.LanguageResult[C]:
        response = self.session_manager.send("https://api.cognitive.microsofttranslator.com/detect", data=[{"text": text}])
        return models.LanguageResult(raw=response, language=response[0]["language"])

    # TODO: Implement `_transliterate``

    def _dictionary(self: C, text: str, source_lang: typing.Any) -> typing.Union[typing.Union[models.DictionaryResult[C], models.RichDictionaryResult[C]], typing.List[typing.Union[models.DictionaryResult[C], models.RichDictionaryResult[C]]]]:
        # TODO: Need to reimplement
        raise exceptions.UnsupportedMethod("Need to reimplement")
        source_lang = self._language(text)

        dest_lang = source_lang  # ?

        response = self.session_manager.send("https://api.cognitive.microsofttranslator.com/dictionary/lookup", data=[{'text': text}], params={'from': source_lang, 'to': dest_lang})
        _result = []
        for _dictionary in response[0]["translations"]:
            _dictionary_result = _dictionary["displayTarget"]
            _result.append(_dictionary_result)
        return source_lang, _result

    def _text_to_speech(self: C, text: str, speed: int, gender: models.Gender, source_lang: typing.Any) -> models.TextToSpechResult[C]:
        if source_lang == "auto":
            source_lang = self._language_to_code(self.language(text).language)

        if gender is not models.Gender.OTHER and gender is not models.Gender.GENDERLESS:
            gender = models.Gender.MALE

        final_gender = gender.value.capitalize()

        _supported_langs_url = "https://{region}.tts.speech.microsoft.com/cognitiveservices/voices/list".format(region=self.session_manager._region)
        _supported_langs_list = self.session_manager.send(_supported_langs_url, data={})  # FIXME: No value for `data`

        # all locals list: {('zh-HK', 'zh-HK'), ('de', 'de-DE'), ('da', 'da-DK'), ('id', 'id-ID'), ('ko', 'ko-KR'), ('en', 'en-NZ'), ('el', 'el-GR'), ('ms', 'ms-MY'), ('es', 'es-AR'), ('ro', 'ro-RO'), ('pl', 'pl-PL'), ('it', 'it-IT'), ('hr', 'hr-HR'), ('pt', 'pt-PT'), ('hu', 'hu-HU'), ('sw', 'sw-KE'), ('en', 'en-GB'), ('mt', 'mt-MT'), ('tr', 'tr-TR'), ('ar', 'ar-EG'), ('fr', 'fr-CA'), ('te', 'te-IN'), ('fr', 'fr-BE'), ('en', 'en-SG'), ('zh-CN', 'zh-CN'), ('fr', 'fr-FR'), ('en', 'en-PH'), ('cs', 'cs-CZ'), ('fi', 'fi-FI'), ('zh-TW', 'zh-TW'), ('de', 'de-CH'), ('nb', 'nb-NO'), ('bg', 'bg-BG'), ('he', 'he-IL'), ('en', 'en-CA'), ('en', 'en-HK'), ('es', 'es-MX'), ('en', 'en-AU'), ('th', 'th-TH'), ('pt', 'pt-BR'), ('mr', 'mr-IN'), ('sk', 'sk-SK'), ('ru', 'ru-RU'), ('nl', 'nl-NL'), ('en', 'en-US'), ('ta', 'ta-IN'), ('hi', 'hi-IN'), ('cy', 'cy-GB'), ('ar', 'ar-SA'), ('ga', 'ga-IE'), ('nl', 'nl-BE'), ('de', 'de-AT'), ('ca', 'ca-ES'), ('uk', 'uk-UA'), ('es', 'es-CO'), ('es', 'es-ES'), ('es', 'es-US'), ('en', 'en-ZA'), ('ur', 'ur-PK'), ('sv', 'sv-SE'), ('lv', 'lv-LV'), ('lt', 'lt-LT'), ('vi', 'vi-VN'), ('et', 'et-EE'), ('en', 'en-IN'), ('en', 'en-IE'), ('ja', 'ja-JP'), ('fr', 'fr-CH'), ('gu', 'gu-IN'), ('sl', 'sl-SI')}
        _locals = {'zh-CN': 'zh-CN', 'mr': 'mr-IN', 'en': 'en-US', 'ru': 'ru-RU', 'el': 'el-GR', 'es': 'es-CO',
                   'id': 'id-ID', 'pt': 'pt-PT', 'ko': 'ko-KR', 'ta': 'ta-IN', 'te': 'te-IN', 'et': 'et-EE',
                   'pl': 'pl-PL', 'it': 'it-IT', 'ms': 'ms-MY', 'mt': 'mt-MT', 'ro': 'ro-RO', 'vi': 'vi-VN',
                   'bg': 'bg-BG', 'zh-TW': 'zh-TW', 'tr': 'tr-TR', 'de': 'de-CH', 'fr': 'fr-CH', 'nb': 'nb-NO',
                   'nl': 'nl-BE', 'uk': 'uk-UA', 'he': 'he-IL', 'ur': 'ur-PK', 'hi': 'hi-IN', 'ja': 'ja-JP',
                   'hr': 'hr-HR', 'sv': 'sv-SE', 'hu': 'hu-HU', 'sw': 'sw-KE', 'lt': 'lt-LT', 'sl': 'sl-SI',
                   'fi': 'fi-FI', 'lv': 'lv-LV', 'sk': 'sk-SK', 'da': 'da-DK', 'cy': 'cy-GB', 'gu': 'gu-IN',
                   'ga': 'ga-IE', 'th': 'th-TH', 'ar': 'ar-EG', 'ca': 'ca-ES', 'zh-HK': 'zh-HK', 'cs': 'cs-CZ'}

        _source_local = _locals.get(source_lang)

        for _supported_lang in _supported_langs_list:
            if _supported_lang["Locale"] == _source_local and _supported_lang["Gender"] == final_gender:
                voice = _supported_lang["ShortName"]
                break
        else:
            for _supported_lang in _supported_langs_list:
                if _supported_lang["Locale"] == _source_local:  # `gender` is an optional parameter
                    voice = _supported_lang["ShortName"]
                    break
            else:
                raise exceptions.NoResult("Microsoft Translate doesn't support {source_lang} for text to speech conversions".format(source_lang=source_lang))

        speech_url = "https://{region}.tts.speech.microsoft.com/cognitiveservices/v1".format(region=self.session_manager._region)
        headers = {"authorization": "Bearer {token}".format(token=self.session_manager._token), "content-type": "application/ssml+xml", "x-microsoft-outputformat": "audio-48khz-192kbitrate-mono-mp3"}
        data = "<speak version='1.0' xml:lang='{local}'><voice xml:lang='{local}' xml:gender='{gender}' name='{voice}'><prosody rate='{speed}%'>{text}</prosody></voice></speak>".format(text=text, gender=final_gender, speed=float(speed - 100), local=_source_local, voice=voice)
        spech_result = self.session.post(speech_url, data=data.encode('utf-8'), headers=headers)

        return models.TextToSpechResult(source_lang=source_lang, result=spech_result.content)

    def _language_to_code(self, language: Language) -> typing.Union[str, typing.Any]:
        if language.id == "zho":
            return "zh-Hans"
        elif language.id == "och":
            return "zh-Hant"
        return language.alpha2

    def _code_to_language(self, code: typing.Union[str, typing.Any]) -> Language:
        language_code = str(code).lower()
        if language_code in {"zh-cn", "zh-hans"}:
            return Language("zho")
        elif language_code == "zh-tw":
            return Language("och")
        return Language(language_code)

    def __str__(self) -> str:
        return "Microsoft Translate"
