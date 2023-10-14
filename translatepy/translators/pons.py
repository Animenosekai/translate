
"""
translatepy's implementation of <PONS>
"""
import typing
import uuid

from translatepy import exceptions, models
from translatepy.language import Language
from translatepy.translators.base import (BaseTranslateException,
                                          BaseTranslator, C)
from translatepy.utils import request


class PONSException(BaseTranslateException):
    error_codes = {
        429: "Too many requests"  # add your own status codes and error
    }

    # you can use it like so in your endpoint:
    # raise TranslateNameException(request.status_code)


class PONS(BaseTranslator):
    """
    translatepy's implementation of <PONS>
    """

    _supported_languages = {'auto', 'ar', 'bg', 'ca', 'cs', 'da', 'de', 'el', 'en', 'es', 'et', 'fa', 'fi', 'fr', 'he', 'hr', 'ht', 'hu', 'id', 'it', 'ja',
                            'ko', 'lt', 'lv', 'nb', 'nl', 'pl', 'pt-br', 'pt-pt', 'ro', 'ru', 'sk', 'sl', 'sr', 'sv', 'th', 'tr', 'uk', 'vi', 'zh-cn', 'zh-tw'}

    _base_url = "https://api.pons.com/text-translation-web/v4/{endpoint}"

    def __init__(self, session: typing.Optional[request.Session] = None, *args, **kwargs):
        super().__init__(session, *args, **kwargs)
        self.impression_id = str(uuid.uuid4())  # if really checked, we might need to request the webpage

    def _translate(self: C, text: str, dest_lang: typing.Any, source_lang: typing.Any, *args, **kwargs) -> models.TranslationResult[C]:
        json_data = {"impressionId": self.impression_id,
                     "text": text,
                     "targetLanguage": dest_lang}
        if source_lang != "auto":
            json_data["sourceLanguage"] = source_lang
        request = self.session.post(self._base_url.format(endpoint="translate"),
                                    params={"locale": "en"},
                                    json=json_data)
        request.raise_for_status()
        data = request.json()
        return models.TranslationResult(raw=data, source_lang=data["sourceLanguage"], translation=data["text"])

    def _alternatives(self: C, translation: models.TranslationResult, *args, **kwargs) -> typing.Union[models.TranslationResult[C], typing.List[models.TranslationResult[C]]]:
        request = self.session.post(self._base_url.format(endpoint="alternatives"),
                                    params={"locale": "en"},
                                    json={"impressionId": self.impression_id,
                                          "text": translation.translation,
                                          "sourceLanguage": self._language_to_code(translation.source_lang),
                                          "targetLanguage": self._language_to_code(translation.dest_lang),
                                          "targetPrefix": ""})
        request.raise_for_status()
        data = request.json()
        return [models.TranslationResult(translation=translation["text"], raw=data) for translation in data["alternatives"]]

    # def _transliterate(self: C, text: str, dest_lang: typing.Any, source_lang: typing.Any, *args, **kwargs) -> models.TransliterationResult[C]:
    #     return super()._transliterate(text, dest_lang, source_lang, *args, **kwargs)

    # def _spellcheck(self: C, text: str, source_lang: typing.Any, *args, **kwargs) -> typing.Union[models.SpellcheckResult[C], models.RichSpellcheckResult[C]]:
    #     return super()._spellcheck(text, source_lang, *args, **kwargs)

    def _language(self: C, text: str, *args, **kwargs) -> models.LanguageResult[C]:
        request = self.session.post(self._base_url.format(endpoint="detect"),
                                    params={"locale": "en"},
                                    json={"impressionId": self.impression_id,
                                          "text": text,
                                          "hint": "en"})
        request.raise_for_status()
        data = request.json()
        return models.LanguageResult(raw=data, language=data["language"])

    # def _example(self: C, text: str, source_lang: typing.Any, *args, **kwargs) -> typing.Union[models.ExampleResult[C], typing.List[models.ExampleResult[C]]]:
    #     return super()._example(text, source_lang, *args, **kwargs)

    # TODO: Implement this

    # def _dictionary(self: C, text: str, source_lang: typing.Any, *args, **kwargs) -> typing.Union[typing.Union[models.DictionaryResult[C], models.RichDictionaryResult[C]], typing.List[typing.Union[models.DictionaryResult[C], models.RichDictionaryResult[C]]]]:
    #     return super()._dictionary(text, source_lang, *args, **kwargs)

    # MAYBE ?
    # def _text_to_speech(self: C, text: str, speed: int, gender: models.Gender, source_lang: typing.Any, *args, **kwargs) -> models.TextToSpeechResult[C]:
    #     return super()._text_to_speech(text, speed, gender, source_lang)

    def _language_to_code(self, language: Language) -> typing.Union[str, typing.Any]:
        if language.id == "por":
            return "pt-pt"
        if language.id == "zho":
            return "zh-cn"
        elif language.id == "och":
            return "zh-tw"
        return language.alpha2

    def _code_to_language(self, code: typing.Union[str, typing.Any]) -> Language:
        language_code = str(code).lower()
        if language_code == "pt-pt":
            return Language("por")
        elif language_code == "zh-cn":
            return Language("zho")
        elif language_code == "zh-tw":
            return Language("och")
        return Language(language_code)

    def __str__(self) -> str:
        return "PONS"
