from re import compile
from translatepy.utils.sanitize import remove_spaces
from typing import Union

from translatepy.exceptions import UnknownLanguage
from translatepy.utils._language_data import CODES, LANGUAGE_DATA, VECTORS
from translatepy.utils.lru_cacher import LRUDictCache
from translatepy.utils.similarity import StringVector, fuzzy_search

# preparing the vectors
LOADED_VECTORS = [StringVector(language, data=data) for language, data in VECTORS.items()]

LANGUAGE_CLEANUP_REGEX = compile("\(.+\)")


class Scopes():
    class Scope():
        def __init__(self, name: str) -> None:
            self.name = str(name)

        def __repr__(self) -> str:
            return "LanguageScope({name})".format(name=self.name)

    def get(self, name: str):
        if name is None:
            return
        name = str(name).lower().replace(" ", "")
        if name == "individual":
            return self.INDIVIDUAL
        elif name == "macrolanguage":
            return self.MACROLANGUAGE
        return self.SPECIAL

    INDIVIDUAL = Scope("Individual")
    MACROLANGUAGE = Scope("Macrolanguage")
    SPECIAL = Scope("Special")


class Types():
    class Type():
        def __init__(self, name: str) -> None:
            self.name = str(name)

        def __repr__(self) -> str:
            return "LanguageType({name})".format(name=self.name)

    def get(self, name: str):
        if name is None:
            return
        name = str(name).lower().replace(" ", "")
        if name == "living":
            return self.LIVING
        elif name == "ancient":
            return self.ANCIENT
        elif name == "extinct":
            return self.EXTINCT
        elif name == "historical":
            return self.HISTORICAL
        elif name == "constructed":
            return self.CONSTRUCTED
        return self.SPECIAL

    ANCIENT = Type("Ancient")
    CONSTRUCTED = Type("Constructed")
    EXTINCT = Type("Extinct")
    HISTORICAL = Type("Historical")
    LIVING = Type("Living")
    SPECIAL = Type("Special")


_languages_cache = LRUDictCache(512)


class Language():

    class LanguageExtra():
        def __init__(self, data: dict) -> None:
            self.type = Types().get(data.get("t", None))
            self.scope = Scopes().get(data.get("s", None))

        def __repr__(self) -> str:
            return "LanguageExtra(type={type}, scope={scope})".format(type=self.type, scope=self.scope)

    def __init__(self, language: str, threshold: Union[int, float] = 93) -> None:
        if isinstance(language, Language):
            return language
        if language is None or remove_spaces(language) == "":
            raise UnknownLanguage("N/A", 0, "You need to pass in a language")
        language = str(language)
        normalized_language = remove_spaces(LANGUAGE_CLEANUP_REGEX.sub("", language.lower()))

        # Check the incoming language, whether it is in the cache, then return the values from the cache
        if normalized_language in _languages_cache:
            self.id, self.similarity = _languages_cache[normalized_language]
        else:
            if normalized_language in CODES:
                self.id = CODES[normalized_language]
                self.similarity = 100
            else:
                _search_result, _similarity = fuzzy_search(LOADED_VECTORS, normalized_language)
                self.similarity = _similarity * 100
                if self.similarity < threshold:
                    raise UnknownLanguage(_search_result, self.similarity, "Couldn't recognize the given language ({0})\nDid you mean: {1} (Similarity: {2}%)?".format(language, _search_result, round(self.similarity, 2)))
                self.id = VECTORS[_search_result]["i"]

        data = LANGUAGE_DATA[self.id]

        # Сache the language values to speed up the language recognition process in the future
        _languages_cache[normalized_language] = (self.id, self.similarity)

        self.alpha2 = data.get("2", None)
        self.alpha3b = data.get("b", None)
        self.alpha3t = data.get("t", None)
        self.alpha3 = str(data["3"])
        self.name = str(data["e"])
        self.extra = self.LanguageExtra(data.get("x", {}))
        self.in_foreign_languages = dict(data.get("f", {}))
        self.in_foreign_languages["en"] = self.name

    def clean_cache(self) -> None:
        _languages_cache.clear()

    def __repr__(self) -> str:
        return "Language({language})".format(language=self.id)

    def __str__(self) -> str:
        return str(self.id)
