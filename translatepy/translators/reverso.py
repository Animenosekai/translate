import base64

from translatepy.exceptions import UnsupportedMethod
from translatepy.language import Language
from translatepy.translators.base import BaseTranslator
from translatepy.utils.request import Request


class ReversoTranslate(BaseTranslator):
    """
    A Python implementation of Reverso's API
    """

    _supported_languages = {'auto', 'ara', 'chi', 'dut', 'dut', 'eng', 'fra', 'ger', 'heb', 'ita', 'jpn', 'pol', 'por', 'rum', 'rum', 'rum', 'rus', 'spa', 'spa', 'tur'}

    def __init__(self, request: Request = Request()):
        self.session = request

    def _translate(self, text: str, dest_lang: str, source_lang: str) -> str:
        if source_lang == "auto":
            source_lang = self._language(text)

        request = self.session.post(
            "https://api.reverso.net/translate/v1/translation",
            json={
                "input": text,
                "from": source_lang,
                "to": dest_lang,
                "format": "text",
                "options": {
                    "origin": "translation.web",
                    "sentenceSplitter": False,
                    "contextResults": False,
                    "languageDetection": False
                }
            },
            headers={"Content-Type": "application/json; charset=UTF-8"}
        )
        if request.status_code < 400:
            response = request.json()
            try:
                _detected_language = response["languageDetection"]["detectedLanguage"]
            except Exception:
                _detected_language = source_lang
            return _detected_language, response["translation"][0]

    def _spellcheck(self, text: str, source_lang: str) -> str:
        if source_lang == "auto":
            source_lang = self._language(text)

        request = self.session.post(
            "https://orthographe.reverso.net/api/v1/Spelling",
            json={
                "text": text,
                "language": source_lang,
                "autoReplace": True,
                "interfaceLanguage": "en",
                "locale": "Indifferent",
                "origin": "interactive",
                "generateSynonyms": False,
                "generateRecommendations": False,
                "getCorrectionDetails": False
            },
            headers={"Content-Type": "application/json; charset=UTF-8"}
        )
        response = request.json()
        if request.status_code < 400:
            return source_lang, response.get("text", text)

    def _language(self, text: str) -> str:
        request = self.session.post(
            "https://api.reverso.net/translate/v1/translation",
            json={
                "input": text,
                "from": "eng",
                "to": "fra",
                "format": "text",
                "options": {
                    "origin": "translation.web",
                    "sentenceSplitter": False,
                    "contextResults": False,
                    "languageDetection": True
                }
            },
            headers={"Content-Type": "application/json; charset=UTF-8"}
        )
        response = request.json()
        if request.status_code < 400:
            try:
                return response["languageDetection"]["detectedLanguage"]
            except Exception:
                return response["from"]

    def _example(self, text: str, dest_lang: str, source_lang: str):
        # TODO: nrows value

        if source_lang == "auto":
            source_lang = self._language(text)

        dest_lang = Language(dest_lang).alpha2
        source_lang = Language(source_lang).alpha2

        url = "https://context.reverso.net/bst-query-service"
        params = {"source_text": text, "source_lang": source_lang, "target_lang": dest_lang, "npage": 1, "nrows": 20, "expr_sug": 0, "json": 1, "dym_apply": True, "pos_reorder": 5}
        request = self.session.post(url, params=params, headers={"Content-Type": "application/x-www-form-urlencoded"})
        response = request.json()

        if request.status_code < 400:
            return source_lang, response["list"]

    def _dictionary(self, text: str, dest_lang: str, source_lang: str):
        if source_lang == "auto":
            source_lang = self._language(text)

        dest_lang = Language(dest_lang).alpha2
        source_lang = Language(source_lang).alpha2

        url = "https://context.reverso.net/bst-query-service"
        params = {"source_text": text, "source_lang": source_lang, "target_lang": dest_lang, "npage": 1, "nrows": 20, "expr_sug": 0, "json": 1, "dym_apply": True, "pos_reorder": 5}
        request = self.session.post(url, params=params, headers={"Content-Type": "application/x-www-form-urlencoded"})
        response = request.json()

        if request.status_code < 400:
            _result = []
            for _dictionary in response["dictionary_entry_list"]:
                _result.append(_dictionary["term"])
            return source_lang, _result

    def _text_to_speech(self, text, speed, gender, source_lang):
        if source_lang == "auto":
            source_lang = self._language(text)

        _supported_langs_url = "https://voice.reverso.net/RestPronunciation.svc/v1/output=json/GetAvailableVoices"
        _supported_langs_result = self.session.get(_supported_langs_url)
        _supported_langs_list = _supported_langs_result.json()["Voices"]

        _gender = "M" if gender == "male" else "F"
        _text = base64.b64encode(text.encode()).decode()
        _source_language = "US English".lower() if source_lang == "eng" else Language.by_reverso(source_lang).name.lower()

        for _supported_lang in _supported_langs_list:
            if _supported_lang["Language"].lower() == _source_language and _supported_lang["Gender"] == _gender:
                voice = _supported_lang["Name"]
                break
        else:
            raise UnsupportedMethod("{source_lang} language not supported by Reverso".format(source_lang=source_lang))

        url = "https://voice.reverso.net/RestPronunciation.svc/v1/output=json/GetVoiceStream/voiceName={}?voiceSpeed={}&inputText={}".format(voice, speed, _text)
        response = self.session.get(url)
        if response.status_code < 400:
            return source_lang, response.content

    def _language_normalize(self, language: Language) -> str:
        if language.id == "zho":
            return "chi"
        return language.alpha3

    def _language_denormalize(self, language_code):
        if str(language_code).lower() in {"chi", "zh-cn"}:
            return Language("zho")
        return Language(language_code)

    def __str__(self) -> str:
        return "Reverso"
