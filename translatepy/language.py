"""
Handles the languages management on `translatepy`
"""

import re
import typing

from translatepy import exceptions
from translatepy.utils import similarity, sanitize, _language_data, lru_cacher

# preparing the vectors
LOADED_VECTORS = [similarity.StringVector(language, data=data) for language, data in _language_data.VECTORS.items()]

LANGUAGE_CLEANUP_REGEX = re.compile(r"\(.+\)")

# Type alias
Number = typing.Union[int, float]


class Scopes():
    class Scope():
        def __init__(self, name: str) -> None:
            self.name = str(name)

        def __str__(self) -> str:
            return self.name

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

        def __str__(self) -> str:
            return self.name

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


_languages_cache = lru_cacher.LRUDictCache(512)


class Language():
    """
    A class holding language data
    """

    class LanguageExtra():
        """
        Provides extra information on the language (limited to some languages)
        """

        def __init__(self, data: dict) -> None:
            self.type = Types().get(data.get("t", None))
            self.scope = Scopes().get(data.get("s", None))

        def __repr__(self) -> str:
            return "LanguageExtra(type={type}, scope={scope})".format(type=self.type, scope=self.scope)

        def as_dict(self) -> dict:
            return {
                "type": self.type.name if self.type is not None else None,
                "scope": self.scope.name if self.scope is not None else None
            }

    def __init__(self, language: typing.Union[str, "Language"], threshold: Number = 93) -> None:
        if isinstance(language, Language):
            self.id = language.id
            self.similarity = language.similarity
        else:
            if language is None or sanitize.remove_spaces(language) == "":
                raise exceptions.UnknownLanguage("N/A", 0, "You need to pass in a language")
            language = str(language)
            normalized_language = sanitize.remove_spaces(LANGUAGE_CLEANUP_REGEX.sub("", language.lower()))

            # Check the incoming language, whether it is in the cache, then return the values from the cache
            if normalized_language in _languages_cache:
                self.id, self.similarity = _languages_cache[normalized_language]
            else:
                if normalized_language in _language_data.CODES:
                    self.id = _language_data.CODES[normalized_language]
                    self.similarity = 100
                else:
                    _search_result, _similarity = similarity.fuzzy_search(LOADED_VECTORS, normalized_language)
                    self.similarity = _similarity * 100
                    if self.similarity < threshold:
                        raising_message = "Couldn't recognize the given language ({0})\nDid you mean: {1} (Similarity: {2}%)?".format(language, _search_result, round(self.similarity, 2))
                        raise exceptions.UnknownLanguage(_search_result, self.similarity, raising_message)
                    self.id = _language_data.VECTORS[_search_result]["i"]

            # Сache the language values to speed up the language recognition process in the future
            _languages_cache[normalized_language] = (self.id, self.similarity)

        data = _language_data.LANGUAGE_DATA[self.id]

        self.alpha2 = data.get("2", None)
        self.alpha3b = data.get("b", None)
        self.alpha3t = data.get("t", None)
        self.alpha3 = str(data["3"])
        self.name = str(data["e"])
        self.extra = self.LanguageExtra(data.get("x", {}))
        self.in_foreign_languages = dict(data.get("f", {}))
        self.in_foreign_languages["en"] = self.name

    def clean_cache(self) -> None:
        """
        Cleans the language tokens similarity caches
        """
        _languages_cache.clear()

    def __repr__(self) -> str:
        return "Language({language})".format(language=self.id)

    def __str__(self) -> str:
        """
        Returns the identifier for this language
        """
        return str(self.id)

    def as_dict(self, foreign: bool = True) -> dict:
        """
        Returns a dictionary representation of the `Language` object
        """
        return {
            "id": self.id,
            "alpha2": self.alpha2,
            "alpha3b": self.alpha3b,
            "alpha3t": self.alpha3t,
            "alpha3": self.alpha3,
            "name": self.name,
            "extra": self.extra.as_dict(),
            "in_foreign_languages": self.in_foreign_languages if foreign else None
        }
