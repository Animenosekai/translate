"""
migrate.py

Migrates the v2 data into cain encoded v3 data
"""

import typing

import cain
from rich.console import Console

from backup._language_data import CODES, LANGUAGE_DATA, VECTORS
from backup._importer_data import VECTORS as IMPORTER_VECTORS
# from translatepy.utils.importer import IMPORTER_DATA_DIR
from translatepy.language import (LANGUAGE_DATA_DIR, Foreign, Language,
                                  LanguageExtra)
from translatepy.utils.vectorize import Vector, string_preprocessing, vectorize

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
Console().print(list(sorted(parsing_languages.values())))

results = []
for key, val in LANGUAGE_DATA.items():
    ext = val.get("x", {})

    if ext.get("t") and ext.get("scope"):
        extra = LanguageExtra({
            "type": str(ext["t"]),
            "scope": str(ext["scope"])
        })
    else:
        extra = None

    if "f" in val:
        foreign = Foreign({language: val["f"][lang] for lang, language in parsing_languages.items()})
    else:
        foreign = None

    result = Language({
        "id": key,
        "alpha3": val["3"],
        "name": val["e"],
        "alpha2": val.get("2"),
        "alpha3b": val.get("b"),
        "alpha3t": val.get("t"),
        "extra": extra,
        "foreign": foreign
    })
    # print(result)
    results.append(result)

with open(LANGUAGE_DATA_DIR / "data.cain", "b+w") as f:
    cain.dump(results, f, typing.List[Language])

# Vectors

results = []

for key, value in VECTORS.items():
    results.append(vectorize(value["i"], key))

with open(LANGUAGE_DATA_DIR / "vectors.cain", "b+w") as f:
    cain.dump(results, f, typing.List[Vector])

results = []

for key, value in IMPORTER_VECTORS.items():
    results.append(vectorize(string_preprocessing(value["t"]), key))

with open(LANGUAGE_DATA_DIR.parent / "translators" / "vectors.cain", "b+w") as f:
    cain.dump(results, f, typing.List[Vector])

# Codes

results = []

for key, value in CODES.items():
    results.append((key, value))

with open(LANGUAGE_DATA_DIR / "codes.cain", "b+w") as f:
    cain.dump(results, f, typing.List[typing.Tuple[str, str]])
