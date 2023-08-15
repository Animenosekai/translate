import cain
import typing
from translatepy.utils.vectorize import string_preprocessing, vectorize, Vector
from translatepy.language import Language, LANGUAGE_DATA_DIR, LanguageExtra, Foreign
from backup._language_data import LANGUAGE_DATA, CODES, VECTORS

languages = {
    element: string_preprocessing(LANGUAGE_DATA[CODES[element]]["e"])
    for element in ['af', 'sq', 'am', 'ar', 'hy', 'az', 'eu', 'ba', 'be', 'bn', 'bs', 'bg', 'ca', 'cv', 'ceb', 'ny', 'co',
                    'hr', 'cs', 'da', 'nl', 'eo', 'et', 'tl', 'fi', 'fr', 'fy', 'gl', 'ka', 'de', 'el', 'gu',
                    'ht', 'ha', 'haw', 'hi', 'hmn', 'hu', 'is', 'ig', 'id', 'ga', 'it', 'ja', 'kn', 'kk', 'km',
                    'ko', 'ku', 'ky', 'lo', 'la', 'lv', 'lt', 'lb', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mn',
                    'my', 'ne', 'no', 'or', 'ps', 'fa', 'pl', 'pt', 'pa', 'ro', 'ru', 'sm', 'gd', 'sr', 'st', 'sn', 'sd',
                    'si', 'sk', 'sl', 'so', 'es', 'su', 'sw', 'sv', 'tg', 'ta', 'te', 'th', 'tr', 'tt', 'uk', 'ur', 'ug', 'uz',
                    'vi', 'cy', 'xh', 'yi', 'yo', 'zu', 'zh', 'he', 'jv']
}

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

    if val.get("f"):
        data = {}
        for value in languages.values():
            data[value] = None
        for lang, value in val["f"].items():
            data[languages[lang]] = value
        foreign = Foreign(data)
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
    results.append(result)

with open(LANGUAGE_DATA_DIR / "data.cain", "b+w") as f:
    cain.dump(results, f, typing.List[Language])

# Vectors

results = []

for key, value in VECTORS.items():
    results.append(vectorize(value["i"], key))

with open(LANGUAGE_DATA_DIR / "vectors.cain", "b+w") as f:
    cain.dump(results, f, typing.List[Vector])

# Codes

results = []

for key, value in CODES.items():
    results.append((key, value))

with open(LANGUAGE_DATA_DIR / "codes.cain", "b+w") as f:
    cain.dump(results, f, typing.List[typing.Tuple[str, str]])
