"""
Module containing various models for holding informations.
"""
from json import dumps
from translatepy.language import Language


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
        return "TranslationResult(service={service}, source={source}, source_language={source_language}, destination_language={destination_language}, result={result})".format(
            service=self.service,
            source=self.source,
            source_language=self.source_language,
            destination_language=self.destination_language,
            result=self.result
        )

    def as_json(self, **kwargs) -> str:
        return dumps({
            "service": str(self.service),
            "source": str(self.source),
            "source_language": str((self.source_language.alpha2) if isinstance(self.source_language, Language) else self.source_language),
            "destination_language": str((self.destination_language.alpha2) if isinstance(self.destination_language, Language) else self.destination_language),
            "result": str(self.result),
        }, **kwargs)


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
        return "TransliterationResult(service={service}, source={source}, source_language={source_language}, destination_language={destination_language}, result={result})".format(
            service=self.service,
            source=self.source,
            source_language=self.source_language,
            destination_language=self.destination_language,
            result=self.result
        )

    def as_json(self, **kwargs) -> str:
        return dumps({
            "service": str(self.service),
            "source": str(self.source),
            "source_language": str((self.source_language.alpha2) if isinstance(self.source_language, Language) else self.source_language),
            "destination_language": str((self.destination_language.alpha2) if isinstance(self.destination_language, Language) else self.destination_language),
            "result": str(self.result),
        }, **kwargs)


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
        return "SpellcheckResult(service={service}, source={source}, source_language={source_language}, result={result})".format(
            service=self.service,
            source=self.source,
            source_language=self.source_language,
            result=self.result
        )

    def as_json(self, **kwargs) -> str:
        return dumps({
            "service": str(self.service),
            "source": str(self.source),
            "source_language": str((self.source_language.alpha2) if isinstance(self.source_language, Language) else self.source_language),
            "result": str(self.result),
        }, **kwargs)


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
        return "LanguageResult(service={service}, source={source}, result={result})".format(
            service=self.service,
            source=self.source,
            result=self.result
        )

    def as_json(self, **kwargs) -> str:
        return dumps({
            "service": str(self.service),
            "source": str(self.source),
            "result": str(self.result),
        }, **kwargs)

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
        return "ExampleResult(service={service}, source={source}, source_language={source_language}, destination_language={destination_language}, result={result})".format(
            service=self.service,
            source=self.source,
            source_language=self.source_language,
            destination_language=self.destination_language,
            result=self.result
        )

    def as_json(self, **kwargs) -> str:
        return dumps({
            "service": str(self.service),
            "source": str(self.source),
            "source_language": str((self.source_language.alpha2) if isinstance(self.source_language, Language) else self.source_language),
            "destination_language": str((self.destination_language.alpha2) if isinstance(self.destination_language, Language) else self.destination_language),
            "result": str(self.result),
        }, **kwargs)


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

    def as_json(self, **kwargs) -> str:
        return dumps({
            "service": str(self.service),
            "source": str(self.source),
            "source_language": str((self.source_language.alpha2) if isinstance(self.source_language, Language) else self.source_language),
            "destination_language": str((self.destination_language.alpha2) if isinstance(self.destination_language, Language) else self.destination_language),
            "result": str(self.result),
        }, **kwargs)


class TextToSpechResult:
    """
    Class that holds the result of a text to spech.
    """

    def __init__(self, service, source, source_language, speed, gender, result):
        self.service = service
        self.source = source
        self.source_language = source_language
        self.speed = speed,
        self.gender = gender
        self.result = result

    def write_to_file(self, file):
        """
        Writes the spoken text to an MP3 file.

        Args:
            file: The output file
        """

        if isinstance(file, str):
            with open(file, "wb") as fp:
                fp.write(self.result)
            return

        if hasattr(file, "write"):
            file.write(self.result)
            return

    def __str__(self) -> str:
        return self.result

    def __repr__(self) -> str:
        return str(self.__dict__)
