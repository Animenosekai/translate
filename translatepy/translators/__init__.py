from translatepy.translators.base import BaseTranslator

from translatepy.translators.bing import BingTranslate
from translatepy.translators.deepl import DeeplTranslate
from translatepy.translators.google import (GoogleTranslate, GoogleTranslateV1,
                                            GoogleTranslateV2)
from translatepy.translators.libre import LibreTranslate
from translatepy.translators.mymemory import MyMemoryTranslate
from translatepy.translators.reverso import ReversoTranslate
from translatepy.translators.translatecom import TranslateComTranslate
from translatepy.translators.yandex import YandexTranslate
from translatepy.translators.microsoft import MicrosoftTranslate

from translatepy.translators.qcri import QCRI
from translatepy.translators.pons import PONS
from translatepy.translators.papago import Papago


# aliases

Reverso = ReversoTranslate
Bing = BingTranslate
DeepL = DeeplTranslate
Deepl = DeeplTranslate
Google = GoogleTranslate
Libre = LibreTranslate
MyMemory = MyMemoryTranslate
TranslateCom = TranslateComTranslate
Yandex = YandexTranslate
Microsoft = MicrosoftTranslate

QCRITranslate = QCRI
PONSTranslate = PONS
PapagoTranslate = Papago
NaverTranslate = Papago
