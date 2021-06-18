from safeIO import JSONFile
from safeIO.safeIO import TextFile
from translatepy.language import Language

data = JSONFile("data.json").read()
csv_data = []
for details in TextFile("iso639.csv"):
    detail = details.split(",")
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

results = []
for code in data:
    language = Language(code)
    results.append({
        "codes": {
            "alpha2": code,
            "alpha3": {
                "b": "",
                "t": ""
            }
        },
        "english": "",
        "foreign": {
            ""
        },
        "id": ""
    })