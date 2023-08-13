"""
MyMemory

translatepy's implementation of MyMemory
"""
import typing

from translatepy import models
from translatepy.language import Language
from translatepy.translators.base import (BaseTranslateException,
                                          BaseTranslator, C)
from translatepy.utils import request
from translatepy.utils.request import Request


class MyMemoryException(BaseTranslateException):
    error_codes = {
        "NO_MATCH": "There is no match to the translation"
    }


class MyMemoryTranslate(BaseTranslator):
    """
    translatepy's implementation of MyMemory
    """
    base_url = "https://api.mymemory.translated.net/get"

    def __init__(self, session: typing.Optional[request.Session] = None):
        super().__init__(session)

    def _translate(self: C, text: str, dest_lang: typing.Any, source_lang: typing.Any) -> models.TranslationResult[C]:
        request = self.session.get(self.base_url, params={"q": text, "langpair": source_lang + "|" + dest_lang})
        request.raise_for_status()
        try:
            data = request.json()["matches"][0]
            result = data["matches"][0]
        except IndexError:
            raise MyMemoryException("NO_MATCH")

        try:
            _detected_language = result["source"].split("-")[0]
        except Exception:
            _detected_language = source_lang

        return models.TranslationResult(source_lang=_detected_language, translation=result["translation"], raw=data)

    def _language(self: C, text: str) -> models.LanguageResult[C]:
        request = self.session.get(self.base_url, params={"q": text, "langpair": "autodetect|en"})
        request.raise_for_status()
        data = request.json()
        return models.LanguageResult(language=data["matches"][0]["source"], raw=data)

    def _language_to_code(self, language: Language) -> typing.Union[str, typing.Any]:
        if language.id == "auto":
            return "autodetect"
        return language.alpha2

    def _code_to_language(self, code: typing.Union[str, typing.Any]) -> Language:
        language_code = str(code).split("-")[0]
        if language_code == "autodetect":
            return Language("auto")
        # this should work without checking
        # elif str(language_code).lower() == "zh":
        #     return Language("zho")
        return Language(language_code)

    def __str__(self) -> str:
        return "MyMemory"
