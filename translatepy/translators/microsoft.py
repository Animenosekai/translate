"""
This implementation was made specifically for translatepy by 'Zhymabek Roman'.
"""
from icecream import ic

import base64
import hashlib
import os
import uuid
import urllib
import hmac
import time
import datetime as dt
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

class MicrosoftTranslateV2(BaseTranslator):
    """
    A Python implementation of Microsoft Translation, reverse engenered from Microsoft Translator Android application.
    Ported from https://github.com/d4n3436/GTranslate/blob/master/src/GTranslate/Translators/MicrosoftTranslator.cs
    Huge thanks to d4n3436.
    """

    _api_endpoint = "dev.microsofttranslator-int.com"
    _api_version = "3.0"
    _api_private_key = bytes([
        0xa2, 0x29, 0x3a, 0x3d, 0xd0, 0xdd, 0x32, 0x73,
        0x97, 0x7a, 0x64, 0xdb, 0xc2, 0xf3, 0x27, 0xf5,
        0xd7, 0xbf, 0x87, 0xd9, 0x45, 0x9d, 0xf0, 0x5a,
        0x09, 0x66, 0xc6, 0x30, 0xc6, 0x6a, 0xaa, 0x84,
        0x9a, 0x41, 0xaa, 0x94, 0x3a, 0xa8, 0xd5, 0x1a,
        0x6e, 0x4d, 0xaa, 0xc9, 0xa3, 0x70, 0x12, 0x35,
        0xc7, 0xeb, 0x12, 0xf6, 0xe8, 0x23, 0x07, 0x9e,
        0x47, 0x10, 0x95, 0x91, 0x88, 0x55, 0xd8, 0x17
    ])

    def __init__(self, request: Request = Request()):
        self.session = request

    def _translate(self, text, destination_language, source_language):
        translate_url = f"{self._api_endpoint}/translate?api-version={self._api_version}&to={destination_language}"
        ic(translate_url)
        if source_language != "auto":
            translate_url += "&from={source_language}"

        request = self.session.post(f"https://{translate_url}", headers={"X-MT-Signature": self._get_signature(translate_url)}, json=[{"text": text}])
        response = request.json()
        ic(response)
        return response

    def _get_signature(self, url):
        guid = uuid.uuid4().hex
        escaped_url = urllib.parse.quote(url, safe='')

        now = dt.datetime.utcnow()
        date_str = now.strftime("%a, %d %b %Y %H:%M:%S GMT").lower()

        data_to_sign = f"MSTranslatorAndroidApp{escaped_url}{date_str}{guid}".lower().encode('utf-8')

        hash_bytes = hmac.new(self._api_private_key, data_to_sign, hashlib.sha256).digest()
        signature = f"MSTranslatorAndroidApp::{base64.b64encode(hash_bytes).decode()}::{date_str}::{guid}"
        ic(signature)
        print(signature)
        return signature

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


class MicrosoftTranslateV1(BaseTranslator):
    """
    A Python implementation of Microsoft Translation, reverse engenered from Microsoft SwiftKey

    Also I found '/v1/languages?scope=translation' endpoint, idk maybe it can be useful
    """

    _supported_languages = {'auto', 'af', 'sq', 'am', 'ar', 'hy', 'as', 'az', 'bn', 'bs', 'bg', 'my', 'ca', 'ca', 'zh-Hans', 'cs', 'da', 'nl', 'nl', 'en', 'et', 'fj', 'fil', 'fil', 'fi', 'fr', 'fr-ca', 'de', 'ga', 'el', 'gu', 'ht', 'ht', 'he', 'hi', 'hr', 'hu', 'is', 'iu', 'id', 'it', 'ja', 'kn', 'kk', 'km', 'ko', 'ku', 'lo', 'lv', 'lt', 'ml', 'mi', 'mr', 'ms', 'mg', 'mt', 'ne', 'nb', 'nb', 'or', 'pa', 'pa', 'fa', 'pl', 'pt', 'ps', 'ps', 'ro', 'ro', 'ro', 'ru', 'sk', 'sl', 'sm', 'es', 'es', 'sr-Cyrl', 'sw', 'sv', 'ty', 'ta', 'te', 'th', 'ti', 'tlh-Latn', 'tlh-Latn', 'to', 'tr', 'uk', 'ur', 'vi', 'cy', 'zh-Hans', 'zh-Hant', 'yue', 'prs', 'mww', 'tlh-Piqd', 'kmr', 'pt-pt', 'otq', 'sr-Cyrl', 'sr-Latn', 'yua'}

    def __init__(self, request: Request = Request()):
        self.session = request
        self.session.headers["Authorization"] = "Bearer 16318c3a-5fb1-4091-8f63-65aa993e2f1d"
        self._update_trace_id()

    def _update_trace_id(self):
        self.session.headers["X-ClientTraceId"] = str(uuid.uuid4())

    def _translate(self, text: str, destination_language: str, source_language: str) -> str:
        if source_language == "auto":
            source_language = self._language(text)

        request = self.session.post("https://translate.api.swiftkey.com/v1/translate", params={'from': source_language, 'to': destination_language}, json=[{"text": text}])
        response = request.json()
        self._update_trace_id()
        return source_language, response[0]["translations"][0]["text"]

    def _language(self, text: str) -> str:
        request = self.session.post("https://translate.api.swiftkey.com/v1/translate", params={'to': "en"}, json=[{"text": text}])
        response = request.json()
        self._update_trace_id()
        return response[0]["detectedLanguage"]["language"]

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
        return "Microsoft Translate V1"

MicrosoftTranslate = MicrosoftTranslateV1
