"""
This implementation was made specifically for translatepy by 'Zhymabek Roman'.
"""
import base64
import json
import hashlib
import uuid
import urllib
import hmac
import datetime as dt

from urllib.parse import urlencode, urlparse, urlunparse

from translatepy.language import Language
from translatepy import models
from translatepy.translators.base import BaseTranslateException, BaseTranslator
from translatepy.utils.request import Request



class MicrosoftTranslateV1(BaseTranslator):
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

    def _translate(self, text, dest_lang, source_lang):
        translate_url = f"{self._api_endpoint}/translate"
        translate_params = {"api-version": self._api_version, "to": dest_lang}

        if source_lang != "auto":
            translate_params.update({"from": source_lang})

        encoded_params = urlencode(translate_params)
        parsed_url = urlparse(translate_url)

        final_translate_url = urlunparse((parsed_url.scheme, parsed_url.netloc, parsed_url.path, parsed_url.params, encoded_params, parsed_url.fragment))

        request = self.session.post(f"https://{final_translate_url}", headers={"X-MT-Signature": self._get_signature(final_translate_url)}, json=[{"text": text}])
        response = request.json()

        if source_lang == "auto":
            source_lang = response[0]["detectedLanguage"]["language"]

        return models.TranslationResult(dest_lang=dest_lang, source_lang=source_lang, translation=response[0]["translations"][0]["text"], raw=response)

    def _get_signature(self, url: str):
        guid = uuid.uuid4().hex
        escaped_url = urllib.parse.quote_plus(url)

        now = dt.datetime.utcnow()
        date_str = now.strftime("%a, %d %b %Y %H:%M:%SGMT")

        data_to_sign = f"MSTranslatorAndroidApp{escaped_url}{date_str}{guid}".lower().encode('utf-8')

        hash_bytes = hmac.new(self._api_private_key, data_to_sign, hashlib.sha256).digest()
        signature = f"MSTranslatorAndroidApp::{base64.b64encode(hash_bytes).decode()}::{date_str}::{guid}"
        return signature

    def _language_to_code(self, code):
        language = Language(code)
        if language.id == "zho":
            return "zh-Hans"
        elif language.id == "och":
            return "zh-Hant"
        return language.alpha2

    def _code_to_language(self, code):
        language_code = str(code).lower()
        if language_code in {"zh-cn", "zh-hans"}:
            return Language("zho")
        elif language_code == "zh-tw":
            return Language("och")
        return Language(language_code)


class MicrosoftTranslateV2(BaseTranslator):
    """
    A Python implementation of Microsoft Translation, reverse engenered from Microsoft SwiftKey by ZhymabekRoman

    Also I found '/v1/languages?scope=translation' endpoint, idk maybe it can be useful
    """

    _supported_languages = {'auto', 'af', 'sq', 'am', 'ar', 'hy', 'as', 'az', 'bn', 'bs', 'bg', 'my', 'ca', 'ca', 'zh-Hans', 'cs', 'da', 'nl', 'nl', 'en', 'et', 'fj', 'fil', 'fil', 'fi', 'fr', 'fr-ca', 'de', 'ga', 'el', 'gu', 'ht', 'ht', 'he', 'hi', 'hr', 'hu', 'is', 'iu', 'id', 'it', 'ja', 'kn', 'kk', 'km', 'ko', 'ku', 'lo', 'lv', 'lt', 'ml', 'mi', 'mr', 'ms', 'mg', 'mt', 'ne', 'nb', 'nb', 'or', 'pa', 'pa', 'fa', 'pl', 'pt', 'ps', 'ps', 'ro', 'ro', 'ro', 'ru', 'sk', 'sl', 'sm', 'es', 'es', 'sr-Cyrl', 'sw', 'sv', 'ty', 'ta', 'te', 'th', 'ti', 'tlh-Latn', 'tlh-Latn', 'to', 'tr', 'uk', 'ur', 'vi', 'cy', 'zh-Hans', 'zh-Hant', 'yue', 'prs', 'mww', 'tlh-Piqd', 'kmr', 'pt-pt', 'otq', 'sr-Cyrl', 'sr-Latn', 'yua'}

    def __init__(self, session = None, *args, **kwargs):
        super().__init__(session, *args, **kwargs)
        self.session.headers["Authorization"] = "Bearer 16318c3a-5fb1-4091-8f63-65aa993e2f1d"

    def _translate(self, text: str, dest_lang: str, source_lang: str) -> str:
        if source_lang == "auto":
            source_lang = self._language(text).source_lang

        request = self.session.post("https://translate.api.swiftkey.com/v1/translate", params={'from': source_lang, 'to': dest_lang}, json=[{"text": text}])
        response = request.json()
        return models.TranslationResult(dest_lang=dest_lang, source_lang=source_lang, translation=response[0]["translations"][0]["text"], raw=response)

    def _language(self, text: str) -> str:
        request = self.session.post("https://translate.api.swiftkey.com/v1/translate", params={'to': "en"}, json=[{"text": text}])
        response = request.json()
        return models.LanguageResult(source_lang=response[0]["detectedLanguage"]["language"], raw=response)

    def _language_to_code(self, code):
        language = Language(code)
        if language.id == "zho":
            return "zh-Hans"
        elif language.id == "och":
            return "zh-Hant"
        return language.alpha2

    def _code_to_language(self, code):
        language_code = str(code).lower()
        if language_code in {"zh-cn", "zh-hans"}:
            return Language("zho")
        elif language_code == "zh-tw":
            return Language("och")
        return Language(language_code)

    def __str__(self) -> str:
        return "Microsoft Translate V2"


class MicrosoftTranslateV3(BaseTranslator):
    # Other methods: https://learn.microsoft.com/ru-ru/dotnet/api/microsoft.crm.unifiedservicedesk.dynamics.microsofttranslationservice.languageservice?view=dynamics-usd-3#methods
    _supported_languages = {'auto', 'af', 'sq', 'am', 'ar', 'hy', 'as', 'az', 'bn', 'bs', 'bg', 'my', 'ca', 'ca', 'zh-Hans', 'cs', 'da', 'nl', 'nl', 'en', 'et', 'fj', 'fil', 'fil', 'fi', 'fr', 'fr-ca', 'de', 'ga', 'el', 'gu', 'ht', 'ht', 'he', 'hi', 'hr', 'hu', 'is', 'iu', 'id', 'it', 'ja', 'kn', 'kk', 'km', 'ko', 'ku', 'lo', 'lv', 'lt', 'ml', 'mi', 'mr', 'ms', 'mg', 'mt', 'ne', 'nb', 'nb', 'or', 'pa', 'pa', 'fa', 'pl', 'pt', 'ps', 'ps', 'ro', 'ro', 'ro', 'ru', 'sk', 'sl', 'sm', 'es', 'es', 'sr-Cyrl', 'sw', 'sv', 'ty', 'ta', 'te', 'th', 'ti', 'tlh-Latn', 'tlh-Latn', 'to', 'tr', 'uk', 'ur', 'vi', 'cy', 'zh-Hans', 'zh-Hant', 'yue', 'prs', 'mww', 'tlh-Piqd', 'kmr', 'pt-pt', 'otq', 'sr-Cyrl', 'sr-Latn', 'yua'}
    _app_id_list = ["TAgiBjv8rXgUxIhcK7TTXGPrFSsjhAWfqypS5SRKQxl4*", "B97A24C0E08728B33D41E853C50D405E50E46563", "3DAEE5B978BA031557E739EE1E2A68CB1FAD5909"]

    def _translate(self, text, dest_lang, source_lang):
      for app_id in self._app_id_list:
        text_array = json.dumps([text])
        url = "https://api.microsofttranslator.com/v2/ajax.svc/TranslateArray"
        params = {
            "appId": app_id,
            "texts": text_array,
            "from": source_lang,
            "to": dest_lang,
        }
        requests = self.session.get(url, params=params)

        if requests.status_code != 200:
            # logger.warning(f"Possible not valid app_id: {app_id}")
            continue

        requests.encoding = 'utf-8-sig'

        try:
            response = requests.json()
            translation = response[0]["TranslatedText"]
        except Exception as ex:
            translation = None
            # logger.warning(f"Possible not valid app_id: {app_id}. Exception: {ex}")
            continue

        return models.TranslationResult(dest_lang=dest_lang, source_lang=source_lang, translation=translation, raw=response)
      else:
          raise ValueError("No valid app_id")

    def _text_to_speech(self, text, speed, gender, source_lang):
        params = {
            'word': text,
            'lang': source_lang,
        }

        requests = self.session.get('https://www.translatedict.com/speak.php', params=params)
        return models.TextToSpeechResult(result=requests.content)

    def _language_to_code(self, code):
        language = Language(code)
        if language.id == "zho":
            return "zh-Hans"
        elif language.id == "auto":
            return ""
        elif language.id == "och":
            return "zh-Hant"
        return language.alpha2

    def _code_to_language(self, code):
        language_code = str(code).lower()
        if language_code == "":
            return Language("auto")
        elif language_code in {"zh-cn", "zh-hans"}:
            return Language("zho")
        elif language_code == "zh-tw":
            return Language("och")
        return Language(language_code)

    def __str__(self) -> str:
        return "Microsoft Translate V3"

# TODO: workaround
MicrosoftTranslate = MicrosoftTranslateV3
