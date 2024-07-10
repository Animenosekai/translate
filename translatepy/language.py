"""
Handles the languages management on `translatepy`
"""

import copy
import os
import pathlib
import typing

import cain
from nasse.utils.boolean import to_bool

from translatepy import exceptions
from translatepy.utils import lru, vectorize

# Type alias
Number = typing.Union[int, float]
"""Represents a number"""


class LanguageExtra(cain.Object):
    """Extra data given on supported languages"""
    scope: cain.types.Enum["individual", "macrolanguage", "special"]
    """Language scope
    
    Note: Can be one of "individual", "macrolanguage", "special"
    """
    type: cain.types.Enum["ancient", "constructed", "extinct",
                          "historical", "living", "special"]
    """
    Language type
    
    Note: Can be one of "ancient", "constructed", "extinct", "historical", "living", "special"
    """


class Foreign(cain.Object):
    """The language name in foreign languages"""
    afrikaans: str
    """The language name in afrikaans"""
    albanian: str
    """The language name in albanian"""
    amharic: str
    """The language name in amharic"""
    arabic: str
    """The language name in arabic"""
    armenian: str
    """The language name in armenian"""
    azerbaijani: str
    """The language name in azerbaijani"""
    basque: str
    """The language name in basque"""
    belarusian: str
    """The language name in belarusian"""
    bengali: str
    """The language name in bengali"""
    bosnian: str
    """The language name in bosnian"""
    bulgarian: str
    """The language name in bulgarian"""
    burmese: str
    """The language name in burmese"""
    catalan: str
    """The language name in catalan"""
    chinese: str
    """The language name in chinese"""
    croatian: str
    """The language name in croatian"""
    czech: str
    """The language name in czech"""
    danish: str
    """The language name in danish"""
    dutch: str
    """The language name in dutch"""
    esperanto: str
    """The language name in esperanto"""
    estonian: str
    """The language name in estonian"""
    finnish: str
    """The language name in finnish"""
    french: str
    """The language name in french"""
    galician: str
    """The language name in galician"""
    georgian: str
    """The language name in georgian"""
    german: str
    """The language name in german"""
    gujarati: str
    """The language name in gujarati"""
    haitian: str
    """The language name in haitian"""
    hebrew: str
    """The language name in hebrew"""
    hindi: str
    """The language name in hindi"""
    hungarian: str
    """The language name in hungarian"""
    icelandic: str
    """The language name in icelandic"""
    indonesian: str
    """The language name in indonesian"""
    irish: str
    """The language name in irish"""
    italian: str
    """The language name in italian"""
    japanese: str
    """The language name in japanese"""
    javanese: str
    """The language name in javanese"""
    kannada: str
    """The language name in kannada"""
    kazakh: str
    """The language name in kazakh"""
    khmer: str
    """The language name in khmer"""
    kirghiz: str
    """The language name in kirghiz"""
    korean: str
    """The language name in korean"""
    lao: str
    """The language name in lao"""
    latin: str
    """The language name in latin"""
    latvian: str
    """The language name in latvian"""
    lithuanian: str
    """The language name in lithuanian"""
    luxembourgish: str
    """The language name in luxembourgish"""
    macedonian: str
    """The language name in macedonian"""
    malagasy: str
    """The language name in malagasy"""
    malay: str
    """The language name in malay"""
    maltese: str
    """The language name in maltese"""
    maori: str
    """The language name in maori"""
    marathi: str
    """The language name in marathi"""
    moderngreek: str
    """The language name in moderngreek"""
    mongolian: str
    """The language name in mongolian"""
    nepali: str
    """The language name in nepali"""
    norwegian: str
    """The language name in norwegian"""
    panjabi: str
    """The language name in panjabi"""
    persian: str
    """The language name in persian"""
    polish: str
    """The language name in polish"""
    portuguese: str
    """The language name in portuguese"""
    romanian: str
    """The language name in romanian"""
    russian: str
    """The language name in russian"""
    scottishgaelic: str
    """The language name in scottishgaelic"""
    serbian: str
    """The language name in serbian"""
    sinhala: str
    """The language name in sinhala"""
    slovak: str
    """The language name in slovak"""
    slovenian: str
    """The language name in slovenian"""
    spanish: str
    """The language name in spanish"""
    sundanese: str
    """The language name in sundanese"""
    swahili: str
    """The language name in swahili"""
    swedish: str
    """The language name in swedish"""
    tagalog: str
    """The language name in tagalog"""
    tajik: str
    """The language name in tajik"""
    tamil: str
    """The language name in tamil"""
    telugu: str
    """The language name in telugu"""
    thai: str
    """The language name in thai"""
    turkish: str
    """The language name in turkish"""
    ukrainian: str
    """The language name in ukrainian"""
    urdu: str
    """The language name in urdu"""
    uzbek: str
    """The language name in uzbek"""
    vietnamese: str
    """The language name in vietnamese"""
    welsh: str
    """The language name in welsh"""
    xhosa: str
    """The language name in xhosa"""
    yiddish: str
    """The language name in yiddish"""
    zulu: str
    """The language name in zulu"""


LANGUAGE_CACHE = lru.LRUDictCache(512)
NULLABLE_ATTRIBUTES = ("alpha2", "alpha3b", "alpha3t", "extra", "foreign")


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

    def __init__(self, language: typing.Union[str, "Language", typing.Dict], threshold: int = 93) -> None:
        if isinstance(language, typing.Dict):
            super().__init__(language)
        elif isinstance(language, Language):
            self._cain_value = copy.copy(language._cain_value)
            try:
                self._rich = language._rich
            except AttributeError:
                pass
        else:
            results = self.search(language)
            if not results:
                raise exceptions.UnknownLanguage("N/A", 0,
                                                 "Couldn't find any corresponding language")
            result = results[0]
            if result.similarity < threshold:
                raising_message = f"Couldn't recognize the given translator ({language})\nDid you mean: {result.vector.string} (Similarity: {round(result.similarity, 2)}%)?"
                raise exceptions.UnknownLanguage(result, result.similarity, raising_message)

            try:
                self._cain_value = copy.copy(DATA["data"][result.vector.id]._cain_value)
                self._rich = True
            except KeyError:
                self._cain_value = {
                    "id": result.vector.id,
                    "alpha3": result.vector.id,
                    "name": result.vector.string
                }
                for attr in NULLABLE_ATTRIBUTES:
                    self._cain_value[attr] = None
                self._rich = False
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

    def __repr__(self) -> str:
        return f'Language({self.name})'

    def __str__(self) -> str:
        return self.id

    def __eq__(self, obj: typing.Union["Language", str]) -> bool:
        if isinstance(obj, str):
            obj = Language(obj)
        if not isinstance(obj, Language):
            return False
        return self.id == obj.id

    def __hash__(self) -> int:
        return hash(self.id)

    def get_extra(self, attribute: str) -> typing.Optional[str]:
        """Retrieves the given attribute from `extra` if available"""
        if not self.extra:
            return None
        try:
            return self.extra[attribute]
        except KeyError:
            return None

    def get_foreign(self, attribute: typing.Union[str, "Language"]) -> typing.Optional[str]:
        """Retrieves the given attribute from `foreign` if available"""
        if not self.foreign:
            return None
        if isinstance(attribute, Language):
            attribute = vectorize.string_preprocessing(attribute.name)
        try:
            return self.foreign[attribute]
        except KeyError:
            return None

    @property
    def similarity(self) -> float:
        """The similarity with the vector while searching the language"""
        return self._similarity

    @property
    def native(self) -> str:
        """The native name for the language or its english name"""
        return self.get_foreign(self) or self.name

    @property
    def rich(self) -> bool:
        """If the language discovery used the full translatepy dataset
        Note: This returns `False` if the `Language` was not fully initialized"""
        try:
            return self._rich
        except AttributeError:
            return False

# Internal Data


class LanguageData(typing.TypedDict):
    """Groups all of the data"""
    codes: typing.Dict[str, str]
    data: typing.Dict[str, Language]
    vectors: typing.List[vectorize.Vector]


# Load the data in memory
LANGUAGE_DATA_DIR = pathlib.Path(__file__).parent / "data" / "languages"
"""The directory where all of the data is stored"""

DATA = LanguageData({})  # type: ignore (will be filled later)
"""The languages in-memory data"""

with open(LANGUAGE_DATA_DIR / "codes.cain", "b+r") as f:
    DATA["codes"] = {key: value for key, value in cain.load(f, typing.List[typing.Tuple[str, str]])}

TRANSLATEPY_LANGUAGE_FULL = (to_bool(os.environ.get("TRANSLATEPY_LANGUAGE_FULL"))
                             and (LANGUAGE_DATA_DIR / "data_full.cain").is_file())
"""If the full language data database got loaded at runtime"""

with open(LANGUAGE_DATA_DIR / ("data_full.cain" if TRANSLATEPY_LANGUAGE_FULL
                               else "data.cain"), "b+r") as f:
    DATA["data"] = {value.id: value for value in cain.load(f, typing.List[Language])}


def load_full():
    """Loads the full data languages DB"""
    global TRANSLATEPY_LANGUAGE_FULL
    if TRANSLATEPY_LANGUAGE_FULL:
        return
    with open(LANGUAGE_DATA_DIR / "data_full.cain", "b+r") as f:
        DATA["data"] = {value.id: value for value in cain.load(f, typing.List[Language])}
    TRANSLATEPY_LANGUAGE_FULL = True


with open(LANGUAGE_DATA_DIR / "vectors.cain", "b+r") as f:
    DATA["vectors"] = cain.load(f, typing.List[vectorize.Vector])

# Defining common languages
COMMON_LANGUAGES = [
    Language("eng"),
    Language("sqi"),
    Language("twi"),
    Language("ara"),
    Language("hye"),
    Language("aze"),
    Language("eus"),
    Language("bel"),
    Language("dzo"),
    Language("bos"),
    Language("bul"),
    Language("mya"),
    Language("cat"),
    Language("zho"),
    Language("hrv"),
    Language("ces"),
    Language("dan"),
    Language("nld"),
    Language("fao"),
    Language("fin"),
    Language("fra"),
    Language("glg"),
    Language("kat"),
    Language("deu"),
    Language("guj"),
    Language("slv"),
    Language("heb"),
    Language("hin"),
    Language("hun"),
    Language("isl"),
    Language("ind"),
    Language("gle"),
    Language("ita"),
    Language("jpn"),
    Language("jav"),
    Language("kan"),
    Language("kaz"),
    Language("khm"),
    Language("kir"),
    Language("kor"),
    Language("lao"),
    Language("lat"),
    Language("lav"),
    Language("lit"),
    Language("ltz"),
    Language("mkd"),
    Language("mlg"),
    Language("msa"),
    Language("mlt"),
    Language("mri"),
    Language("mar"),
    Language("ell"),
    Language("mon"),
    Language("nep"),
    Language("nor"),
    Language("pan"),
    Language("fas"),
    Language("pol"),
    Language("por"),
    Language("ron"),
    Language("rus"),
    Language("gla"),
    Language("srp"),
    Language("sin"),
    Language("slk"),
    Language("slv"),
    Language("spa"),
    Language("sun"),
    Language("swa"),
    Language("swe"),
    Language("tgl"),
    Language("tgk"),
    Language("tsn"),
    Language("tel"),
    Language("tha"),
    Language("tur"),
    Language("ukr"),
    Language("urd"),
    Language("uzb"),
    Language("vie"),
    Language("cym"),
    Language("xho"),
    Language("yid"),
    Language("zul"),
    Language("epo")
]
"""All of the available foreign languages for the `foreign` field on the `Language` class and English"""
