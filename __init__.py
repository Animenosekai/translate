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
                    if response is None:
                        raise TranslationError("An error occured while translating your text")
                    else:
                        return response
                else:
                    return response
            else:
                return response
        else:
            return response

    def transliterate(self, text, source_language):
        pass

    def spellcheck(self, text, source_language):
        pass

    def language(self, text, source_language):
        pass

    def example(self, text, source_language):
        pass

translator = Translator()