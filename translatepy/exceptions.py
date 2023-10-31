"""A list of exceptions used throughout translatepy"""
from nasse.exceptions import NasseException


class TranslatepyException(NasseException):
    LOG = False

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class NoResult(TranslatepyException, ValueError):  # ValueError is needed for backward compatibility
    STATUS_CODE = 503
    MESSAGE = "No service returned a valid result"
    EXCEPTION_NAME = "NO_RESULT"

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class ParameterTypeError(TranslatepyException, TypeError):
    STATUS_CODE = 400
    MESSAGE = "The given parameter has a type error"
    EXCEPTION_NAME = "PARAMETER_TYPE_ERROR"

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class UnknownLanguage(TranslatepyException):
    STATUS_CODE = 400
    MESSAGE = "Couldn't recognize the given language"
    EXCEPTION_NAME = "UNKNOWN_LANGUAGE"

    def __init__(self, guessed_language, similarity, *args: object) -> None:
        super().__init__(*args)
        self.guessed_language = str(guessed_language)
        self.similarity = similarity


class UnknownTranslator(TranslatepyException):
    STATUS_CODE = 400
    MESSAGE = "Couldn't recognize the given translator"
    EXCEPTION_NAME = "UNKNOWN_TRANSLATOR"

    def __init__(self, guessed_translator, similarity, *args: object) -> None:
        super().__init__(*args)
        self.guessed_translator = str(guessed_translator)
        self.similarity = similarity


class UnsupportedMethod(TranslatepyException):
    STATUS_CODE = 501
    MESSAGE = "This method is not implemented on the given service"
    EXCEPTION_NAME = "UNSUPPORTED_METHOD"

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class UnsupportedLanguage(TranslatepyException):
    STATUS_CODE = 501
    MESSAGE = "The given language is not supported by the service"
    EXCEPTION_NAME = "UNSUPPORTED_LANGUAGE"

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class ServiceURLError(TranslatepyException):
    STATUS_CODE = 400
    MESSAGE = "You asked for a service URL which is not available for the given service"
    EXCEPTION_NAME = "SERVIER_URL_ERROR"

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class RateLimitPrevention(TranslatepyException):
    STATUS_CODE = 500
    MESSAGE = "The server made too many requests to another server"
    EXCEPTION_NAME = "RATE_LIMIT_PREVENTION"
