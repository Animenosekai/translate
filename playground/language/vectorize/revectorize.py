from json import dumps
from re import compile

from translatepy.language import Language, Types
from translatepy.utils._language_data import LANGUAGE_DATA
from translatepy.utils.similarity import StringVector

LANGUAGE_CLEANUP_REGEX = compile("\(.+\)")
results = {}

def vectorize(string: str, data: Language):
    vector = StringVector(string)
    if len(vector.set) > 0:
        return {
            "i": data.id,
            "s": list(vector.set),
            "l": vector.length,
            "c": dict(vector.counter)
        }
    else:
        raise ValueError

for lang in LANGUAGE_DATA:
    l = Language(lang)
    if l.alpha2 is not None and l.extra.type in {Types.ANCIENT, Types.LIVING}:
        for _, name in l.in_foreign_languages.items():
            normalized_language = LANGUAGE_CLEANUP_REGEX.sub("", str(name).lower()).replace(" ", "")
            try:
                results[normalized_language] = vectorize(normalized_language, l)
            except Exception as e:
                print(e)
                continue

with open("vector_results.py", "w") as out:
    out.write(f"VECTORS = {dumps(results, ensure_ascii=False, separators=(',', ':')).replace('[', '{').replace(']', '}')}")