from translatepy import Translate


class TestAllTranslators:
    def setup(self):
        self.translator = Translate()

    def test_translate(self):
        translation_args_list = [["What cool weather today!", "fr"],
                                 ["Hello", "Japanese", "en"],
                                 ["Hello, how are you?", "ja"]]

        for args in translation_args_list:
            assert self.translator.translate(*args)

    def test_transliterate(self):
        transliteration_args_list = [["What cool weather today!", "ar"],
                                     ["Hello", "Japanese", "en"],
                                     ["Hello, how are you?", "ja"]]

        for args in transliteration_args_list:
            assert self.translator.transliterate(*args)

    def test_spellcheck(self):
        spellcheck_args_list = [["What cool weater todai!"], ["Helo"],
                                ["Helo, how are tou?"]]

        for args in spellcheck_args_list:
            assert self.translator.spellcheck(*args)

    def test_example(self):
        example_args_list = [["What cool weater todai!", "fr"], ["Helo", "French"],
                             ["Helo, how are tou?", "ru"]]

        for args in example_args_list:
            assert self.translator.example(*args)

    def test_dictionary(self):
        dictionary_args_list = [["What cool weater todai!", "fr"], ["Helo", "French"],
                                ["Helo, how are tou?", "ru"]]

        for args in dictionary_args_list:
            assert self.translator.dictionary(*args)

    def test_language(self):
        language_args_list = [["What cool weater todaiy"], ["Привет"],
                              ["自动"]]

        for args in language_args_list:
            assert self.translator.language(*args)

    def test_text_to_speech(self):
        texts_args_list = [["What cool weater todaiy"], ["Привет"],
                           ["自动"]]

        for args in texts_args_list:
            assert self.translator.text_to_speech(*args)

    def test_translate_html(self):
        translation_args_list = [("<h1>Hello</h1> <span class='everyone'>everyone</span><br>I hope that <span class='everyone'>everyone</span><div class='okay-container'> is doing <strong>Okay〜!</strong></div>", "ja")]

        for args in translation_args_list:
            assert self.translator.translate_html(*args)
