from translatepy.translators.google import GoogleTranslateV1, GoogleTranslateV2
from translatepy.translators.bing import BingTranslate
from translatepy.translators.yandex import YandexTranslate
from translatepy.translators.reverso import ReversoTranslate
from translatepy.translators.deepl import DeeplTranslate, DeeplTranslateException
from translatepy.exceptions import UnsupportedMethod
from translatepy import Translator


class TestAllTranslators:
    def setup(self):
        self.services_list = [
            GoogleTranslateV1(),
            GoogleTranslateV2(),
            BingTranslate(),
            ReversoTranslate(),
            YandexTranslate(),
            DeeplTranslate(),
            Translator(),
        ]

    def test_service_translate(self):
        translation_args_list = [["What cool weather today!", "fr"],
                                 ["Hello", "Japanese", "en"],
                                 ["Hello, how are you?", "ja"]]

        for service in self.services_list:
            for args in translation_args_list:
                try:
                    result = service.translate(*args)
                    assert result
                except (UnsupportedMethod, DeeplTranslateException):
                    continue

    def test_service_transliterate(self):
        transliteration_args_list = [["What cool weather today!", "ar"],
                                     ["Hello", "Japanese", "en"],
                                     ["Hello, how are you?", "ja"]]

        for service in self.services_list:
            for args in transliteration_args_list:
                try:
                    result = service.transliterate(*args)
                    assert result
                except (UnsupportedMethod, DeeplTranslateException):
                    continue

    def test_service_spellcheck(self):
        spellcheck_args_list = [["What cool weater todai!"], ["Helo"],
                                ["Helo, how are tou?"]]

        for service in self.services_list:
            for args in spellcheck_args_list:
                try:
                    result = service.spellcheck(*args)
                    assert result
                except (UnsupportedMethod, DeeplTranslateException):
                    continue

    def test_service_example(self):
        example_args_list = [["What cool weater todai!", "fr"], ["Helo", "French"],
                             ["Helo, how are tou?", "ru"]]

        for service in self.services_list:
            for args in example_args_list:
                try:
                    result = service.example(*args)
                    assert result
                except (UnsupportedMethod, DeeplTranslateException):
                    continue

    def test_service_dictionary(self):
        dictionary_args_list = [["What cool weater todai!", "fr"], ["Helo", "French"],
                                ["Helo, how are tou?", "ru"]]

        for service in self.services_list:
            for args in dictionary_args_list:
                try:
                    result = service.dictionary(*args)
                    assert result
                except (UnsupportedMethod, DeeplTranslateException):
                    continue

    def test_service_language(self):
        language_args_list = [["What cool weater todaiy"], ["Привет"],
                              ["自动"]]

        for service in self.services_list:
            for args in language_args_list:
                try:
                    result = service.language(*args)
                    assert result
                except (UnsupportedMethod, DeeplTranslateException):
                    continue

    def test_service_text_to_speech(self):
        texts_args_list = [["What cool weater todaiy"], ["Привет"],
                           ["自动"]]

        for service in self.services_list:
            for args in texts_args_list:
                try:
                    result = service.text_to_speech(*args)
                    assert result
                except (UnsupportedMethod, DeeplTranslateException):
                    continue
