class TranslationError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class UnknownLanguage(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)