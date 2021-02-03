from translators.google import GoogleTranslate
from translators.bing import BingTranslate
from translators.yandex import YandexTranslate
from translators.reverso import ReversoTranslate
from models.exceptions import TranslationError

class Translator():
    """
    A class which groups all of the APIs
    """
    def __init__(self) -> None:
        self.google_translate = GoogleTranslate()
        self.yandex_translate = YandexTranslate()
        self.bing_translate = BingTranslate()
        self.reverso_translate = ReversoTranslate()

    def translate(self, text, destination_language, source_language=None):
        response = self.google_translate.translate(text, destination_language, source_language)
        if response is None:
            response = self.bing_translate.translate(text, destination_language, source_language)
            if response is None:
                response = self.reverso_translate(text, destination_language, source_language)
                if response is None:
                    response = self.yandex_translate.translate(text, destination_language, source_language)
                    return response
                else:
                    return response
            else:
                return response
        else:
            return response

    def transliterate(self, text, source_language):
        return self.yandex_translate.transliterate(text, source_language)

    def spellcheck(self, text, source_language):
        response = self.bing_translate.spellcheck(text, source_language)
        if response is None:
            response = self.reverso_translate.spellcheck(text, source_language)
            if response is None:
                return self.yandex_translate.spellcheck(text, source_language)
            else:
                return response
        else:
            return response

    def language(self, text):
        response = self.google_translate.language(text)
        if response is None:
            response = self.bing_translate.language(text)
            if response is None:
                response = self.reverso_translate.language(text)
                if response is None:
                    return self.yandex_translate.language(text)
                else:
                    return response
            else:
                return response
        else:
            return response

    def example(self, text, destination_language, source_language=None):
        return self.bing_translate.example(text, destination_language, source_language)

translator = Translator()