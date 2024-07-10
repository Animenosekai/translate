"""transforms the previous database to dot paths only"""
import typing
import cain
from translatepy.utils import importer, vectorize

IDS = {
    "translatecomtranslate": "translatepy.translators.translatecom.TranslateComTranslate",
    "deepltranslate": "translatepy.translators.deepl.DeeplTranslate",
    "mymemorytranslate": "translatepy.translators.mymemory.MyMemoryTranslate",
    "googletranslate": "translatepy.translators.google.GoogleTranslate",
    "microsofttranslate": "translatepy.translators.microsoft.MicrosoftTranslate",
    "yandextranslate": "translatepy.translators.yandex.YandexTranslate",
    "reversotranslate": "translatepy.translators.reverso.ReversoTranslate",
    "libretranslate": "translatepy.translators.libre.LibreTranslate",
    "bingtranslate": "translatepy.translators.bing.BingTranslate"
}

for translator in IDS.values():
    importer.translator_from_path(translator)

vectors = []
for vector in importer.IMPORTER_VECTORS:
    id = IDS.get(vector.id)
    if not id:
        continue
    vectors.append(vectorize.vectorize(id=id, string=vector.string))

with (importer.IMPORTER_DATA_FILE).open("wb") as f:
    cain.dump(vectors, f, typing.List[vectorize.Vector])
