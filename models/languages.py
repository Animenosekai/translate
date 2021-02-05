from data.data import LANGUAGES_CODE
from data.data import LANGUAGES_NAME_TO_CODE_EN
from data.data import LANGUAGES_NAME_TO_CODE_INTERNATIONAL
from data.data import LANGUAGES_CODE_TO_NAME_EN
from utils.similarity import language_search
from models.exceptions import UnknownLanguage


class Language():
    def __init__(self, language) -> None:
        self.language = str(language).lower()
        if self.language == 'zh-cn':
            self.language = 'zh-CN'
            self.similarity = 1
        elif self.language == 'zh-tw':
            self.language = 'zh-TW'
            self.similarity = 1
        elif self.language not in LANGUAGES_CODE:
            result = LANGUAGES_NAME_TO_CODE_EN.get(self.language, None)
            if result is None:
                result = LANGUAGES_NAME_TO_CODE_INTERNATIONAL.get(self.language, None)
                if result is None:
                    name, lang, similarity = language_search(self.language)
                    if similarity > 0.95:
                        self.language = lang
                        self.similarity = similarity
                    else:
                        exception_message = "Couldn't recognize the given language (" + str(language) + ")\nDid you mean '" + name + "' (Similarity: " + str(round(similarity*100, 2)) + "%)?"
                        raise UnknownLanguage(exception_message)
                else:
                    self.language = result
                    self.similarity = 1
            else:
                self.language = result
                self.similarity = 1
        else:
            self.similarity = 1

    
        self.name = LANGUAGES_CODE_TO_NAME_EN.get(self.language, "Unknown").title()
                
        #### Defining for specific translators (not available for now)
        self.google_translate = self.language
        self.bing_translate = self.language
        self.yandex_translate = self.language
        self.reverso = self.language
    
    def __repr__(self) -> str:
        if self.similarity != 1:
            return self.name + " (Similarity: " + str(round(self.similarity*100, 2)) + "%)"
        else:
            return self.name

    def __str__(self) -> str:
        return self.language

    def __call__(self, *args, **kwds):
        return self.language

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Language):
            return o.language == self.language
        return str(o) == self.result

    def __ne__(self, o: object) -> bool:
        if isinstance(o, Language):
            return o.language != self.language
        return str(o) != self.result
