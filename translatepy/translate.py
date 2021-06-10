"""
translatepy v2.0.0 (Alpha)

© Anime no Sekai — 2021
"""

from translatepy.translators import BaseTranslator, GoogleTranslate, BingTranslate, YandexTranslate, ReversoTranslate, DeeplTranslate
from translatepy.models import TranslationResult, TransliterationResult, SpellcheckResult, LanguageResult
from translatepy.utils.annotations import List
from translatepy.utils.request import Request
from translatepy.exceptions import UnsupportedMethod


class Translate():
    """
    A class which groups all of the APIs
    """

    def __init__(
        self,
        services_list: List[BaseTranslator] = [
            YandexTranslate,
            GoogleTranslate,
            BingTranslate,
            ReversoTranslate,
            DeeplTranslate,
        ],
        request: Request = Request()
    ) -> None:

        if not isinstance(services_list, List):
            raise TypeError("Parameter 'services_list' must be a list, {} was given".format(type(services_list).__name__))

        if not services_list:
            raise ValueError("Parameter 'services_list' must not be empty")

        self.services = []
        for service in services_list:
            if not isinstance(service, type):
                raise ValueError("Type of the parameter 'services_list' must be a class")

            if not issubclass(service, BaseTranslator):
                raise TypeError("Type of the parameter 'services_list' must be a child class of BaseTranslator class")

            self.services.append(service(request=request))

    def translate(self, text: str, destination_language: str, source_language: str = "auto") -> TranslationResult:
        """
        Translates the given text to the given language

        i.e Good morning (en) --> おはようございます (ja)
        """

        for service in self.services:
            try:
                result = service.translate(
                    text, destination_language, source_language)
            except Exception:
                continue
            else:
                return result
        else:
            raise ValueError("No service has returned the correct result")

    def transliterate(self, text: str, destination_language: str = "en", source_language: str = "auto") -> TransliterationResult:
        """
        Transliterates the given text

        i.e おはよう --> Ohayou
        """
        for service in self.services:
            try:
                result = service.transliterate(text, destination_language, source_language)
            except Exception:
                continue
            else:
                return result
        else:
            raise ValueError("No service has returned the correct result")

    def spellcheck(self, text: str, source_language: str = "auto") -> SpellcheckResult:
        """
        Checks the spelling of a given text

        i.e God morning --> Good morning
        """

        for service in self.services:
            try:
                result = service.spellcheck(text, source_language)
            except Exception:
                continue
            else:
                return result
        else:
            raise ValueError("No service has returned the correct result")

    def language(self, text: str) -> LanguageResult:
        """
        Returns the language of the given text

        i.e 皆さんおはようございます！ --> Japanese
        """

        for service in self.services:
            try:
                response = service.language(text)
            except Exception:
                continue
            else:
                return response
        else:
            raise ValueError("No service has returned the correct result")

    def example(self, text: str, destination_language: str, source_language: str = "auto") -> str:
        """
        Returns a set of examples / use cases for the given word

        i.e Hello --> ['Hello friends how are you?', 'Hello im back again.']
        """

        for service in self.services:
            try:
                response = service.example(text, destination_language, source_language)
            except Exception:
                continue
            else:
                return response
        else:
            raise ValueError("No service has returned the correct result")

    def dictionary(self, text: str, destination_language: str, source_language="auto") -> str:
        """
        Returns a list of translations that are classified between two categories: featured and less common

        i.e Hello --> {'featured': ['ハロー', 'こんにちは'], 'less_common': ['hello', '今日は', 'どうも', 'こんにちわ', 'こにちは', 'ほいほい', 'おーい', 'アンニョンハセヨ', 'アニョハセヨ'}
        """

        for service in self.services:
            try:
                response = service.dictionary(text, destination_language, source_language)
            except Exception:
                continue
            else:
                return response
        else:
            raise ValueError("No service has returned the correct result")

    def text_to_speech(self, text: str, source_language: str = "auto") -> bytes:
        """
        Gives back the text to speech result for the given text

        Args:
          text: the given text
          source_language: the source language (Defaut value = None)

        Returns:
            the mp3 file as bytes

        Example:
            >>> from translatepy import Translator
            >>> t = Translator()
            >>> result = t.text_to_speech("Hello, how are you?", "English")
            >>> with open("output.mp3", "wb") as output: # open a binary (b) file to write (w)
            ...     output.write(result)
            ... print("Output of Text to Speech is available in output.mp3!")

            # the result is an MP3 file with the text to speech output
        """

        # TODO: Implement
        raise UnsupportedMethod("")

        for service in self.services:
            try:
                response = service.text_to_speech(text, source_language)
            except Exception:
                continue
            else:
                return response
        else:
            raise ValueError("No service has returned the correct result")
