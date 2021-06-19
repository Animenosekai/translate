#from translatepy.utils import iso639
#from translatepy.utils.iso639_table import Language as LanguageISO639
from translatepy.utils.similarity import fuzzy_search
from translatepy.utils.lru_cacher import LRUDictCache
from translatepy.exceptions import UnknownLanguage


class Language():

    _languages_cache = LRUDictCache(512)

    def __init__(self, language: str):

        # We check the incoming argument language, whether it is a string, if not, we raise an exception
        if not isinstance(language, str) and not isinstance(language, LanguageISO639):
            raise TypeError("Parameter 'language' must be a string or Language instance, {} was given".format(type(language).__name__))

        if not isinstance(language, LanguageISO639):
            # Starting language recognition
            self.language, self.similarity = self._detect_language(language)
        else:
            self.language, self.similarity = language, 100

        for _foreign_lang_code, _name_in_foreign_lang in self.language.in_foreign_languages.items():
            setattr(self, _foreign_lang_code, _name_in_foreign_lang)
            setattr(self, iso639.by_alpha2.get(_foreign_lang_code).name.lower(), _name_in_foreign_lang)

    def _detect_language(self, language: str):

        _language = language.lower()

        result = None
        similarity = 100

        # Check the incoming language, whether it is in the cache, then return the values from the cache
        if _language in self._languages_cache:
            result, similarity = self._languages_cache[_language]

        # Starting the language recognition process
        # First of all, we do an accurate search for the language, if the accurate search the language did not give any result, then we proceed to a non-accurate (fuzzy) search
        if result is None:
            result = iso639.by_alpha2.get(_language, None)

        if result is None:
            result = iso639.by_alpha3.get(_language, None)

        if result is None:
            result = iso639.by_name.get(_language, None)

        if result is None:
            result = iso639.by_foreign_name.get(_language, None)

        if result is None:
            similarity, result = self._language_search(_language)

        # Сache the language values to speed up the language recognition process in the future
        self._languages_cache[_language] = (result, similarity)

        if similarity < 93 or result is None:
            raise UnknownLanguage("Couldn't recognize the given language ({0})\nDid you mean: {1} (Similarity: {2}%)?".format(language, result.name, similarity))

        return result, similarity

    def _language_search(self, _language):
        _language_names = [name for name, lang_typle in iso639.by_name.items()]
        _foreign_language_names = [name for name, lang_typle in iso639.by_foreign_name.items()]
        _all_languages_names = _language_names + _foreign_language_names

        _search_result, _similarity = fuzzy_search(_all_languages_names, _language)

        result = iso639.by_name.get(_search_result, None)
        if result is None:
            result = iso639.by_foreign_name.get(_search_result, None)

        return round(_similarity * 100), result

    def clean_cache(self) -> None:
        self._languages_cache.clear()

    def __repr__(self):
        return str(self.language)

    def __getattr__(self, name):
        return getattr(self.language, name, None)

    def __str__(self):
        return self.language.alpha2

    def __len__(self):
        return len(iso639._languages_list)

    def __iter__(self):
        return iter(iso639._languages_list)

    @classmethod
    def by_yandex(cls, language_code):
        return iso639.by_yandex.get(language_code.lower())

    @classmethod
    def by_google(cls, language_code):
        return cls(iso639.by_google.get(language_code.lower()))

    @classmethod
    def by_bing(cls, language_code):
        return cls(iso639.by_bing.get(language_code.lower()))

    @classmethod
    def by_reverso(cls, language_code):
        return cls(iso639.by_reverso.get(language_code.lower()))

    @classmethod
    def by_deepl(cls, language_code):
        return cls(iso639.by_deepl.get(language_code.lower()))
