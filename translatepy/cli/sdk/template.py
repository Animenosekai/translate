"""Keeps code templates"""

TRANSLATOR_TEMPLATE = '''\
"""
translatepy's implementation of <TranslatorName>
"""
import typing

from translatepy import exceptions, models
from translatepy.language import Language
from translatepy.translators.base import (BaseTranslateException,
                                          BaseTranslator, C)
from translatepy.utils import request

class TranslatorNameException(BaseTranslateException):
    error_codes = {
        429: "Too many requests" # add your own status codes and error
    }

    # you can use it like so in your endpoint:
    # raise TranslateNameException(request.status_code)

class TranslatorName(BaseTranslator):
    """
    translatepy's implementation of <TranslatorName>
    """

    _supported_languages = {"set", "of", "supported", "language", "code", "eng", "fra", "jpa"}

    def __init__(self, session: typing.Optional[request.Session] = None, *args, **kwargs):
        super().__init__(session, *args, **kwargs)

    def _translate(self: C, text: str, dest_lang: typing.Any, source_lang: typing.Any, *args, **kwargs) -> models.TranslationResult[C]:
        return super()._translate(text, dest_lang, source_lang, *args, **kwargs)

    def _alternatives(self: C, translation: models.TranslationResult, *args, **kwargs) -> typing.Union[models.TranslationResult[C], typing.List[models.TranslationResult[C]]]:
        return super()._alternatives(translation, *args, **kwargs)

    def _transliterate(self: C, text: str, dest_lang: typing.Any, source_lang: typing.Any, *args, **kwargs) -> models.TransliterationResult[C]:
        return super()._transliterate(text, dest_lang, source_lang, *args, **kwargs)

    def _spellcheck(self: C, text: str, source_lang: typing.Any, *args, **kwargs) -> typing.Union[models.SpellcheckResult[C], models.RichSpellcheckResult[C]]:
        return super()._spellcheck(text, source_lang, *args, **kwargs)

    def _language(self: C, text: str, *args, **kwargs) -> models.LanguageResult[C]:
        return super()._language(text, *args, **kwargs)

    def _example(self: C, text: str, source_lang: typing.Any, *args, **kwargs) -> typing.Union[models.ExampleResult[C], typing.List[models.ExampleResult[C]]]:
        return super()._example(text, source_lang, *args, **kwargs)

    def _dictionary(self: C, text: str, source_lang: typing.Any, *args, **kwargs) -> typing.Union[typing.Union[models.DictionaryResult[C], models.RichDictionaryResult[C]], typing.List[typing.Union[models.DictionaryResult[C], models.RichDictionaryResult[C]]]]:
        return super()._dictionary(text, source_lang, *args, **kwargs)

    def _text_to_speech(self: C, text: str, speed: int, gender: models.Gender, source_lang: typing.Any, *args, **kwargs) -> models.TextToSpechResult[C]:
        return super()._text_to_speech(text, speed, gender, source_lang)

    def _code_to_language(self, code: typing.Union[str, typing.Any], *args, **kwargs) -> Language:
        return super()._code_to_language(code, *args, **kwargs)

    def _language_to_code(self, language: Language, *args, **kwargs) -> typing.Union[str, typing.Any]:
        return super()._language_to_code(language, *args, **kwargs)
'''
