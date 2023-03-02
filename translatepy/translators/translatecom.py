import typing

from translatepy import models
from translatepy.language import Language
from translatepy.translators.base import BaseTranslator, C
from translatepy.utils import request


class TranslateComTranslate(BaseTranslator):
    """
    translatepy's implementation of translate.com
    """

    translate_url = "https://www.translate.com/translator/ajax_translate"
    langdetect_url = "https://www.translate.com/translator/ajax_lang_auto_detect"

    def __init__(self, session: typing.Optional[request.Session] = None):
        super().__init__(session)

    def _translate(self: C, text: str, dest_lang: typing.Any, source_lang: typing.Any) -> models.TranslationResult[C]:
        if source_lang == "auto":
            source_lang = self._language_to_code(self.language(text).language)
        request = self.session.post(self.translate_url, data={"text_to_translate": text, "source_lang": source_lang, "translated_lang": dest_lang, "use_cache_only": "false"})
        request.raise_for_status()
        data = request.json()
        return models.TranslationResult(raw=data, source_lang=source_lang, translation=data["translated_text"])

    def _language(self: C, text: str) -> models.LanguageResult[C]:
        # You could use `self.session` to make a request to the endpoint, with all of the parameters
        request = self.session.post(self.langdetect_url, data={"text_to_translate": text})
        request.raise_for_status()
        data = request.json()
        return models.LanguageResult(language=data["language"], raw=data)

    def _language_to_code(self, language: Language) -> typing.Union[str, typing.Any]:
        return language.alpha2

    def _code_to_language(self, code: typing.Union[str, typing.Any]) -> Language:
        if str(code).lower() == "zh-cn":
            return Language("zho")
        return Language(code)

    def __str__(self) -> str:
        return "Translate.com"
