"""
translatepy v1.6.1 (Stable)

© Anime no Sekai — 2021
"""

from typing import Union
from translatepy.models.languages import Language
from translatepy.translators.google import GoogleTranslate
from translatepy.translators.bing import BingTranslate
from translatepy.translators.yandex import YandexTranslate
from translatepy.translators.reverso import ReversoTranslate
from translatepy.translators.deepl import DeepL
from translatepy.translators.unselected import Unselected

from translatepy.utils.annotations import List, Dict

TRANSLATION_CACHES = {}
TRANSLITERATION_CACHES = {}
SPELLCHECK_CACHES = {}
LANGUAGE_CACHES = {}
EXAMPLE_CACHES = {}
DICTIONARY_CACHES = {}
AUTOMATIC = Language("auto")

class TranslationResult():
    """
    The result for a translation
    """
    def __init__(self, source, result, source_language, destination_language, service) -> None:
        self.source = str(source)
        self.result = str(result)
        self.source_language = source_language
        self.destination_language = destination_language
        self.service = service

    def __repr__(self) -> str:
        return "Source (" + (self.source_language.name if isinstance(self.source_language, Language) else str(self.source_language)) + "): " + self.source + "\nResult (" + (self.destination_language.name if isinstance(self.destination_language, Language) else str(self.destination_language)) + "): " + self.result

    def __str__(self) -> str:
        return self.result

    def __call__(self, *args, **kwds):
        return self.result

    def __eq__(self, o: object) -> bool:
        return str(o) == self.result

    def __ne__(self, o: object) -> bool:
        return str(o) != self.result


class Translator():
    """
    A class which groups all of the APIs
    """
    def __init__(self, use_google=True, use_yandex=True, use_bing=True, use_reverso=True, use_deepl=True) -> None:
        self.google_translate = (GoogleTranslate() if use_google else Unselected())
        self.yandex_translate = (YandexTranslate() if use_yandex else Unselected())
        self.bing_translate = (BingTranslate() if use_bing else Unselected())
        self.reverso_translate = (ReversoTranslate() if use_reverso else Unselected())
        self.deepl_translate = (DeepL() if use_deepl else Unselected())

    def translate(self, text, destination_language, source_language=None) -> Union[TranslationResult, None]:
        """
        Translates the given text to the given language

        i.e Good morning (en) --> おはようございます (ja)
        """
        global TRANSLATION_CACHES

        if str(text).replace(" ", "").replace("\n", "") == "":
            return None

        ## language handling
        if not isinstance(destination_language, Language):
            destination_language = Language(destination_language)
        if source_language is not None and not isinstance(source_language, Language):
            source_language = Language(source_language)

        ## caches handling
        _cache_key = str({"t": str(text), "d": str(destination_language), "s": str(source_language)})
        if _cache_key in TRANSLATION_CACHES:
            return TRANSLATION_CACHES[_cache_key]

        services = [self.google_translate, self.bing_translate, self.deepl_translate, self.reverso_translate, self.yandex_translate]
        for service in services:
            if not isinstance(service, Unselected):
                lang, response = service.translate(text, destination_language, source_language)
                if response is not None:
                    try:
                        lang = Language(lang)
                    except Exception: pass
                    result = TranslationResult(source=text, result=response, source_language=lang, destination_language=destination_language, service=self.reverso_translate)
                    TRANSLATION_CACHES[str({"t": str(text), "d": str(destination_language), "s": str(source_language)})] = result
                    TRANSLATION_CACHES[str({"t": str(text), "d": str(destination_language), "s": str(lang)})] = result
                    return result
        return None

    def transliterate(self, text, source_language=None) -> Union[str, None]:
        """
        Transliterates the given text

        i.e おはよう --> Ohayou
        """
        global TRANSLITERATION_CACHES


        if str(text).replace(" ", "").replace("\n", "") == "":
            return None

        ## language handling
        if source_language is not None and not isinstance(source_language, Language):
            source_language = Language(source_language)

        _cache_key = str({"t": str(text), "s": str(source_language)})
        if _cache_key in TRANSLITERATION_CACHES:
            return TRANSLITERATION_CACHES[_cache_key]

        services = [self.google_translate, self.yandex_translate]
        for service in services:
            if not isinstance(service, Unselected):
                lang, response = service.transliterate(text, source_language)
                if response is not None:
                    try:
                        lang = Language(lang)
                    except Exception: pass

                    TRANSLITERATION_CACHES[str({"t": str(text), "s": str(source_language)})] = response
                    TRANSLITERATION_CACHES[str({"t": str(text), "s": str(lang)})] = response
        return None

    def spellcheck(self, text, source_language=None) -> Union[str, None]:
        """
        Checks the spelling of a given text

        i.e God morning --> Good morning
        """
        global SPELLCHECK_CACHES


        if str(text).replace(" ", "").replace("\n", "") == "":
            return None

        ## language handling
        if source_language is not None and not isinstance(source_language, Language):
            source_language = Language(source_language)

        _cache_key = str({"t": str(text), "s": str(source_language)})
        if _cache_key in SPELLCHECK_CACHES:
            return SPELLCHECK_CACHES[_cache_key]

        services = [self.bing_translate, self.reverso_translate, self.yandex_translate]
        for service in services:
            if not isinstance(service, Unselected):
                lang, response = service.spellcheck(text, source_language)
                if response is not None:
                    try:
                        lang = Language(lang)
                    except Exception: pass

                    SPELLCHECK_CACHES[str({"t": str(text), "s": str(source_language)})] = response
                    SPELLCHECK_CACHES[str({"t": str(text), "s": str(lang)})] = response
                    return response
        return None

    def language(self, text) -> Union[Language, str, None]:
        """
        Returns the language of the given text

        i.e 皆さんおはようございます！ --> Japanese
        """
        global LANGUAGE_CACHES


        if str(text).replace(" ", "").replace("\n", "") == "":
            return None

        text = str(text)
        if text in LANGUAGE_CACHES:
            return LANGUAGE_CACHES[text]

        services = [self.google_translate, self.bing_translate, self.deepl_translate, self.reverso_translate, self.yandex_translate]
        for service in services:
            if not isinstance(service, Unselected):
                response = service.language(text)
                if response is not None:
                    try:
                        response = Language(response)
                    except Exception: pass

                    LANGUAGE_CACHES[text] = response
                    return response
        return None

    def example(self, text, destination_language=None, source_language=None) -> Union[List, None]:
        """
        Returns a set of examples / use cases for the given word

        i.e Hello --> ['Hello friends how are you?', 'Hello im back again.']
        """
        global EXAMPLE_CACHES

        if str(text).replace(" ", "").replace("\n", "") == "":
            return None

        if destination_language is None:
            destination_language = "Japanese"  # could be anything

        ## language handling
        if not isinstance(destination_language, Language):
            destination_language = Language(destination_language)
        if source_language is not None and not isinstance(source_language, Language):
            source_language = Language(source_language)

        ## caches handling
        _cache_key = str({"t": str(text), "d": str(destination_language), "s": str(source_language)})
        if _cache_key in EXAMPLE_CACHES:
            return EXAMPLE_CACHES[_cache_key]

        lang, response = self.bing_translate.example(text, destination_language, source_language)
        if response is None and isinstance(self.bing_translate, Unselected):
            return None

        try:
            lang = Language(lang)
        except Exception: pass
        EXAMPLE_CACHES[str({"t": str(text), "d": str(destination_language), "s": str(source_language)})] = response
        EXAMPLE_CACHES[str({"t": str(text), "d": str(destination_language), "s": str(lang)})] = response
        return response

    def dictionary(self, text, destination_language, source_language=None) -> Union[Dict[str, Union[str, List[str]]], None]:
        """
        Returns a list of translations that are classified between two categories: featured and less common

        i.e Hello --> {'featured': ['ハロー', 'こんにちは'], 'less_common': ['hello', '今日は', 'どうも', 'こんにちわ', 'こにちは', 'ほいほい', 'おーい', 'アンニョンハセヨ', 'アニョハセヨ'}

        _html and _response are also provided if you want to parse the HTML response (by DeepL/Linguee) by yourself
        """
        global DICTIONARY_CACHES

        if str(text).replace(" ", "").replace("\n", "") == "":
            return None

        ## language handling
        if not isinstance(destination_language, Language):
            destination_language = Language(destination_language)
        if source_language is not None and not isinstance(source_language, Language):
            source_language = Language(source_language)

        ## caches handling
        _cache_key = str({"t": str(text), "d": str(destination_language), "s": str(source_language)})
        if _cache_key in DICTIONARY_CACHES:
            return DICTIONARY_CACHES[_cache_key]

        lang, response = self.deepl_translate.dictionary(text, destination_language, source_language)
        if response is None and isinstance(self.deepl_translate, Unselected):
            return None
        try:
            lang = Language(lang)
        except Exception: pass
        DICTIONARY_CACHES[str({"t": str(text), "d": str(destination_language), "s": str(source_language)})] = response
        DICTIONARY_CACHES[str({"t": str(text), "d": str(destination_language), "s": str(lang)})] = response
        return response

    def text_to_speech(self, text, source_language=None) -> Union[bytes, None]:
        """
        Gives back the text to speech result for the given text

        Args:
          text: the given text
          source_language: the source language (Defaut value = None)

        Returns:
            bytes --> the mp3 file as bytes
            None --> when an error occurs

        Example:
            >>> from translatepy import Translator
            >>> t = Translator()
            >>> result = t.text_to_speech("Hello, how are you?", "English")
            >>> if result is not None:
            ...     with open("output.mp3", "wb") as output: # open a binary (b) file to write (w)
            ...         output.write(result)
            ...     print("Output of Text to Speech is available in output.mp3!")
            ... else:
            ...     print("Couldn't get text to speech result...")

            # the result is an MP3 file with the text to speech output
        """

        if str(text).replace(" ", "").replace("\n", "") == "":
            return None

        ## language handling
        if source_language is not None and not isinstance(source_language, Language):
            source_language = Language(source_language)

        return self.google_translate.text_to_speech(text, source_language)

    def clean_cache(self) -> None:
        """
        Cleans translatepy's global caches

        Returns:
            None
        """
        global TRANSLATION_CACHES
        global TRANSLITERATION_CACHES
        global SPELLCHECK_CACHES
        global LANGUAGE_CACHES
        global EXAMPLE_CACHES
        global DICTIONARY_CACHES

        TRANSLATION_CACHES = {}
        TRANSLITERATION_CACHES = {}
        SPELLCHECK_CACHES = {}
        LANGUAGE_CACHES = {}
        EXAMPLE_CACHES = {}
        DICTIONARY_CACHES = {}

#translator = Translator()
