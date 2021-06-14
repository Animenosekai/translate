from translatepy.exceptions import UnsupportedMethod
from translatepy.language import Language
from translatepy.utils.request import Request
from translatepy.translators.base import BaseTranslator

class MyMemoryTranslate(BaseTranslator):
    """
    translatepy's implementation of MyMemory
    """

    def __init__(self, request: Request):
        self.session = request
        self.base_url = "https://api.mymemory.translated.net/get"

    def _translate(self, text: str, destination_language: str, source_language: str) -> str:
        """
        This is the translating endpoint

        Must return a tuple with (detected_language, result)
        """
        request = self.session.get(self.base_url, params={"q": text, "langpair": source_language + "|" + destination_language})
        if request.status_code < 400:
            result = request.json()["matches"][0]
            try:
                _detected_language = result["source"].split("-")[0]
            except Exception:
                _detected_language = source_language
            return _detected_language, result["translation"]

    def _transliterate(self, text, destination_language, source_language):
        raise UnsupportedMethod()

    def _language(self, text: str) -> str:
        """
        This is the language detection endpoint

        Must return a string with the language code
        """
        # You could use `self.session` to make a request to the endpoint, with all of the parameters
        request = self.session.get(self.base_url, params={"q": text, "langpair": "autodetect|en"})
        request.raise_for_status()
        result = request.json()["matches"][0]
        return result["source"]


    def _supported_languages(self):
        raise UnsupportedMethod()

    def _spellcheck(self, text, source_language):
        raise UnsupportedMethod()

    def _example(self, text, destination_language, source_language):
        raise UnsupportedMethod()

    def _dictionary(self, text, destination_language, source_language):
        raise UnsupportedMethod()

    def _text_to_speech(self, text, speed, gender, source_language):
        raise UnsupportedMethod()


    def _language_normalize(self, language: Language) -> str:
        """
        This is the language validation function
        It receives a "translatepy.language.Language" object and returns the correct language code

        Must return a string with the correct language code
        """
        if language.language.alpha2 == "auto":
            return "autodetect"
        return language.language.alpha2

    def _language_denormalize(self, language_code) -> str:
        """
        This is the language denormalization function
        It receives a string with the translator language code and returns a "translatepy.language.Language" object

        Must return a string with the correct language code
        """
        language_code = str(language_code).split("-")[0]
        if language_code == "autodetect":
            return Language("Automatic")
        return Language(language_code)
