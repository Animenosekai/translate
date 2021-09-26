from translatepy.translators.base import BaseTranslator
from typing import List
from translatepy.exceptions import UnsupportedMethod
from translatepy.translators.bing import BingTranslate
from translatepy.translators.deepl import (DeeplTranslate,
                                           DeeplTranslateException)
from translatepy.translators.google import GoogleTranslateV1, GoogleTranslateV2
from translatepy.translators.mymemory import (MyMemoryException,
                                              MyMemoryTranslate)
from translatepy.translators.reverso import ReversoTranslate
from translatepy.translators.translatecom import TranslateComTranslate
from translatepy.translators.yandex import YandexTranslate
from translatepy.utils.request import Request

IGNORED_EXCEPTIONS = (UnsupportedMethod,)


class TestAllTranslators:
    def setup(self):
        self.services_list: List[BaseTranslator] = [
            GoogleTranslateV1(),
            GoogleTranslateV2(),
            BingTranslate(),
            ReversoTranslate(),
            YandexTranslate(),
            DeeplTranslate(),
            TranslateComTranslate(),
            MyMemoryTranslate()
        ]

    def test_service_translate(self):
        translation_args_list = [("Hello, how are you?", "ja")]

        for service in self.services_list:
            for args in translation_args_list:
                try:
                    result = service.translate(*args)
                    assert result
                except IGNORED_EXCEPTIONS:
                    continue

    def test_service_transliterate(self):
        transliteration_args_list = [("こんにちは?", "en")]

        for service in self.services_list:
            for args in transliteration_args_list:
                try:
                    result = service.transliterate(*args)
                    assert result
                except IGNORED_EXCEPTIONS:
                    continue

    def test_service_spellcheck(self):
        spellcheck_args_list = [("Helo, how are tou?",)]

        for service in self.services_list:
            for args in spellcheck_args_list:
                try:
                    result = service.spellcheck(*args)
                    assert result
                except IGNORED_EXCEPTIONS:
                    continue

    def test_service_example(self):
        example_args_list = [("Hello", "french")]

        for service in self.services_list:
            for args in example_args_list:
                try:
                    result = service.example(*args)
                    assert result
                except IGNORED_EXCEPTIONS:
                    continue

    def test_service_dictionary(self):
        dictionary_args_list = [("Hello", "french")]

        for service in self.services_list:
            for args in dictionary_args_list:
                try:
                    result = service.dictionary(*args)
                    assert result
                except IGNORED_EXCEPTIONS:
                    continue

    def test_service_language(self):
        language_args_list = [("Привет",)]

        for service in self.services_list:
            for args in language_args_list:
                try:
                    result = service.language(*args)
                    assert result
                except IGNORED_EXCEPTIONS:
                    continue

    def test_service_text_to_speech(self):
        texts_args_list = [("自动",)]

        for service in self.services_list:
            for args in texts_args_list:
                try:
                    result = service.text_to_speech(*args)
                    assert result
                except IGNORED_EXCEPTIONS:
                    continue

    def test_service_translate_html(self):
        translation_args_list = [("<h1>Hello</h1> <span class='everyone'>everyone</span><br>I hope that <span class='everyone'>everyone</span><div class='okay-container'> is doing <strong>Okay〜!</strong></div>", "ja")]

        for service in self.services_list:
            for args in translation_args_list:
                try:
                    result = service.translate_html(*args)
                    assert result
                except IGNORED_EXCEPTIONS:
                    continue
