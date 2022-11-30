from translatepy.exceptions import UnsupportedMethod
from translatepy.translators.base import BaseTranslator
from translatepy.translators.bing import (BingTranslate, BingTranslateException)
from translatepy.translators.deepl import (DeeplTranslate, DeeplTranslateException)
from translatepy.translators.google import GoogleTranslateV1, GoogleTranslateV2
from translatepy.translators.mymemory import (MyMemoryTranslate, MyMemoryException)
from translatepy.translators.reverso import ReversoTranslate
from translatepy.translators.translatecom import TranslateComTranslate
from translatepy.translators.yandex import (YandexTranslate, YandexTranslateException)
from translatepy.translators.microsoft import MicrosoftTranslate

IGNORED_EXCEPTIONS = (UnsupportedMethod, DeeplTranslateException, BingTranslateException, MyMemoryException, YandexTranslateException)  # DeepL's and Bing's rate limit is way too sensitive


class TestAllTranslators:
    def setup(self):
        all_services_list = [
            GoogleTranslateV1,
            GoogleTranslateV2,
            BingTranslate,
            ReversoTranslate,
            YandexTranslate,
            DeeplTranslate,
            TranslateComTranslate,
            MyMemoryTranslate,
            MicrosoftTranslate
        ]

        self.services_list = []

        for service in all_services_list:
            if not isinstance(service, BaseTranslator):
                try:
                    self.services_list.append(service())
                except IGNORED_EXCEPTIONS as ex:
                    self._print_exception_info(ex)
            else:
                self.services_list.append(service)

    def _print_exception_info(self, exception: Exception):
        print("During test, '{exception_name}({exception_info})' exception was catched. Ignoring...".format(exception_name=exception.__class__.__name__, exception_info=str(exception)))

    def test_service_translate(self):
        translation_args_list = [("Hello, how are you?", "ja")]

        for service in self.services_list:
            for args in translation_args_list:
                try:
                    result = service.translate(*args)
                    assert result
                except IGNORED_EXCEPTIONS as ex:
                    self._print_exception_info(ex)
                    continue

    def test_service_transliterate(self):
        transliteration_args_list = [("こんにちは?", "en")]

        for service in self.services_list:
            for args in transliteration_args_list:
                try:
                    result = service.transliterate(*args)
                    assert result
                except IGNORED_EXCEPTIONS as ex:
                    self._print_exception_info(ex)
                    continue

    def test_service_spellcheck(self):
        spellcheck_args_list = [("Helo, how are tou?",)]

        for service in self.services_list:
            for args in spellcheck_args_list:
                try:
                    result = service.spellcheck(*args)
                    assert result
                except IGNORED_EXCEPTIONS as ex:
                    self._print_exception_info(ex)
                    continue

    def test_service_example(self):
        example_args_list = [("Hello", "french")]

        for service in self.services_list:
            for args in example_args_list:
                try:
                    result = service.example(*args)
                    assert result
                except IGNORED_EXCEPTIONS as ex:
                    self._print_exception_info(ex)
                    continue

    def test_service_dictionary(self):
        dictionary_args_list = [("Hello", "french")]

        for service in self.services_list:
            for args in dictionary_args_list:
                try:
                    result = service.dictionary(*args)
                    assert result
                except IGNORED_EXCEPTIONS as ex:
                    self._print_exception_info(ex)
                    continue

    def test_service_language(self):
        language_args_list = [("Привет",)]

        for service in self.services_list:
            for args in language_args_list:
                try:
                    result = service.language(*args)
                    assert result
                except IGNORED_EXCEPTIONS as ex:
                    self._print_exception_info(ex)
                    continue

    def test_service_text_to_speech(self):
        texts_args_list = [("自动",)]

        for service in self.services_list:
            for args in texts_args_list:
                try:
                    result = service.text_to_speech(*args)
                    assert result
                except IGNORED_EXCEPTIONS as ex:
                    self._print_exception_info(ex)
                    continue

    def test_service_translate_html(self):
        translation_args_list = [("<h1>Hello</h1> <span class='everyone'>everyone</span><br>I hope that <span class='everyone'>everyone</span><div class='okay-container'> is doing <strong>Okay〜!</strong></div>", "ja")]

        for service in self.services_list:
            for args in translation_args_list:
                try:
                    result = service.translate_html(*args)
                    assert result
                except IGNORED_EXCEPTIONS as ex:
                    self._print_exception_info(ex)
                    continue
