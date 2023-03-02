from translatepy.translators.new_base import *


class Test(BaseTranslator):
    """
    Testing some stuff
    """

    def _translate(self: C, text: str, dest_lang: typing.Any, source_lang: typing.Any) -> models.TranslationResult[C]:
        return models.TranslationResult(translation="Hello", source_lang=Language("English"))
