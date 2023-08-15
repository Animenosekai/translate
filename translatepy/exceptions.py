from nasse.exceptions import NasseException


class TranslatepyException(NasseException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class VersionNotSupported(TranslatepyException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class NoResult(TranslatepyException, ValueError):  # ValueError is needed for backward compatibility
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class ParameterError(TranslatepyException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class ParameterTypeError(ParameterError, TypeError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class ParameterValueError(ParameterError, ValueError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class TranslationError(TranslatepyException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class UnknownLanguage(TranslatepyException):
    def __init__(self, guessed_language, similarity, *args: object) -> None:
        super().__init__(*args)
        self.guessed_language = str(guessed_language)
        self.similarity = similarity


class UnknownTranslator(TranslatepyException):
    def __init__(self, guessed_translator, similarity, *args: object) -> None:
        super().__init__(*args)
        self.guessed_translator = str(guessed_translator)
        self.similarity = similarity


class UnsupportedMethod(TranslatepyException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class UnsupportedLanguage(TranslatepyException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class RequestStatusError(TranslatepyException):
    def __init__(self, status_code, *args: object) -> None:
        super().__init__(*args)
        self.status_code = int(status_code)


class ServiceURLError(TranslatepyException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class RateLimitPrevention(TranslatepyException):
    STATUS_CODE = 500
    MESSAGE = "The server made too many requests to another server"
    EXCEPTION_NAME = "RATE_LIMIT_PREVENTION"
