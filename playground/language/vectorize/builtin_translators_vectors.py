import json

from nasse.logging import LogLevels, log
from translatepy import Translator
from translatepy.language import LANGUAGE_CLEANUP_REGEX
from translatepy.utils.sanitize import remove_spaces
from translatepy.utils.similarity import StringVector

results = {}
try:
    with open("translation_results.json") as f:
        results = json.load(f)
except Exception:
    pass

"""
to = ['af', 'am', 'ar', 'az', 'be', 'bg', 'bn', 'bs', 'ca', 'ceb', 'co', 'cs', 'cy', 'da', 'de', 'el', 'eo', 'es', 'et', 'eu', 'fa', 'fi', 'fr', 'fy', 'ga', 'gd', 'gl', 'gu', 'ha', 'haw', 'hi', 'hmn', 'hr', 'ht', 'hu', 'hy', 'id', 'ig', 'is', 'it', 'he', 'ja', 'jv', 'ka', 'kk', 'km', 'kn', 'ko', 'ku', 'ky', 'la', 'lb', 'lo', 'lt', 'lv', 'mg', 'mi', 'mk', 'ml', 'mn', 'mr', 'ms', 'mt', 'my', 'ne', 'nl', 'no', 'ny', 'or', 'pa', 'pl', 'ps', 'pt', 'ro', 'ru', 'sd', 'si', 'sk', 'sl', 'sm', 'sn', 'so', 'sq', 'sr', 'st', 'su', 'sv', 'sw', 'ta', 'te', 'tg', 'th', 'tl', 'tr', 'ug', 'uk', 'ur', 'uz', 'vi', 'xh', 'yi', 'yo', 'zh', 'zu']

translators = {
    "GoogleTranslate": [
        "Google",
        "Google Translate",
        "Google Translate API",
        "Google Translator"
    ],
    "GoogleTranslateV1": [
        "Google Translate V1",
        "Google Translate V1 API",
        "Google Translate API V1",
    ],
    "GoogleTranslateV2": [
        "Google Translate V2",
        "Google Translate V2 API",
        "Google Translate API V2",
    ],
    "MicrosoftTranslate": [
        "Microsoft",
        "Microsoft Translator",
        "Microsoft Translator API",
        "Microsoft Translate"
    ],
    "YandexTranslate": [
        "Yandex",
        "Yandex Translate",
        "Yandex Translator",
        "Yandex Translator API"
    ],
    "LibreTranslate": [
            "Libre",
            "Libre Translate",
            "Libre Translator",
        "Libre Translator API"
    ],
    "BingTranslate": [
        "Bing",
        "Bing Translate",
        "Bing Translator",
        "Bing Translator API"
    ],
    "DeeplTranslate": [
        "Deepl",
        "Deepl Translate",
        "Deepl Translator",
        "Deepl Translator API"
    ],
    "MyMemoryTranslate": [
        "MyMemory",
        "MyMemory Translate",
        "MyMemory Translator",
        "MyMemory Translator API"
    ],
    "ReversoTranslate": [
        "Reverso",
        "Reverso Translate",
        "Reverso Translator",
        "Reverso Translator API"
    ],
    "TranslateComTranslate": [
        "Translate.com",
        "Translate.com Translate",
        "Translate.com Translator",
        "Translate.com Translator API"
        "Translatecom",
        "Translatecom Translate",
        "Translatecom Translator",
        "Translatecom Translator API"
    ]
}


t = Translator()

log("Translating vectors")
for translator, aliases in translators.items():
    log("Current Translator: " + translator)
    current_results = aliases.copy()
    for alias in aliases:
        log("   Current Alias: " + alias)
        for lang in to:
            log("       Current Language: " + lang, end="\r")
            try:
                result = t.translate(alias, lang, "English").result
                current_results.append(result)
                log(f"       Current Language: {lang} — {result}", end="\r")
            except Exception:
                print("")
                log(f"       An error occured while translating {alias} to {lang}", LogLevels.WARNING, end="\r")
            print("")
        results[translator] = list(set(current_results))
        with open("translation_results.json", "w") as f:
            json.dump(results, f, ensure_ascii=False, indent=4)
"""


log("Vectorizing")
string_results = {}
for translator, aliases in results.items():
    log("Current Translator: " + translator)
    for alias in aliases:
        log("   Current Alias: " + alias)
        normalized = remove_spaces(LANGUAGE_CLEANUP_REGEX.sub("", alias.lower()))
        vector = StringVector(normalized)
        string_results[alias] = {
            "s": list(vector.set),
            "l": vector.length,
            "c": dict(vector.counter),
            "t": translator
        }
    with open("vectors_results.json", "w") as f:
        json.dump(string_results, f, ensure_ascii=False, separators=(",", ":"))
