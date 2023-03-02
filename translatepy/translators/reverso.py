"""
Reverso

translatepy's implementation of Reverso
"""

import base64
import typing

from translatepy import models
from translatepy.exceptions import UnsupportedMethod
from translatepy.language import Language
from translatepy.translators.base import BaseTranslator, C


class ReversoTranslate(BaseTranslator):
    """
    A Python implementation of Reverso's API
    """

    _supported_languages = {'ara', 'auto', 'chi', 'dut', 'eng', 'fra', 'ger', 'heb', 'ita', 'jpn', 'pol', 'por', 'rum', 'rus', 'spa', 'tur'}

    def _translate(self: C, text: str, dest_lang: typing.Any, source_lang: typing.Any) -> models.TranslationResult[C]:
        if source_lang == "auto":
            source_lang = self._language_to_code(self.language(text).language)

        request = self.session.post(
            "https://api.reverso.net/translate/v1/translation",
            json={
                "input": text,
                "from": source_lang,
                "to": dest_lang,
                "format": "text",
                "options": {
                    "origin": "translation.web",
                    "sentenceSplitter": False,
                    "contextResults": False,
                    "languageDetection": False
                }
            },
            headers={"Content-Type": "application/json; charset=UTF-8"}
        )
        request.raise_for_status()
        response = request.json()
        try:
            # didn't we get it earlier ?
            _detected_language = response["languageDetection"]["detectedLanguage"]
        except Exception:
            _detected_language = source_lang
        return models.TranslationResult(translation=response["translation"][0], source_lang=_detected_language, raw=response)

    def _spellcheck(self: C, text: str, source_lang: typing.Any) -> typing.Union[models.SpellcheckResult[C], models.RichSpellcheckResult[C]]:
        if source_lang == "auto":
            source_lang = self._language_to_code(self.language(text).language)

        request = self.session.post(
            "https://orthographe.reverso.net/api/v1/Spelling",
            json={
                "text": text,
                "language": source_lang,
                "autoReplace": True,
                "interfaceLanguage": "en",
                "locale": "Indifferent",
                "origin": "interactive",
                "generateSynonyms": False,
                "generateRecommendations": False,
                "getCorrectionDetails": False
            },
            headers={"Content-Type": "application/json; charset=UTF-8"}
        )
        request.raise_for_status()
        response = request.json()
        return models.SpellcheckResult(corrected=response.get("text", text), source_lang=source_lang, raw=response)

    def _language(self: C, text: str) -> models.LanguageResult[C]:
        request = self.session.post(
            "https://api.reverso.net/translate/v1/translation",
            json={
                "input": text,
                "from": "eng",
                "to": "fra",
                "format": "text",
                "options": {
                    "origin": "translation.web",
                    "sentenceSplitter": False,
                    "contextResults": False,
                    "languageDetection": True
                }
            },
            headers={"Content-Type": "application/json; charset=UTF-8"}
        )
        request.raise_for_status()
        response = request.json()
        try:
            return models.LanguageResult(language=response["languageDetection"]["detectedLanguage"], raw=response)
        except Exception:
            return models.LanguageResult(language=response["from"], raw=response)

    def _example(self: C, text: str, source_lang: typing.Any) -> typing.Union[models.ExampleResult[C], typing.List[models.ExampleResult[C]]]:
        # TODO: nrows value

        if source_lang == "auto":
            source_lang = self.language(text).language.alpha2
        else:
            source_lang = self._code_to_language(source_lang).alpha2

        url = "https://context.reverso.net/bst-query-service"
        params = {"source_text": text, "source_lang": source_lang, "target_lang": source_lang, "npage": 1, "nrows": 20, "expr_sug": 0, "json": 1, "dym_apply": True, "pos_reorder": 5}
        request = self.session.post(url, params=params, headers={"Content-Type": "application/x-www-form-urlencoded"})
        response = request.json()

        request.raise_for_status()
        return [models.ExampleResult(example=ex) for ex in response["list"]]

    def _dictionary(self: C, text: str, source_lang: typing.Any) -> typing.Union[typing.Union[models.DictionaryResult[C], models.RichDictionaryResult[C]], typing.List[typing.Union[models.DictionaryResult[C], models.RichDictionaryResult[C]]]]:
        raise UnsupportedMethod("Need to reimplement")
        if source_lang == "auto":
            source_lang = self._language(text)

        dest_lang = ""
        dest_lang = Language(dest_lang).alpha2
        source_lang = Language(source_lang).alpha2

        url = "https://context.reverso.net/bst-query-service"
        params = {"source_text": text, "source_lang": source_lang, "target_lang": dest_lang, "npage": 1, "nrows": 20, "expr_sug": 0, "json": 1, "dym_apply": True, "pos_reorder": 5}
        request = self.session.post(url, params=params, headers={"Content-Type": "application/x-www-form-urlencoded"})
        response = request.json()

        if request.status_code < 400:
            _result = []
            for _dictionary in response["dictionary_entry_list"]:
                _result.append(_dictionary["term"])
            return source_lang, _result

    def _text_to_speech(self: C, text: str, speed: int, gender: models.Gender, source_lang: typing.Any) -> models.TextToSpechResult[C]:
        if source_lang == "auto":
            source_lang = self.language(text).language
        else:
            source_lang = self._code_to_language(source_lang)

        _supported_langs_url = "https://voice.reverso.net/RestPronunciation.svc/v1/output=json/GetAvailableVoices"
        _supported_langs_result = self.session.get(_supported_langs_url)
        _supported_langs_list = _supported_langs_result.json()["Voices"]

        if gender is models.Gender.MALE:
            final_gender = "M"
        else:
            final_gender = "F"

        text = base64.b64encode(text.encode()).decode()
        final_source_lang = "US English".lower() if source_lang.id == "eng" else source_lang.name.lower()

        for _supported_lang in _supported_langs_list:
            if _supported_lang["Language"].lower() == final_source_lang and _supported_lang["Gender"] == final_gender:
                voice = _supported_lang["Name"]
                break
        else:
            for _supported_lang in _supported_langs_list:
                if _supported_lang["Language"].lower() == final_source_lang:  # the gender is optional
                    voice = _supported_lang["Name"]
            raise UnsupportedMethod("{source_lang} language not supported by Reverso".format(source_lang=source_lang))

        url = "https://voice.reverso.net/RestPronunciation.svc/v1/output=json/GetVoiceStream/voiceName={}?voiceSpeed={}&inputText={}".format(voice, speed, text)
        response = self.session.get(url)
        response.raise_for_status()
        return models.TextToSpechResult(source_lang=source_lang, result=response.content)

    def _language_to_code(self, language: Language) -> typing.Union[str, typing.Any]:
        if language.id == "zho":
            return "chi"
        return language.alpha3

    def _code_to_language(self, code: typing.Union[str, typing.Any]) -> Language:
        if str(code).lower() in {"chi", "zh-cn"}:
            return Language("zho")
        return Language(code)

    def __str__(self) -> str:
        return "Reverso"
