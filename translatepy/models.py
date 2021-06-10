"""
Module containing various models for holding informations.
"""


class TranslationResult:
    """
    Class that holds the result of a Translation.
    """

    def __init__(self, service, source, source_language, destination_language, result):
        self.service = service
        self.source = source
        self.source_language = source_language
        self.destination_language = destination_language
        self.result = result

    def __str__(self) -> str:
        return self.result

    def __repr__(self) -> str:
        return str(self.__dict__)


class TransliterationResult:
    """
    Class that holds the result of a Transliteration.
    """

    def __init__(self, service, source, source_language, destination_language, result):
        self.service = service
        self.source = source
        self.source_language = source_language
        self.destination_language = destination_language
        self.result = result

    def __str__(self) -> str:
        return self.result

    def __repr__(self) -> str:
        return str(self.__dict__)


class SpellcheckResult:
    """
    Class that holds the result of a Spellchecking.
    """

    def __init__(self, service, source, source_language, result):
        self.service = service
        self.source = source
        self.source_language = source_language
        self.result = result

    def __str__(self) -> str:
        return self.result

    def __repr__(self) -> str:
        return str(self.__dict__)


class LanguageResult:
    """
    Class that holds the result of a Language.
    """

    def __init__(self, service, source, result):
        self.service = service
        self.source = source
        self.result = result

    def __str__(self) -> str:
        return self.result

    def __repr__(self) -> str:
        return str(self.__dict__)


class ExampleResult:
    """
    Class that holds the result of a Example.
    """

    def __init__(self, service, source, source_language, destination_language, result):  # source_result, destination_result):
        self.service = service
        self.source = source
        self.source_language = source_language
        self.destination_language = destination_language
        self.result = result
        # self.source_result = source_result
        # self.destination_result = destination_result

    def __str__(self) -> str:
        # return self.source_result + self.destination_result
        return self.result

    def __repr__(self) -> str:
        return str(self.__dict__)


class DictionaryResult:
    """
    Class that holds the result of a Dictionary.
    """

    def __init__(self, service, source, source_language, destination_language, result):
        self.service = service
        self.source = source
        self.source_language = source_language
        self.destination_language = destination_language
        self.result = result

    def __str__(self) -> str:
        return self.result

    def __repr__(self) -> str:
        return str(self.__dict__)
