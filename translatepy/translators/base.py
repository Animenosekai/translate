from abc import ABC, abstractmethod

from translatepy.language import Language
from translatepy.models import TranslationResult, TransliterationResult, SpellcheckResult, LanguageResult, ExampleResult, DictionaryResult
from translatepy.utils.lru_cacher import LRUDictCache
from translatepy.utils.annotations import List


class BaseTranslateException(Exception):
    def __init__(self, status_code, message=None):
        if message is None:
            self.message = self.error_codes.get(status_code, "Unknown error. Error code: {}".format(status_code))
        else:
            self.message = message

        self.status_code = status_code

    def __str__(self):
        return "{} | {}".format(self.status_code, self.message)


# TODO: Feat: Implement supported_languages method
# TODO: Feat: Implement text_to_spech method
# TODO: Fix Dictionaries and Examples results. See models file
# TODO: Feat: support translating > 5000 characters (or just excpetion raising)
# TODO: Feat: Some translation services give out a lot of useful information that can come in handy for programmers. We need to implement for example kwargs in the model.py file


class BaseTranslator(ABC):
    """
    Base abstract class for a translate service
    """

    _translations_cache = LRUDictCache()
    _transliterations_cache = LRUDictCache()
    _languages_cache = LRUDictCache()
    _spellchecks_cache = LRUDictCache()
    _examples_cache = LRUDictCache()
    _dictionaries_cache = LRUDictCache()

    def translate(self, text: str, destination_language: str, source_language: str = "auto") -> TranslationResult:
        """
        Translates text from a given language to another specific language.

        Parameters:
        ----------
            text : str
                The text to be translated.
            destination_language : str
                If str it expects the language code that the `text` should be translated to.
                to check the list of languages that a `Translator` supports, and use `.get_language` to
                search for a language of the `Translator`, and find it's code.
            source_language : str
                If str it expects the code of the language that the `text` is written in. When using the default value (`auto`),
                the `Translator` will try to find the language automatically.

        Returns:
        --------
            TranslationResult:
                Translation result.

        """

        # Validate the text
        self._validate_text(text)

        # Validate the languages
        # We save the values in new variables, so at the end
        # of this method, we still have acess to the original codes.
        # With this we can use the original codes to build the response,
        # this makes the code transformation transparent to the user.
        dest_code = self._detect_and_validate_lang(destination_language)
        source_code = self._detect_and_validate_lang(source_language)

        self._validate_language_pair(source_code, dest_code)

        # Build cache key
        _cache_key = str({"t": text, "d": dest_code, "s": source_code})

        if _cache_key in self._translations_cache:
            # Taking the values from the cache
            source_language, translation = self._translations_cache[_cache_key]
        else:
            # Call the private concrete implementation of the Translator to get the translation
            source_language, translation = self._translate(text, dest_code, source_code)

            # Сache the translation values to speed up the translation process in the future
            self._translations_cache[_cache_key] = (source_language, translation)

        # Return a `TranslationResult` object
        return TranslationResult(
            service=str(self),
            source=text,
            source_language=str(source_language),
            destination_language=str(destination_language),
            result=translation,
        )

    @abstractmethod
    def _translate(self, text: str, destination_language: str, source_language: str) -> str:
        """
        Private method that concrete Translators must implement to hold the concrete
        logic for the translations. Receives the validated and normalized parameters and must
        return a translation (str).
        """

    def transliterate(self, text: str, destination_language: str, source_language: str = "auto") -> TransliterationResult:
        """
        Transliterates text from a given language to another specific language.

        Args:
            text: The text to be transliterated.
            destination_language: If str it expects the language code that the `text` should be translated to.
                to check the list of languages that a `Translator` supports, and use `.get_language` to
                search for a language of the `Translator`, and find it's code. Default value = English
            source_language: If str it expects the code of the language that the `text` is written in. When using the default value (`auto`),
                the `Translator` will try to find the language automatically.

        Returns:
            A `TransliterationResult` object with the results of the translation.
        """

        # Validate the text
        self._validate_text(text)

        # Validate the languages
        # We save the values in new variables, so at the end
        # of this method, we still have acess to the original codes.
        # With this we can use the original codes to build the response,
        # this makes the code transformation transparent to the user.
        dest_code = self._detect_and_validate_lang(destination_language)
        source_code = self._detect_and_validate_lang(source_language)

        self._validate_language_pair(source_code, dest_code)

        # Build cache key
        _cache_key = str({"t": text, "d": dest_code, "s": source_code})

        if _cache_key in self._transliterations_cache:
            # Taking the values from the cache
            source_language, transliteration = self._transliterations_cache[_cache_key]
        else:
            # Call the private concrete implementation of the Translator to get the transliteration
            source_language, transliteration = self._transliterate(text, dest_code, source_code)

            # Сache the transliteration values to speed up the translation process in the future
            self._transliterations_cache[_cache_key] = (source_language, transliteration)

        # Return a `TransliterationResult` object
        return TransliterationResult(
            service=str(self),
            source=text,
            source_language=str(source_language),
            destination_language=str(destination_language),
            result=transliteration,
        )

    @abstractmethod
    def _transliterate(self, text: str, destination_language, source_language: str) -> str:
        """
        Private method that concrete Translators must implement to hold the concrete
        logic for the transliteration. Receives the validated and normalized parameters and must
        return a transliteration (str).
        """

    def spellcheck(self, text: str, source_language: str = "auto") -> SpellcheckResult:
        """
        Checks text spelling in a given language.

        Args:
            text: The text to be checks.
            source_language: If str it expects the code of the language that the `text` is written in. When using the default value (`auto`),
                the `Translator` will try to find the language automatically.

        Returns:
            A `SpellcheckResult` object with the results of the corrected text.

        """

        # Validate the text
        self._validate_text(text)

        # Validate the languages
        # We save the values in new variables, so at the end
        # of this method, we still have acess to the original codes.
        # With this we can use the original codes to build the response,
        # this makes the code transformation transparent to the user.
        source_code = self._detect_and_validate_lang(source_language)

        # Build cache key
        _cache_key = str({"t": text, "s": source_code})

        if _cache_key in self._spellchecks_cache:
            # Taking the values from the cache
            source_language, spellcheck = self._spellchecks_cache[_cache_key]
        else:
            # Call the private concrete implementation of the Translator to get the spellchecked text
            source_language, spellcheck = self._spellcheck(text, source_code)

            # Сache the spellcheck values to speed up the translation process in the future
            self._spellchecks_cache[_cache_key] = (source_language, spellcheck)

        # Return a `SpellcheckResult` object
        return SpellcheckResult(
            service=str(self),
            source=text,
            source_language=str(source_language),
            result=spellcheck,
        )

    @abstractmethod
    def _spellcheck(self, text: str, source_language: str) -> str:
        """
        Private method that concrete Translators must implement to hold the concrete
        logic for the spellcheck. Receives the validated and normalized parameters and must
        return a spellchecked text (str).
        """

    def language(self, text: str) -> LanguageResult:
        """
        Detect the language of the text

        Args:
            text: The text to be detect the language

        Returns:
            A `LanguageResult` object with the results of the detected language.

        """

        # Validate the text
        self._validate_text(text)

        # Build cache key
        _cache_key = str({"t": text})

        if _cache_key in self._languages_cache:
            # Taking the values from the cache
            language = self._languages_cache[_cache_key]
        else:
            # Call the private concrete implementation of the Translator to get the language
            language = self._language(text)

            # Сache the languages values to speed up the translation process in the future
            self._languages_cache[_cache_key] = language

        denormalized_lang = self._language_denormalize(language)

        # Return a `LanguageResult` object
        return LanguageResult(
            service=str(self),
            source=text,
            result=denormalized_lang,
        )

    @abstractmethod
    def _language(self, text: str) -> str:
        """
        Private method that concrete Translators must implement to hold the concrete
        logic for the language. Receives the validated and normalized parameters and must
        return a language code (str).
        """

    def example(self, text: str, destination_language: str, source_language: str = "auto") -> ExampleResult:
        """
        Returns a set of examples

        Parameters:
        ----------
            text : str
                The text to be translated.
            destination_language : str
                If str it expects the language code that the `text` should be translated to.
                to check the list of languages that a `Translator` supports, and use `.get_language` to
                search for a language of the `Translator`, and find it's code.
            source_language : str
                If str it expects the code of the language that the `text` is written in. When using the default value (`auto`),
                the `Translator` will try to find the language automatically.

        Returns:
        --------
            ExampleResult:
                Examples result.

        """

        # Validate the text
        self._validate_text(text)

        # Validate the languages
        # We save the values in new variables, so at the end
        # of this method, we still have acess to the original codes.
        # With this we can use the original codes to build the response,
        # this makes the code transformation transparent to the user.
        dest_code = self._detect_and_validate_lang(destination_language)
        source_code = self._detect_and_validate_lang(source_language)

        self._validate_language_pair(source_code, dest_code)

        # Build cache key
        _cache_key = str({"t": text, "d": dest_code, "s": source_code})

        if _cache_key in self._examples_cache:
            # Taking the values from the cache
            source_language, example = self._examples_cache[_cache_key]
        else:
            # Call the private concrete implementation of the Translator to get the examples
            source_language, example = self._example(text, dest_code, source_code)

            # Сache the translation values to speed up the translation process in the future
            self._examples_cache[_cache_key] = (source_language, example)

        # Return a `ExampleResult` object
        return ExampleResult(
            service=str(self),
            source=text,
            source_language=str(source_language),
            destination_language=str(destination_language),
            result=example,
        )

    @abstractmethod
    def _example(self, text: str, destination_language: str, source_language: str) -> List:
        """
        Private method that concrete Translators must implement to hold the concrete
        logic for the translations. Receives the validated and normalized parameters and must
        return a examples list (List).
        """

    def dictionary(self, text: str, destination_language: str, source_language: str = "auto") -> DictionaryResult:
        """
        Returns a list of dictionary results.

        Parameters:
        ----------
            text : str
                The text to be translated.
            destination_language : str
                If str it expects the language code that the `text` should be translated to.
                to check the list of languages that a `Translator` supports, and use `.get_language` to
                search for a language of the `Translator`, and find it's code.
            source_language : str
                If str it expects the code of the language that the `text` is written in. When using the default value (`auto`),
                the `Translator` will try to find the language automatically.

        Returns:
        --------
            DictionaryResult:
                Dictionary result.

        """

        # Validate the text
        self._validate_text(text)

        # Validate the languages
        # We save the values in new variables, so at the end
        # of this method, we still have acess to the original codes.
        # With this we can use the original codes to build the response,
        # this makes the code transformation transparent to the user.
        dest_code = self._detect_and_validate_lang(destination_language)
        source_code = self._detect_and_validate_lang(source_language)

        self._validate_language_pair(source_code, dest_code)

        # Build cache key
        _cache_key = str({"t": text, "d": dest_code, "s": source_code})

        if _cache_key in self._dictionaries_cache:
            # Taking the values from the cache
            source_language, dictionary = self._dictionaries_cache[_cache_key]
        else:
            # Call the private concrete implementation of the Translator to get the dictionary result
            source_language, dictionary = self._dictionary(text, dest_code, source_code)

            # Сache the translation values to speed up the translation process in the future
            self._dictionaries_cache[_cache_key] = (source_language, dictionary)

        # Return a `DictionaryResult` object
        return DictionaryResult(
            service=str(self),
            source=text,
            source_language=str(source_language),
            destination_language=str(destination_language),
            result=dictionary,
        )

    @abstractmethod
    def _dictionary(self, text: str, destination_language: str, source_language: str) -> List:
        """
        Private method that concrete Translators must implement to hold the concrete
        logic for the translations. Receives the validated and normalized parameters and must
        return a dictionary result list (List).
        """

    @abstractmethod
    def _language_normalize(self, language) -> str:
        """
        Private method that concrete Translators must implement to hold the concrete
        logic for the translations. Receives the Language instance and must
        return a normalized code language specific of translator (str).
        """

    @abstractmethod
    def _language_denormalize(self, language_code) -> str:
        """
        Private method that concrete Translators must implement to hold the concrete
        logic for the translations. Receives the language code specific of translator and must
        return a Language instance.
        """

    def _detect_and_validate_lang(self, language: str) -> str:
        """
        Validates the language code, and converts the language code into a single format.
        """
        if isinstance(language, Language):
            result = language
        else:
            result = Language(language)

        return self._language_normalize(result)

    def _validate_text(self, text: str) -> None:
        """
        Performs text validation. Checks the text for the correct type,
        and if it is not empty
        """
        if not isinstance(text, str):
            raise TypeError("Parameter 'text' must be a string, {} was given".format(type(text).__name__))

        if text.replace(" ", "").replace("\n", "") == "":
            raise ValueError("Parameter 'text' must not be empty")

    def _validate_language_pair(self, source_language, destination_language):
        """
        Performs language pair validation
        """
        if source_language == destination_language:
            raise ValueError("Parameter source_language cannot be equal to the destination_language parametr")

    def clean_cache(self) -> None:
        """
        Cleans caches

        Returns:
            None
        """
        self._translations_cache.clear()
        self._transliterations_cache.clear()
        self._spellchecks_cache.clear()
        self._languages_cache.clear()
        self._examples_cache.clear()
        self._dictionaries_cache.clear()

    def __str__(self) -> str:
        """
        String representation of a translator.
        """
        class_name = self.__class__.__name__.split("Translate")[0]
        return "Unknown" if class_name == "" else class_name
