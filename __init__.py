from translators.google import GoogleTranslate
from translators.bing import BingTranslate
from translators.yandex import YandexTranslate
from models.exceptions import TranslationError

class Translator():
    """
    A class which groups all of the APIs
    """
    def __init__(self) -> None:
        self.google_translate = GoogleTranslate()
        self.yandex_translate = YandexTranslate()
        self.bing_translate = BingTranslate()

    def translate(self, text, destination_language, source_language=None):
        response = self.google_translate.translate(text, destination_language, source_language)
        if response is None:
            response = self.bing_translate.translate(text, destination_language, source_language)
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