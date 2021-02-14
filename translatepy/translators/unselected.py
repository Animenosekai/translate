class Unselected():
    """
    When the user decides not to use the translator
    """
    def __init__(self, *args, **kwargs) -> None:
        pass

    def translate(self, *args, **kwargs):
        return None, None

    def transliterate(self, *args, **kwargs):
        return None, None

    def spellcheck(self, *args, **kwargs):
        return None, None

    def language(self, *args, **kwargs):
        return None

    def example(self, *args, **kwargs):
        return None, None

    def __repr__(self) -> str:
        return "N/A"