from translatepy.utils._language_cache import LANGUAGE_DATA, CODES
from translatepy.utils.similarity import StringVector
from json import dumps
from re import compile
from translatepy import Translate
from multiprocessing.pool import ThreadPool

t = Translate()
pool = ThreadPool(105)

to = ['af', 'am', 'ar', 'az', 'be', 'bg', 'bn', 'bs', 'ca', 'ceb', 'co', 'cs', 'cy', 'da', 'de', 'el', 'eo', 'es', 'et', 'eu', 'fa', 'fi', 'fr', 'fy', 'ga', 'gd', 'gl', 'gu', 'ha', 'haw', 'hi', 'hmn', 'hr', 'ht', 'hu', 'hy', 'id', 'ig', 'is', 'it', 'he', 'ja', 'jv', 'ka', 'kk', 'km', 'kn', 'ko', 'ku', 'ky', 'la', 'lb', 'lo', 'lt', 'lv', 'mg', 'mi', 'mk', 'ml', 'mn', 'mr', 'ms', 'mt', 'my', 'ne', 'nl', 'no', 'ny', 'or', 'pa', 'pl', 'ps', 'pt', 'ro', 'ru', 'sd', 'si', 'sk', 'sl', 'sm', 'sn', 'so', 'sq', 'sr', 'st', 'su', 'sv', 'sw', 'ta', 'te', 'tg', 'th', 'tl', 'tr', 'ug', 'uk', 'ur', 'uz', 'vi', 'xh', 'yi', 'yo', 'zh', 'zu']

regex = compile("\(.+\)")

results = {}
types = []
scopes = []
common = []
translations = 0
foreigns = 0

print("Loading the data")

for lang, data in LANGUAGE_DATA.items():
    results[lang] = {}

    if data["codes"]["alpha2"]:
        #print(data["english"])
        results[lang]["2"] = data["codes"]["alpha2"]

    if data["codes"]["alpha3"]["iso6392-b"]:
        results[lang]["b"] = data["codes"]["alpha3"]["iso6392-b"]

    if data["codes"]["alpha3"]["iso6392-t"]:
        results[lang]["t"] = data["codes"]["alpha3"]["iso6392-t"]

    if data["codes"]["alpha3"]["iso6393"]:
        results[lang]["3"] = data["codes"]["alpha3"]["iso6393"]
    else:
        print("no alpha3")

    if data["english"]:
        results[lang]["e"] = data["english"]
    else:
        print("no english")
    
    if data["foreign"] is not None and len(data["foreign"]) > 0:
        f = data["foreign"]
        f.pop("en", None)
        results[lang]["f"] = f
    
    if data["extra"] is not None and len(data["extra"]) > 0:
        results[lang]["x"] = {}
        scopes.append(data["extra"]["scope"])
        types.append(data["extra"]["type"])
        #if data["extra"]["type"] == "living" and data["extra"]["scope"] == "individual":
        #    print(data["english"])
        results[lang]["x"]["t"] = data["extra"]["type"]
        results[lang]["x"]["scope"] = data["extra"]["scope"]
    else:
        print("no extra")

def prepare(text: str):
    return regex.sub("", text.lower()).replace(" ", "")

def translate(data, l):
    print("translating missing", l, "for", data["e"])
    try:
        result = t.translate(data["e"], l, "eng").result
    except Exception:
        result = data["e"]
    print('result', result)
    vector = StringVector(result)
    return (
        l,
        prepare(vector.string),
        {
            "i": lang,
            "l": vector.length,
            "s": list(vector.set),
            "c": dict(vector.count)
        },
        result
    )

vectors = {}
for lang, data in results.items():
    if "2" in data:
        common.append(lang)
        vector = StringVector(data["e"])
        vectors[prepare(vector.string)] = {
            "i": lang,
            "l": vector.length,
            "s": list(vector.set),
            "c": dict(vector.count)
        }
        if "f" in data:
            print(sorted(set(data["f"].keys())))
            lang_to = to.copy()
            for k in data["f"].copy():
                if k == "jw":
                    k = "jv"
                    data["f"][k] = data["f"].pop("jw", None)
                if k == "iw":
                    k = "he"
                    data["f"][k] = data["f"].pop("iw", None)
                if k == "zh-cn":
                    k = "zh"
                    data["f"][k] = data["f"].pop("zh-cn", None)
                try:
                    lang_to.remove(k)
                except Exception:
                    print(k, "does not exist in wanted dataset")
                    data["f"].pop(k, None)
                    continue
                vector = StringVector(data["f"][k])
                vectors[prepare(vector.string)] = {
                    "i": lang,
                    "l": vector.length,
                    "s": list(vector.set),
                    "c": dict(vector.count)
                }
                
            print("missing", lang_to)
            out = pool.starmap(translate, [(data, l) for l in lang_to])
            for r in out:
                l, key, d, tr = r
                data["f"][l] = tr
                vectors[key] = d
        else:
            print("alpha2 but no foreign", lang)
            data["f"] = {}
            out = pool.starmap(translate, [(data, l) for l in to])
            for r in out:
                l, key, d, tr = r
                data["f"][l] = tr
                vectors[key] = d

#StringVector()

with open("results.py", "w") as out:
    out.write(f"LANGUAGE_DATA = {dumps(results, separators=(',', ':'), ensure_ascii=False)}\nCODES = {dumps(CODES, separators=(',', ':'), ensure_ascii=False)}\nVECTORS = {dumps(vectors, separators=(',', ':'), ensure_ascii=False).replace('[', '{').replace(']', '}')}")

print("Scopes:", sorted(set(scopes)))
print("Types:", sorted(set(types)))
print("Common:", sorted(set(common)))
print("Translations:", translations)
print("Foreigns:", foreigns)
print("Length:", len(results))