from translatepy.language import Language
from translatepy.translators.base import BaseTranslator
from translatepy.exceptions import UnsupportedMethod
from translatepy.utils.request import Request


class ReversoTranslate(BaseTranslator):
    """
    A Python implementation of Reverso's API
    """
    def __init__(self, request: Request = Request()):
        self.session = request

    def _translate(self, text: str, destination_language: str, source_language: str) -> str:
        if source_language == "auto":
            source_language = self._language(text)

        request = self.session.post("https://api.reverso.net/translate/v1/translation", json={
            "input": text,
            "from": source_language,
            "to": destination_language,
            "format": "text",
            "options": {
                "origin": "reversodesktop",
                "sentenceSplitter": False,
                "contextResults": False,
                "languageDetection": True
            }
        })
        response = request.json()
        if request.status_code < 400:
            try:
                _detected_language = response["languageDetection"]["detectedLanguage"]
            except Exception:
                _detected_language = source_language
            return _detected_language, response["translation"][0]

    def _transliterate(self, text: str, destination_language: str, source_language: str) -> str:
        raise UnsupportedMethod("Reverso Translate doesn't support this method")

    def _spellcheck(self, text: str, source_language: str) -> str:
        if source_language == "auto":
            source_language = self._language(text)

        request = self.session.post("https://orthographe.reverso.net/api/v1/Spelling", json={
            "text": text,
            "language": source_language,
            "autoReplace": True,
            "interfaceLanguage": "en",
            "locale": "Indifferent",
            "origin": "interactive",
            "generateSynonyms": False,
            "generateRecommendations": False,
            "getCorrectionDetails": False
        })
        response = request.json()
        if request.status_code < 400:
            return source_language, response.get("text", text)

    def _language(self, text: str) -> str:
        request = self.session.post("https://api.reverso.net/translate/v1/translation", json={
            "input": text,
            "from": "eng",
            "to": "fra",
            "format": "text",
            "options": {
                "origin": "reversodesktop",
                "sentenceSplitter": False,
                "contextResults": False,
                "languageDetection": True
            }
        })
        response = request.json()
        if request.status_code < 400:
            return response["languageDetection"]["detectedLanguage"]

    def _example(self, text: str, destination_language: str, source_language: str):
        # TODO: nrows value

        destination_language = Language(destination_language).alpha2
        source_language = Language(source_language).alpha2

        if source_language == "auto":
            source_language = self._language(text)

        url = "https://context.reverso.net/bst-query-service"
        params = {"source_text": text, "source_lang": source_language, "target_lang": destination_language, "npage": 1, "nrows": 20, "expr_sug": 0, "json": 1, "dym_apply": True, "pos_reorder": 5}
        request = self.session.get(url, params=params)
        response = request.json()

        if request.status_code < 400:
            return source_language, response["list"]

    def _dictionary(self, text: str, destination_language: str, source_language: str):
        destination_language = Language(destination_language).alpha2
        source_language = Language(source_language).alpha2

        if source_language == "auto":
            source_language = self._language(text)

        url = "https://context.reverso.net/bst-query-service"
        params = {"source_text": text, "source_lang": source_language, "target_lang": destination_language, "npage": 1, "nrows": 20, "expr_sug": 0, "json": 1, "dym_apply": True, "pos_reorder": 5}
        request = self.session.get(url, params=params)
        response = request.json()

        if request.status_code < 400:
            _result = []
            for _dictionary in response["dictionary_entry_list"]:
                _result.append(_dictionary["term"])
            return source_language, _result

    def _text_to_speech(self, text: str, source_language: str):
        # TODO: Implement
        raise UnsupportedMethod("Reverso Translate doesn't support this method")

    def _language_normalize(self, language) -> str:
        _normalized_language_code = language.alpha3

        if _normalized_language_code == "fre":
            return "fra"
        else:
            return _normalized_language_code

    def __repr__(self) -> str:
        return "Reverso Translate"
