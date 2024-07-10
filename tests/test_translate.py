"""Tests the aggregation of translators"""
import typing

from translatepy import BaseTranslator, Translate
from translatepy.translate import DEFAULT_TRANSLATORS


def alternate(func):
    """Tests with and without fast mode enabled"""

    def wrapper(self):
        # First, we test the method with fast mode disabled
        print(f"Testing {func.__name__}")
        self.translator = Translate(services_list=self.services, fast=False)
        func(self)

        print(f"Testing {func.__name__} with fast mode enabled")
        self.translator = Translate(services_list=self.services, fast=True)
        return func(self)
    return wrapper


class TestAllTranslators:
    """Tests the translators aggregator"""
    translator: Translate
    services: typing.List[BaseTranslator]

    def setup(self):
        """Sets up the test"""
        self.translator = Translate()
        self.services = DEFAULT_TRANSLATORS

    def apply(self, method: str, *args):
        """Tests the given method with the given args"""
        for arg_list in args:
            assert getattr(self.translator, method)(*arg_list)
        return True

    @alternate
    def test_translate(self):
        """Tests the `translate` method"""
        # TODO: Might add a decorator which gets the method name
        # from the testing function name and apply automatically
        assert self.apply("translate",
                          ["What cool weather today!", "fr"],
                          ["Hello", "Japanese", "en"],
                          ["Hello, how are you?", "ja"])

    @alternate
    def test_transliterate(self):
        """Tests the `transliterate` method"""
        assert self.apply("transliterate",
                          ["What cool weather today!", "ar"],
                          ["Hello", "Japanese", "en"],
                          ["Hello, how are you?", "ja"])

    @alternate
    def test_spellcheck(self):
        """Tests the `spellcheck` method"""
        assert self.apply("spellcheck",
                          ["What cool weater todai!"],
                          ["Helo"],
                          ["Helo, how are tou?"])

    @alternate
    def test_language(self):
        """Tests the `language` method"""
        assert self.apply("language",
                          ["What cool weater todaiy"],
                          ["Привет"],
                          ["自动"])

    @alternate
    def test_example(self):
        """Tests the `example` method"""
        assert self.apply("example",
                          ["What cool weater todai!", "fr"],
                          ["Helo", "French"],
                          ["Helo, how are tou?", "ru"])

    @alternate
    def test_translate_html(self):
        """Tests the `translate_html` method"""
        assert self.apply("translate_html",
                          ("<h1>Hello</h1> <span class='everyone'>everyone</span><br>I hope that <span class='everyone'>everyone</span><div class='okay-container'> is doing <strong>Okay〜!</strong></div>", "ja"))

    # TODO: ADD TESTS
    # @alternate
    # def test_dictionary(self):
    #     dictionary_args_list = [["What cool weater todai!", "fr"], ["Helo", "French"],
    #                             ["Helo, how are tou?", "ru"]]

    #     for args in dictionary_args_list:
    #         assert self.translator.dictionary(*args)

    # @alternate
    # def test_text_to_speech(self):
    #     texts_args_list = [["What cool weater todaiy"], ["Привет"],
    #                        ["自动"]]

    #     for args in texts_args_list:
    #         assert self.translator.text_to_speech(*args)
