"""
This implementation was made specifically for translatepy from 'Zhymabek Roman', based on 'Anime no Sekai' version.
"""

import json
import re
from datetime import datetime, timedelta

from translatepy.exceptions import UnsupportedMethod
from translatepy.language import Language
from translatepy.translators.base import BaseTranslateException, BaseTranslator
from translatepy.utils.request import Request


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
        self.ig = ""
        self.iid = ""
        self.key = ""
        self.token = ""
        self.cookies = None
        try:
            self._parse_authorization_data()
        except Exception:
            pass

    def _parse_authorization_data(self):
        _request = self.session.get("https://www.bing.com/translator")
        _page = _request.text
        _parsed_IG = re.findall('IG:"(.*?)"', _page)
        _parsed_IID = re.findall('data-iid="(.*?)"', _page)
        _parsed_helper_info = re.findall("params_RichTranslateHelper = (.*?);", _page)

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

            if isinstance(response, dict):
                status_code = response.get("statusCode", 200)
            else:
                status_code = request.status_code

            if status_code == 200:
                return response
            elif status_code == 400:
                try:
                    self._parse_authorization_data()
                    continue
                except Exception:
                    raise BingTranslateException(status_code)
            else:
                raise BingTranslateException(status_code)
        raise BingTranslateException(400)


class BingTranslate(BaseTranslator):
    """
    A Python implementation of Microsoft Bing Translation's APIs
    """

    def __init__(self, request: Request = Request()):
        self.session_manager = BingSessionManager(request)
        self.session = request

        self._speech_region = None
        self._speech_token = None
        self._speech_token_expiry = 0

    def _translate(self, text: str, destination_language: str, source_language: str) -> str:
        response = self.session_manager.send("https://www.bing.com/ttranslatev3", data={'text': text, 'fromLang': source_language, 'to': destination_language})
        try:
            _detected_language = response[0]["detectedLanguage"]["language"]
        except Exception:
            _detected_language = source_language
        return _detected_language, response[0]["translations"][0]["text"]

    def _example(self, text, destination_language, source_language, translation=None) -> str:
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
        # NOTE: Alternative Transliteration Implementation. Documentation: https://github.com/MicrosoftDocs/azure-docs/blob/master/articles/cognitive-services/Translator/language-support.md
        # response = self.session_manager.send("https://www.bing.com/ttransliteratev3", data={'text': text, 'language': source_language, 'fromScript': 'Cyrl', 'toScript': 'Latn'})
        # return response

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
        if source_language == "auto-detect":
            source_language = self._language(text)

        if not self._speech_token or datetime.now() > self._speech_token_expiry:
            token_response = self.session_manager.send("https://www.bing.com/tfetspktok", data={})
            # print(token_response)
            token_status = token_response.get("statusCode", 200)

            if token_status != 200:
                raise BingTranslateException(token_status, "Error during token request from the server")

            self._speech_token, self._speech_region = token_response.get("token"), token_response.get("region")
            self._speech_token_expiry = datetime.now() + timedelta(milliseconds=int(token_response.get("expiryDurationInMS", 600000)))

        gender = gender.capitalize()

        _supported_langs_url = "https://{region}.tts.speech.microsoft.com/cognitiveservices/voices/list".format(region=self._speech_region)
        _supported_langs_header = {"authorization": "Bearer {token}".format(token=self._speech_token)}
        _supported_langs_result = self.session.get(_supported_langs_url, headers=_supported_langs_header)
        _supported_langs_list = _supported_langs_result.json()

        # all locals list: {('zh-HK', 'zh-HK'), ('de', 'de-DE'), ('da', 'da-DK'), ('id', 'id-ID'), ('ko', 'ko-KR'), ('en', 'en-NZ'), ('el', 'el-GR'), ('ms', 'ms-MY'), ('es', 'es-AR'), ('ro', 'ro-RO'), ('pl', 'pl-PL'), ('it', 'it-IT'), ('hr', 'hr-HR'), ('pt', 'pt-PT'), ('hu', 'hu-HU'), ('sw', 'sw-KE'), ('en', 'en-GB'), ('mt', 'mt-MT'), ('tr', 'tr-TR'), ('ar', 'ar-EG'), ('fr', 'fr-CA'), ('te', 'te-IN'), ('fr', 'fr-BE'), ('en', 'en-SG'), ('zh-CN', 'zh-CN'), ('fr', 'fr-FR'), ('en', 'en-PH'), ('cs', 'cs-CZ'), ('fi', 'fi-FI'), ('zh-TW', 'zh-TW'), ('de', 'de-CH'), ('nb', 'nb-NO'), ('bg', 'bg-BG'), ('he', 'he-IL'), ('en', 'en-CA'), ('en', 'en-HK'), ('es', 'es-MX'), ('en', 'en-AU'), ('th', 'th-TH'), ('pt', 'pt-BR'), ('mr', 'mr-IN'), ('sk', 'sk-SK'), ('ru', 'ru-RU'), ('nl', 'nl-NL'), ('en', 'en-US'), ('ta', 'ta-IN'), ('hi', 'hi-IN'), ('cy', 'cy-GB'), ('ar', 'ar-SA'), ('ga', 'ga-IE'), ('nl', 'nl-BE'), ('de', 'de-AT'), ('ca', 'ca-ES'), ('uk', 'uk-UA'), ('es', 'es-CO'), ('es', 'es-ES'), ('es', 'es-US'), ('en', 'en-ZA'), ('ur', 'ur-PK'), ('sv', 'sv-SE'), ('lv', 'lv-LV'), ('lt', 'lt-LT'), ('vi', 'vi-VN'), ('et', 'et-EE'), ('en', 'en-IN'), ('en', 'en-IE'), ('ja', 'ja-JP'), ('fr', 'fr-CH'), ('gu', 'gu-IN'), ('sl', 'sl-SI')}
        _locals = {'zh-CN': 'zh-CN', 'mr': 'mr-IN', 'en': 'en-US', 'ru': 'ru-RU', 'el': 'el-GR', 'es': 'es-CO', 'id': 'id-ID', 'pt': 'pt-PT', 'ko': 'ko-KR', 'ta': 'ta-IN', 'te': 'te-IN', 'et': 'et-EE', 'pl': 'pl-PL', 'it': 'it-IT', 'ms': 'ms-MY', 'mt': 'mt-MT', 'ro': 'ro-RO', 'vi': 'vi-VN', 'bg': 'bg-BG', 'zh-TW': 'zh-TW', 'tr': 'tr-TR', 'de': 'de-CH', 'fr': 'fr-CH', 'nb': 'nb-NO', 'nl': 'nl-BE', 'uk': 'uk-UA', 'he': 'he-IL', 'ur': 'ur-PK', 'hi': 'hi-IN', 'ja': 'ja-JP', 'hr': 'hr-HR', 'sv': 'sv-SE', 'hu': 'hu-HU', 'sw': 'sw-KE', 'lt': 'lt-LT', 'sl': 'sl-SI', 'fi': 'fi-FI', 'lv': 'lv-LV', 'sk': 'sk-SK', 'da': 'da-DK', 'cy': 'cy-GB', 'gu': 'gu-IN', 'ga': 'ga-IE', 'th': 'th-TH', 'ar': 'ar-EG', 'ca': 'ca-ES', 'zh-HK': 'zh-HK', 'cs': 'cs-CZ'}
        _source_local = _locals.get(source_language)

        for _supported_lang in _supported_langs_list:
            if _supported_lang["Locale"] == _source_local and _supported_lang["Gender"] == gender:
                voice = _supported_lang["ShortName"]
                break
        else:
            raise UnsupportedMethod("Bing Translate doesn't support {source_lang} language".format(source_lang=source_language))

        speech_url = "https://{region}.tts.speech.microsoft.com/cognitiveservices/v1".format(region=self._speech_region)
        headers = {"authorization": "Bearer {token}".format(token=self._speech_token), "content-type": "application/ssml+xml", "x-microsoft-outputformat": "audio-48khz-192kbitrate-mono-mp3"}
        data = "<speak version='1.0' xml:lang='{local}'><voice xml:lang='{local}' xml:gender='{gender}' name='{voice}'><prosody rate='{speed}%'>{text}</prosody></voice></speak>".format(text=text, gender=gender, speed=float(speed - 100), local=_source_local, voice=voice)
        spech_result = self.session.post(speech_url, data=data.encode('utf-8'), headers=headers)
        return source_language, spech_result.content

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
