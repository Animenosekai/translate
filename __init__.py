from models.languages import Language
from translators.google import GoogleTranslate
from translators.bing import BingTranslate
from translators.yandex import YandexTranslate
from translators.reverso import ReversoTranslate

CACHES = []
AUTOMATIC = Language("auto")

class TranslationResult():
    def __init__(self, source, result, source_language, destination_language) -> None:
        self.source = str(source)
        self.result = str(result)
        self.source_language = source_language
        self.destination_language = destination_language

    def __repr__(self) -> str:
        return "Source (" + (self.source_language.name if isinstance(self.source_language, Language) else str(self.source_language)) + "): " + self.source + "\nResult (" + (self.destination_language.name if isinstance(self.destination_language, Language) else str(self.destination_language)) + "): " + self.result

    def __str__(self) -> str:
        return self.result

    def __call__(self, *args, **kwds):
        return self.result

    def __eq__(self, o: object) -> bool:
        return str(o) == self.result

    def __ne__(self, o: object) -> bool:
        return str(o) != self.result
            

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
        global CACHES
        if not isinstance(destination_language, Language):
            destination_language = Language(destination_language)
        if source_language is not None and not isinstance(source_language, Language):
            source_language = Language(source_language)
        
        lang, response = self.google_translate.translate(text, destination_language, source_language)
        if response is None:
            lang, response = self.bing_translate.translate(text, destination_language, source_language)
            if response is None:
                lang, response = self.reverso_translate(text, destination_language, source_language)
                if response is None:
                    lang, response = self.yandex_translate.translate(text, destination_language, source_language)
                    if response is None:
                        return None
                    try:
                        lang = Language(lang)
                    except: pass
                    return TranslationResult(source=text, result=response, source_language=lang, destination_language=destination_language)
                else:
                    try:
                        lang = Language(lang)
                    except: pass
                    return TranslationResult(source=text, result=response, source_language=lang, destination_language=destination_language)
            else:
                try:
                    lang = Language(lang)
                except: pass
                return TranslationResult(source=text, result=response, source_language=lang, destination_language=destination_language)
        else:
            try:
                lang = Language(lang)
            except: pass
            return TranslationResult(source=text, result=response, source_language=lang, destination_language=destination_language)

    def transliterate(self, text, source_language=None):
        if source_language is not None and not isinstance(source_language, Language):
            source_language = Language(source_language)
        return self.yandex_translate.transliterate(text, source_language)

    def spellcheck(self, text, source_language=None):
        if source_language is not None and not isinstance(source_language, Language):
            source_language = Language(source_language)
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
                    response = self.yandex_translate.language(text)
                    if response is None:
                        return response
                    else:
                        try:
                            return Language(response)
                        except:
                            return response
                else:
                    try:
                        return Language(response)
                    except:
                        return response
            else:
                try:
                    return Language(response)
                except:
                    return response
        else:
            try:
                return Language(response)
            except:
                return response

    def example(self, text, destination_language, source_language=None):
        if not isinstance(destination_language, Language):
            destination_language = Language(destination_language)
        if source_language is not None and not isinstance(source_language, Language):
            source_language = Language(source_language)
        return self.bing_translate.example(text, destination_language, source_language)

#translator = Translator()