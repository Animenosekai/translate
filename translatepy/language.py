"""
Handles the languages management on `translatepy`
"""

import copy
import pathlib
import typing

import cain

from translatepy import exceptions
from translatepy.utils import lru, vectorize

# Type alias
Number = typing.Union[int, float]


class LanguageExtra(cain.Object):
    """Extra data given on supported languages"""
    scope: cain.types.Enum["individual", "macrolanguage", "special"]
    """Language scope"""
    type: cain.types.Enum["ancient", "constructed", "extinct",
                          "historical", "living", "special"]
    """Language type"""


class Foreign(cain.Object):
    """The language name in foreign languages"""
    afrikaans: typing.Optional[str]
    """The language name in afrikaans, if available"""
    albanian: typing.Optional[str]
    """The language name in albanian, if available"""
    amharic: typing.Optional[str]
    """The language name in amharic, if available"""
    arabic: typing.Optional[str]
    """The language name in arabic, if available"""
    armenian: typing.Optional[str]
    """The language name in armenian, if available"""
    azerbaijani: typing.Optional[str]
    """The language name in azerbaijani, if available"""
    basque: typing.Optional[str]
    """The language name in basque, if available"""
    bashkir: typing.Optional[str]
    """The language name in bashkir, if available"""
    belarusian: typing.Optional[str]
    """The language name in belarusian, if available"""
    bengali: typing.Optional[str]
    """The language name in bengali, if available"""
    bosnian: typing.Optional[str]
    """The language name in bosnian, if available"""
    bulgarian: typing.Optional[str]
    """The language name in bulgarian, if available"""
    catalan: typing.Optional[str]
    """The language name in catalan, if available"""
    chuvash: typing.Optional[str]
    """The language name in chuvash, if available"""
    cebuano: typing.Optional[str]
    """The language name in cebuano, if available"""
    nyanja: typing.Optional[str]
    """The language name in nyanja, if available"""
    corsican: typing.Optional[str]
    """The language name in corsican, if available"""
    croatian: typing.Optional[str]
    """The language name in croatian, if available"""
    czech: typing.Optional[str]
    """The language name in czech, if available"""
    danish: typing.Optional[str]
    """The language name in danish, if available"""
    dutch: typing.Optional[str]
    """The language name in dutch, if available"""
    esperanto: typing.Optional[str]
    """The language name in esperanto, if available"""
    estonian: typing.Optional[str]
    """The language name in estonian, if available"""
    tagalog: typing.Optional[str]
    """The language name in tagalog, if available"""
    finnish: typing.Optional[str]
    """The language name in finnish, if available"""
    french: typing.Optional[str]
    """The language name in french, if available"""
    westernfrisian: typing.Optional[str]
    """The language name in westernfrisian, if available"""
    galician: typing.Optional[str]
    """The language name in galician, if available"""
    georgian: typing.Optional[str]
    """The language name in georgian, if available"""
    german: typing.Optional[str]
    """The language name in german, if available"""
    moderngreek: typing.Optional[str]
    """The language name in moderngreek, if available"""
    gujarati: typing.Optional[str]
    """The language name in gujarati, if available"""
    haitian: typing.Optional[str]
    """The language name in haitian, if available"""
    hausa: typing.Optional[str]
    """The language name in hausa, if available"""
    hawaiian: typing.Optional[str]
    """The language name in hawaiian, if available"""
    hindi: typing.Optional[str]
    """The language name in hindi, if available"""
    hmong: typing.Optional[str]
    """The language name in hmong, if available"""
    hungarian: typing.Optional[str]
    """The language name in hungarian, if available"""
    icelandic: typing.Optional[str]
    """The language name in icelandic, if available"""
    igbo: typing.Optional[str]
    """The language name in igbo, if available"""
    indonesian: typing.Optional[str]
    """The language name in indonesian, if available"""
    irish: typing.Optional[str]
    """The language name in irish, if available"""
    italian: typing.Optional[str]
    """The language name in italian, if available"""
    japanese: typing.Optional[str]
    """The language name in japanese, if available"""
    kannada: typing.Optional[str]
    """The language name in kannada, if available"""
    kazakh: typing.Optional[str]
    """The language name in kazakh, if available"""
    khmer: typing.Optional[str]
    """The language name in khmer, if available"""
    korean: typing.Optional[str]
    """The language name in korean, if available"""
    kurdish: typing.Optional[str]
    """The language name in kurdish, if available"""
    kirghiz: typing.Optional[str]
    """The language name in kirghiz, if available"""
    lao: typing.Optional[str]
    """The language name in lao, if available"""
    latin: typing.Optional[str]
    """The language name in latin, if available"""
    latvian: typing.Optional[str]
    """The language name in latvian, if available"""
    lithuanian: typing.Optional[str]
    """The language name in lithuanian, if available"""
    luxembourgish: typing.Optional[str]
    """The language name in luxembourgish, if available"""
    macedonian: typing.Optional[str]
    """The language name in macedonian, if available"""
    malagasy: typing.Optional[str]
    """The language name in malagasy, if available"""
    malay: typing.Optional[str]
    """The language name in malay, if available"""
    malayalam: typing.Optional[str]
    """The language name in malayalam, if available"""
    maltese: typing.Optional[str]
    """The language name in maltese, if available"""
    maori: typing.Optional[str]
    """The language name in maori, if available"""
    marathi: typing.Optional[str]
    """The language name in marathi, if available"""
    mongolian: typing.Optional[str]
    """The language name in mongolian, if available"""
    burmese: typing.Optional[str]
    """The language name in burmese, if available"""
    nepali: typing.Optional[str]
    """The language name in nepali, if available"""
    norwegian: typing.Optional[str]
    """The language name in norwegian, if available"""
    oriya: typing.Optional[str]
    """The language name in oriya, if available"""
    pushto: typing.Optional[str]
    """The language name in pushto, if available"""
    persian: typing.Optional[str]
    """The language name in persian, if available"""
    polish: typing.Optional[str]
    """The language name in polish, if available"""
    portuguese: typing.Optional[str]
    """The language name in portuguese, if available"""
    panjabi: typing.Optional[str]
    """The language name in panjabi, if available"""
    romanian: typing.Optional[str]
    """The language name in romanian, if available"""
    russian: typing.Optional[str]
    """The language name in russian, if available"""
    samoan: typing.Optional[str]
    """The language name in samoan, if available"""
    scottishgaelic: typing.Optional[str]
    """The language name in scottishgaelic, if available"""
    serbian: typing.Optional[str]
    """The language name in serbian, if available"""
    southernsotho: typing.Optional[str]
    """The language name in southernsotho, if available"""
    shona: typing.Optional[str]
    """The language name in shona, if available"""
    sindhi: typing.Optional[str]
    """The language name in sindhi, if available"""
    sinhala: typing.Optional[str]
    """The language name in sinhala, if available"""
    slovak: typing.Optional[str]
    """The language name in slovak, if available"""
    slovenian: typing.Optional[str]
    """The language name in slovenian, if available"""
    somali: typing.Optional[str]
    """The language name in somali, if available"""
    spanish: typing.Optional[str]
    """The language name in spanish, if available"""
    sundanese: typing.Optional[str]
    """The language name in sundanese, if available"""
    swahili: typing.Optional[str]
    """The language name in swahili, if available"""
    swedish: typing.Optional[str]
    """The language name in swedish, if available"""
    tajik: typing.Optional[str]
    """The language name in tajik, if available"""
    tamil: typing.Optional[str]
    """The language name in tamil, if available"""
    telugu: typing.Optional[str]
    """The language name in telugu, if available"""
    thai: typing.Optional[str]
    """The language name in thai, if available"""
    turkish: typing.Optional[str]
    """The language name in turkish, if available"""
    tatar: typing.Optional[str]
    """The language name in tatar, if available"""
    ukrainian: typing.Optional[str]
    """The language name in ukrainian, if available"""
    urdu: typing.Optional[str]
    """The language name in urdu, if available"""
    uighur: typing.Optional[str]
    """The language name in uighur, if available"""
    uzbek: typing.Optional[str]
    """The language name in uzbek, if available"""
    vietnamese: typing.Optional[str]
    """The language name in vietnamese, if available"""
    welsh: typing.Optional[str]
    """The language name in welsh, if available"""
    xhosa: typing.Optional[str]
    """The language name in xhosa, if available"""
    yiddish: typing.Optional[str]
    """The language name in yiddish, if available"""
    yoruba: typing.Optional[str]
    """The language name in yoruba, if available"""
    zulu: typing.Optional[str]
    """The language name in zulu, if available"""
    chinese: typing.Optional[str]
    """The language name in chinese, if available"""
    hebrew: typing.Optional[str]
    """The language name in hebrew, if available"""
    javanese: typing.Optional[str]
    """The language name in javanes, if available"""


LANGUAGE_CACHE = lru.LRUDictCache(512)


class Language(cain.Object):
    """A language"""

    id: str
    """The language identifier"""
    alpha3: str
    """The ISO 639-3 (Alpha-3) code"""
    name: str
    """The english name"""
    alpha2: typing.Optional[str]
    """The ISO 639-1 (Alpha-2) code, if available"""
    alpha3b: typing.Optional[str]
    """The ISO 639-2B (Alpha-3) code, if available"""
    alpha3t: typing.Optional[str]
    """The ISO 639-2T (Alpha-3) code, if available"""
    extra: typing.Optional[LanguageExtra]
    """Extra data for the language, if available"""
    foreign: typing.Optional[Foreign]
    """Name in foreign languages, if available"""

    def __init__(self, language: typing.Union[str, "Language", typing.Dict], threhsold: int = 93) -> None:
        if isinstance(language, typing.Dict):
            super().__init__(language)
        elif isinstance(language, Language):
            self._cain_value = copy.copy(language.value)
        else:
            results = self.search(str(language))
            if not results:
                raise exceptions.UnknownLanguage("N/A", 0,
                                                 "Couldn't find any corresponding language")
            result = results[0]
            if result.similarity < threhsold:
                raise exceptions.UnknownLanguage(result, result.similarity,
                                                 "Couldn\'t find the given language. "
                                                 f'Did you mean "{result.vector.string}" ({result.vector.id}; {round(result.similarity)}%) ?')

            self._cain_value = copy.copy(DATA["data"][result.vector.id])
            self._similarity = result.similarity

    @classmethod
    def search(cls, query: str) -> typing.List[vectorize.SearchResult]:
        """Searches the given language"""
        query = vectorize.string_preprocessing(str(query or ""))
        if not query:
            return []

        # Check the incoming language, whether it is in the cache, then return the values from the cache
        cache_results = LANGUAGE_CACHE.get(query, [])
        if cache_results:
            return cache_results

        code_id = DATA["codes"].get(query, None)
        if code_id:
            return [vectorize.SearchResult(
                vector=vectorize.vectorize(code_id, query),
                similarity=100
            )]

        results = vectorize.search(query, DATA["vectors"])

        # Сache the language values to speed up the language recognition process in the future
        LANGUAGE_CACHE[query] = copy.copy(results)

        return results

    @property
    def similarity(self) -> float:
        """The similarity with the vector while searching the language"""
        return self._similarity


class LanguageData(typing.TypedDict):
    """Groups all of the data"""
    codes: typing.Dict[str, str]
    data: typing.Dict[str, Language]
    vectors: typing.List[vectorize.Vector]


# Loading
LANGUAGE_DATA_DIR = pathlib.Path(__file__).parent / "data" / "languages"

DATA = LanguageData({})

with open(LANGUAGE_DATA_DIR / "codes.cain", "b+r") as f:
    DATA["codes"] = {key: value for key, value in cain.load(f, typing.List[typing.Tuple[str, str]])}

with open(LANGUAGE_DATA_DIR / "data.cain", "b+r") as f:
    DATA["data"] = {value.id: value for value in cain.load(f, typing.List[Language])}

with open(LANGUAGE_DATA_DIR / "vectors.cain", "b+r") as f:
    DATA["vectors"] = cain.load(f, typing.List[vectorize.Vector])
