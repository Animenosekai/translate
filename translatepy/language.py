from typing import Union
from translatepy.utils.lru_cacher import LRUDictCache
from translatepy.exceptions import UnknownLanguage
from translatepy.utils.similarity import StringVector, fuzzy_search
from translatepy.utils._language_cache import VECTORS_CACHE, CODES, LANGUAGE_DATA

# preparing the vectors
VECTORS = [StringVector(language, data=VECTORS_CACHE[language]) for language in VECTORS_CACHE]

class Language():
    _languages_cache = LRUDictCache(512)

    class LanguageExtra():
        def __init__(self, data: dict) -> None:
            self.type = data["type"]
            self.scope = data["scope"]

    def __init__(self, language: str, threshold: Union[int, float] = 93) -> None:
        if language is None:
            raise UnknownLanguage("N/A", 0, "You need to pass in a language")
        language = str(language)
        normalized_language = language.lower().replace(" ", "")

        # Check the incoming language, whether it is in the cache, then return the values from the cache
        if normalized_language in self._languages_cache:
            self.id, self.similarity = self._languages_cache[normalized_language]
        else:
            if normalized_language in CODES:
                self.id = CODES[normalized_language]
                self.similarity = 100
            else:
                _search_result, _similarity = fuzzy_search(VECTORS, normalized_language)
                self.similarity = _similarity * 100
                if self.similarity < threshold:
                    raise UnknownLanguage(_search_result, self.similarity, "Couldn't recognize the given language ({0})\nDid you mean: {1} (Similarity: {2}%)?".format(language, _search_result, round(self.similarity, 2)))
                self.id = VECTORS_CACHE[_search_result]["id"]
            
        data = LANGUAGE_DATA[self.id]

        # Сache the language values to speed up the language recognition process in the future
        self._languages_cache[normalized_language] = (self.id, self.similarity)
        
        self.alpha2 = data["codes"]["alpha2"]
        self.alpha3b = data["codes"]["alpha3"]["iso6392-b"]
        self.alpha3t = data["codes"]["alpha3"]["iso6392-t"]
        self.alpha3 = data["codes"]["alpha3"]["iso6393"]
        self.name = data["english"]
        self.extra = self.LanguageExtra(data["extra"])
        self.in_foreign_languages = data["foreign"]


    def clean_cache(self) -> None:
        self._languages_cache.clear()

    def __repr__(self) -> str:
        return "Language({language})".format(language=self.id)

    def __str__(self) -> str:
        return str(self.id)