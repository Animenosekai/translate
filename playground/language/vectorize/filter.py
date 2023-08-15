"""filter.py

Generates the limited dataset
"""
import typing

import cain

from backup._language_data import CODES, LANGUAGE_DATA
from translatepy.language import LANGUAGE_DATA_DIR, Language
from translatepy.utils.vectorize import string_preprocessing

languages = set()
for id, val in LANGUAGE_DATA.items():
    languages.add(id)
    for attr in ("3", "e", "2", "b", "t"):
        if val.get(attr):
            languages.add(val.get(attr))


parsing_languages = languages.copy()
for val in LANGUAGE_DATA.values():
    for lang in languages:
        if "f" not in val:
            continue
        if not val["f"].get(lang) and lang in parsing_languages:
            parsing_languages.remove(lang)

parsing_languages = {element: string_preprocessing(LANGUAGE_DATA[CODES[element]]["e"]) for element in parsing_languages}

results = [Language(lang) for lang in parsing_languages]
with open(LANGUAGE_DATA_DIR / "data.cain", "w+b") as f:
    cain.dump(results, f, typing.List[Language])
