from translatepy.language import Language
from translatepy.translators.base import BaseTranslator
from translatepy.utils.annotations import Tuple
from translatepy.utils.request import Request


class LibreTranslate(BaseTranslator):
    """
    translatepy's implementation of LibreTranslate
    """

    def __init__(self, request: Request = Request()):
        self.session = request

    def _translate(self, text: str, destination_language: str, source_language: str) -> Tuple[str, str]:
        """
        This is the translating endpoint

        Must return a tuple with (detected_language, result)
        """
        if source_language == "auto":
            source_language = self._language(text)
        response = self.session.post("https://libretranslate.com/translate", data={"q": str(text), "source": str(source_language), "target": str(destination_language)}, headers={"Origin": "https://libretranslate.com", "Host": "libretranslate.com", "Referer": "https://libretranslate.com/"})
        return source_language, response.json()["translatedText"]

    def _language(self, text: str) -> str:
        """
        This is the language detection endpoint

        Must return a string with the language code
        """
        response = self.session.post("https://libretranslate.com/detect", data={"q": str(text)}, headers={"Origin": "https://libretranslate.com", "Host": "libretranslate.com", "Referer": "https://libretranslate.com/"})
        return response.json()[0]["language"]

    def _language_normalize(self, language: Language) -> str:
        """
        This is the language validation function
        It receives a "translatepy.language.Language" object and returns the correct language code

        Must return a string with the correct language code
        """
        return language.alpha2

    def _language_denormalize(self, language_code: str) -> Language:
        """
        This is the language denormalization function
        It receives a string with the translator language code and returns a "translatepy.language.Language" object

        Must return a string with the correct language code
        """
        return Language(language_code)

    def __str__(self) -> str:
        """
        This is optional but you can use it if you want to change the way the class is represented as a string.

        It defaults (if not defined) to:
        ... class_name = self.__class__.__name__.split("Translate")[0]
        ... return "Unknown" if class_name == "" else class_name
        """
        return "Libre"
