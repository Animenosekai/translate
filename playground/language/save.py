from safeIO import JSONFile, TextFile
from translatepy.language import Language
from translatepy import Translator
from multiprocessing.pool import ThreadPool
from translatepy.utils.similarity import StringVector

#PROXIES = TextFile("http_proxies-2.txt").readlines()
#t = Translator(request=Request(PROXIES))
t = Translator()

CODES = ["af","sq","am","ar","hy","az","eu","be","bn","bs","bg","ca","ceb","ny","zh-cn","co","hr","cs","da","nl","en","eo","et","tl","fi","fr","fy","gl","ka","de","el","gu","ht","ha","haw","iw","hi","hmn","hu","is","ig","id","ga","it","ja","jw","kn","kk","km","rw","ko","ku","ky","lo","la","lv","lt","lb","mk","mg","ms","ml","mt","mi","mr","mn","my","ne","no","or","ps","fa","pl","pt","pa","ro","ru","sm","gd","sr","st","sn","sd","si","sk","sl","so","es","su","sw","sv","tg","ta","tt","te","th","tr","tk","uk","ur","ug","uz","vi","cy","xh","yi","yo","zu","zh-tw"]
TRANSLATION_POOL = ThreadPool(110)
PROCESSING_POOL = ThreadPool(3000)

data = JSONFile("iso.json").read()
translation = JSONFile("data.json").read()

csv_data = []
for details in TextFile("iso639.csv"):
    detail = [word.replace("\n", "") for word in details.split(",")]
    csv_data.append({
        "alpha3-b": detail[0],
        "alpha3-t": detail[1],
        "alpha2": detail[2],
        "english": detail[3],
        "yandex": detail[4],
        "google": detail[5],
        "bing": detail[6],
        "reverso": detail[7],
        "deepl": detail[8]
    })

TRANSLATION_COUNT = 0
def translate(text, destination, output):
    global TRANSLATION_COUNT
    print("Translation Count", str(TRANSLATION_COUNT))
    try:
        TRANSLATION_COUNT += 1
        output[destination] = t.translate(text, destination, "English").result
    except Exception:
        try:
            TRANSLATION_COUNT += 1
            output[destination] = t.translate(text, destination, "English").result
        except Exception:
            try:
                TRANSLATION_COUNT += 1
                output[destination] = t.translate(text, destination, "English").result
            except Exception:
                pass



results = {}
yandex = {}
google = {}
bing = {}
reverso = {}
deepl = {}
codes = {}
vectors = {}

for language_data in data:
    print("Processing", language_data["name"])

    # getting the current data
    try:
        current = Language(language_data["iso6392B"])
    except:
        current = None
    
    # getting the foreign languages translation
    tr = {}
    if (language_data["iso6391"] if "iso6391" in language_data else None) in translation:
        tr = translation[language_data["iso6391"]]
    elif current is not None:
        tr = current.language.in_foreign_languages
    else:
        #TRANSLATION_POOL.starmap(translate, [(language_data["name"], code, tr) for code in CODES])
        # I stopped after being at my 45000's translation, because Google just rate limited my VPN IP + it wasn't even half way through
        pass

    results[language_data["iso6393"]] = {
        "codes": {
            "alpha2": (language_data["iso6391"] if "iso6391" in language_data else None),
            "alpha3": {
                "iso6392-b": (language_data["iso6392B"] if "iso6392B" in language_data else None),
                "iso6392-t": (language_data["iso6392T"] if "iso6392T" in language_data else None),
                "iso6393": language_data["iso6393"]
            }
        },
        "english": language_data["name"],
        "foreign": tr,
        "extra": {
            "type": language_data["type"],
            "scope": language_data["scope"]
        }
    }

    resulting_data = results[language_data["iso6393"]]



    # extracting services data
    csv_result = None
    for _data in csv_data:
        if resulting_data["english"] == _data["english"]:
            csv_result = _data
            break
        elif resulting_data["codes"]["alpha2"] == _data["alpha2"]:
            csv_result = _data
            break
        elif resulting_data["codes"]["alpha3"]["iso6392-b"] == _data["alpha3-b"]:
            csv_result = _data
            break
        elif resulting_data["codes"]["alpha3"]["iso6392-t"] == _data["alpha3-t"]:
            csv_result = _data
            break
        elif resulting_data["codes"]["alpha3"]["iso6393"] == _data["alpha3-b"]:
            csv_result = _data
            break
        elif resulting_data["codes"]["alpha3"]["iso6393"] == _data["alpha3-t"]:
            csv_result = _data
            break

    if csv_result is not None:
        if csv_result["yandex"] != "":
            yandex[language_data["iso6393"]] = csv_result["yandex"]
        if csv_result["google"] != "":
            google[language_data["iso6393"]] = csv_result["google"]
        if csv_result["bing"] != "":
            bing[language_data["iso6393"]] = csv_result["bing"]
        if csv_result["reverso"] != "":
            reverso[language_data["iso6393"]] = csv_result["reverso"]
        if csv_result["deepl"] != "":
            deepl[language_data["iso6393"]] = csv_result["deepl"]

    if resulting_data["codes"]["alpha2"] is not None:
        codes[resulting_data["codes"]["alpha2"]] = language_data["iso6393"]

    if resulting_data["codes"]["alpha3"]["iso6392-b"] is not None:
        codes[resulting_data["codes"]["alpha3"]["iso6392-b"]] = language_data["iso6393"]

    if resulting_data["codes"]["alpha3"]["iso6392-t"] is not None:
        codes[resulting_data["codes"]["alpha3"]["iso6392-t"]] = language_data["iso6393"]

    if resulting_data["codes"]["alpha3"]["iso6393"] is not None:
        codes[resulting_data["codes"]["alpha3"]["iso6393"]] = language_data["iso6393"]

    # vectorize
    name = resulting_data["english"].lower().replace(" ", "")
    current_vector = StringVector(name)
    vectors[name] = {
        "id": language_data["iso6393"],
        "set": list(current_vector.set),
        "length": current_vector.length,
    }
    for language in resulting_data["foreign"]:
        current_vector = StringVector(resulting_data["foreign"][language])
        name = resulting_data["foreign"][language].lower().replace(" ", "")
        current_vector = StringVector(name)
        vectors[name] = {
            "id": language_data["iso6393"],
            "set": list(current_vector.set),
            "length": current_vector.length,
        }


results["emj"] = {
    "codes": {
        "alpha2": None,
        "alpha3": {
            "iso6392-b": None,
            "iso6392-t": None,
            "iso6393": None
        }
    },
    "english": "Emoji",
    "foreign": {},
    "extra": {
        "type": "living",
        "scope": "special"
    }
}

name = "Emoji".lower().replace(" ", "")
current_vector = StringVector(name)
vectors[name] = {
    "id": language_data["iso6393"],
    "set": list(current_vector.set),
    "length": current_vector.length,
}
    

JSONFile("YANDEX_RESULTS.json", minify=True).write(yandex)
JSONFile("GOOGLE_RESULTS.json", minify=True).write(google)
JSONFile("BING_RESULTS.json", minify=True).write(bing)
JSONFile("REVERSO_RESULTS.json", minify=True).write(reverso)
JSONFile("DEEPL_RESULTS.json", minify=True).write(deepl)
JSONFile("CODES_RESULTS.json", minify=True).write(codes)
JSONFile("VECTORS_RESULTS.json", minify=True).write(vectors)

JSONFile("LANGUAGES_RESULTS.json", minify=True).write(results)