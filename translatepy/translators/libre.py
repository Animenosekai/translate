"""
LibreTranslate

translatepy's implementation of LibreTranslate

Copyright
---------
Animenosekai
    Original author
"""

import typing

from translatepy import models
from translatepy.language import Language
from translatepy.translators.base import BaseTranslator, C


class LibreTranslate(BaseTranslator):
    """
    translatepy's implementation of LibreTranslate
    """

    def _translate(self: C, text: str, dest_lang: typing.Any, source_lang: typing.Any) -> models.TranslationResult[C]:
        if source_lang == "auto":
            source_lang = self._language_to_code(self.language(text).language)
        response = self.session.post("https://libretranslate.com/translate", data={"q": str(text), "source": str(source_lang), "target": str(dest_lang)}, headers={"Origin": "https://libretranslate.com", "Host": "libretranslate.com", "Referer": "https://libretranslate.com/"})
        data = response.json()
        return models.TranslationResult(source_lang=source_lang, raw=data, translation=data["translatedText"])

    def _language(self: C, text: str) -> models.LanguageResult[C]:
        response = self.session.post("https://libretranslate.com/detect", data={"q": str(text)}, headers={"Origin": "https://libretranslate.com", "Host": "libretranslate.com", "Referer": "https://libretranslate.com/"})
        data = response.json()
        return models.LanguageResult(raw=data, language=data[0]["language"])

    def _language_to_code(self, language: Language) -> typing.Union[str, typing.Any]:
        return language.alpha2

    def _code_to_language(self, code: typing.Union[str, typing.Any]) -> Language:
        return Language(code)

    def __str__(self) -> str:
        return "Libre Translate"
