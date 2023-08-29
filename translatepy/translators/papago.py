"""
translatepy's implementation of <Papago>
"""
import typing
import hmac
import base64
import uuid
import time

from translatepy.__info__ import __translatepy_dir__
from translatepy import exceptions, models
from translatepy.language import Language
from translatepy.translators.base import (BaseTranslateException,
                                          BaseTranslator, C)
from translatepy.utils import request
import cain.types

class PapagoException(BaseTranslateException):
    error_codes = {
        429: "Too many requests"  # add your own status codes and error
    }

    # you can use it like so in your endpoint:
    # raise TranslateNameException(request.status_code)


class PapagoSessionData(cain.types.Object):
    """Bing session data holder"""
    timestamp: cain.types.UInt64
    cookies_keys: typing.List[str]
    cookies_values: typing.List[str]


SESSION_CACHE_EXPIRATION = 3600


class Papago(BaseTranslator):
    """
    translatepy's implementation of <Papago>
    """

    _supported_languages = {
        "auto",  # automatic, not officially supported but will be detected by `Papago.language`
        "ja",  # japanese
        "es",  # spanish
        "ru",  # russian
        "vi",  # vietnamese
        "hi",  # hindi
        "ko",  # korean
        "zh-CN",  # chinese (simplified)
        "fr",  # french
        "pt",  # portuguese
        "th",  # thai
        "en",  # english
        "zh-TW",  # chinese (traditional)
        "de",  # german
        "it",  # italian
        "id",  # indonesian
    }

    def __init__(self, session: typing.Optional[request.Session] = None, *args, **kwargs):
        super().__init__(session, *args, **kwargs)
        self._auth_session_file = __translatepy_dir__ / "sessions" / "papago.cain"
        try:
            with self._auth_session_file.open("rb") as file:
                _auth_session_data = cain.load(file, PapagoSessionData)
                if time.time() - _auth_session_data.timestamp > SESSION_CACHE_EXPIRATION:
                    raise ValueError("The session cache expired")
                self.cookies = {key: _auth_session_data.cookies_values[index] for index, key in enumerate(_auth_session_data.cookies_keys)}
        except Exception:
            self.cookies = self.session.get("https://papago.naver.com").cookies
            self._auth_session_file.parent.mkdir(parents=True, exist_ok=True)
            try:
                with self._auth_session_file.open("wb") as file:
                    cain.dump({
                        "timestamp": int(time.time()),
                        "cookies_keys": list(self.cookies.keys()),
                        "cookies_values": list(self.cookies.values())
                    }, file, PapagoSessionData)
            except Exception:
                pass

    def generate_headers(self, url: str, request_id: str):
        """Generates the headers for the API"""
        # https://papago.naver.com/main.5fbfac62f1cf0b8694fe.chunk.js#8345:8350
        # var t = Object(E.a)(),
        #     n = (new Date).getTime() + a - d;
        # return {
        #     Authorization: "PPG " + t + ":" + p.a.HmacMD5(t + "\n" + e.split("?")[0] + "\n" + n, "v1.7.7_5cf6891a07").toString(p.a.enc.Base64),
        #     Timestamp: n
        # }

        # Then we gotta generate a new timestamp
        # n = datetime.datetime.now().timestamp() * 1000 + a - d

        # normally we should add some alpha but this doesn't seem to have that much of a difference
        timestamp = int(time.time() * 1000)  # in milliseconds

        # The Authorization token is
        # PPG + request_id + : + hmac_md5(request_id + \n + the_api_url_without_params + \n + the_timestamp, "v1.7.7_5cf6891a07").encode("base64")

        def encrypt(string: str, key: str) -> str:
            """Encrypts the given value for the Papago API"""
            key_encoded = str(key).encode("utf-8")
            string_encoded = str(string).encode("utf-8")
            encrypted = hmac.new(key_encoded, string_encoded, 'MD5')
            return base64.b64encode(encrypted.digest()).decode("utf-8")

        processed_url = str(url).split("?")[0]
        data = f"{request_id}\n{processed_url}\n{timestamp}"

        return {
            "Host": "papago.naver.com",
            "Origin": "https://papago.naver.com",
            "Referer": "https://papago.naver.com/",
            "device-type": "pc",
            "Authorization": f"PPG {request_id}:{encrypt(data, 'v1.7.7_5cf6891a07')}",
            "Timestamp": str(timestamp)
        }

    def _translate(self: C, text: str, dest_lang: typing.Any, source_lang: typing.Any, *args, **kwargs) -> models.TranslationResult[C]:
        if source_lang == "auto":
            source_lang = self._language_to_code(self.language(text).source_lang)
        # First we gotta get the device UUID
        request_id = uuid.uuid4()
        req = self.session.post("https://papago.naver.com/apis/n2mt/translate", headers=self.generate_headers("https://papago.naver.com/apis/n2mt/translate", request_id), data={
            "deviceId": str(request_id),  # TODO
            "locale": "en",
            "dict": "false",
            "dictDisplay": 30,
            "honorific": "true",
            "instant": "false",
            "paging": "false",
            "source": source_lang,
            "target": dest_lang,
            "text": text
        }, cookies=self.cookies)
        data = req.json()
        return models.TranslationResult(
            source_lang=source_lang,
            raw=data,
            dest_lang=dest_lang,
            translation=data["translatedText"]
        )

    def _alternatives(self: C, translation: models.TranslationResult, *args, **kwargs) -> typing.Union[models.TranslationResult[C], typing.List[models.TranslationResult[C]]]:
        return super()._alternatives(translation, *args, **kwargs)

    def _transliterate(self: C, text: str, dest_lang: typing.Any, source_lang: typing.Any, *args, **kwargs) -> models.TransliterationResult[C]:
        translation = self.translate(text, dest_lang=dest_lang, source_lang=source_lang)
        return models.TransliterationResult(
            source_lang=translation.source_lang,
            raw=translation.raw,
            transliteration=translation.raw["tlit"]["message"]["tlitResult"][0]["token"]
        )

    def _language(self: C, text: str, *args, **kwargs) -> models.LanguageResult[C]:
        # First we gotta get the device UUID
        request_id = uuid.uuid4()
        req = self.session.post("https://papago.naver.com/apis/langs/dect", headers=self.generate_headers("https://papago.naver.com/apis/langs/dect", request_id), data={
            "query": text
        }, cookies=self.cookies)
        data = req.json()
        return models.LanguageResult(
            source_lang=data["langCode"],
            raw=data
        )

    def _example(self: C, text: str, source_lang: typing.Any, *args, **kwargs) -> typing.Union[models.ExampleResult[C], typing.List[models.ExampleResult[C]]]:
        translation = self.translate(text, dest_lang="en", source_lang=source_lang)
        results = []
        ref = translation.raw["dict"]["items"][0]["source"]
        for pos in translation.raw["dict"]["items"][0]["pos"]:
            for meaning in pos["meanings"]:
                for example in meaning["examples"]:
                    results.append(models.ExampleResult(
                        source_lang=translation.source_lang,
                        raw=translation.raw,
                        example=example["text"],
                        reference=ref
                    ))
        return results

    def _text_to_speech(self: C, text: str, speed: int, gender: models.Gender, source_lang: typing.Any, *args, **kwargs) -> models.TextToSpeechResult[C]:
        # TODO
        # Check the different voices for each language
        # Male ? "jose" : "carmen"
        # Male ? "shinji" : "yuri"
        # Male ? "aleksei" : "vera"
        # Male ? "jinho" : "kyuri"
        # Male ? "liangliang" : "meimei"
        # Male ? "louis" : "roxane"
        # Male ? "sarawut" : "somsi"
        # Male ? "matt" : "clara"
        # Male ? "kuanlin" : "chiahua"
        # Male ? "tim" : "lena"

        males = {
            "ja": "shinji",
            "es": "jose",
            "ru": "aleksei",
            "ko": "jinho",
            "zh-CN": "liangliang",
            "fr": "louis",
            "th": "sarawut",
            "en": "matt",
            "zh-TW": "kuanlin",
            "de": "tim"
        }
        females = {
            "ja": "yuri",
            "es": "carmen",
            "ru": "vera",
            "ko": "kyuri",
            "zh-CN": "meimei",
            "fr": "roxane",
            "th": "somsi",
            "en": "clara",
            "zh-TW": "chiahua",
            "de": "lena"
        }

        if source_lang == "auto":
            source_lang = self._language_to_code(self.language(text).source_lang)

        if source_lang in {"vi", "hi", "pt", "it", "id"}:
            raise exceptions.UnsupportedLanguage()

        request_id = str(uuid.uuid4())

        req = self.session.post("https://papago.naver.com/apis/tts/makeID", data={
            "alpha": 0,
            "pitch": 0,
            "speaker": (males if gender is models.Gender.MALE else females)[source_lang],
            "speed": 0,
            "text": text
        }, headers=self.generate_headers("https://papago.naver.com/apis/tts/makeID", request_id), cookies=self.cookies)
        data = req.json()
        tts_req = self.session.get(f"https://papago.naver.com/apis/tts/{data['id']}")
        return models.TextToSpeechResult(
            source_lang=source_lang,
            raw=data,
            result=tts_req.content
        )

    def _code_to_language(self, code: typing.Union[str, typing.Any], *args, **kwargs) -> Language:
        language_code = str(code).lower()
        if language_code == "zh-cn":
            return Language("zho")
        elif language_code == "zh-tw":
            return Language("och")
        return Language(code)

    def _language_to_code(self, language: Language, *args, **kwargs) -> typing.Union[str, typing.Any]:
        if language.id == "zho":
            return "zh-CN"
        if language.id == "och":
            return "zh-TW"
        return language.alpha2
