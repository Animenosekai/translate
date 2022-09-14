import pytest

from translatepy.exceptions import UnknownTranslator
from translatepy.translators import GoogleTranslate, YandexTranslate
from translatepy.utils.importer import get_translator


def test_importer():
    print("[test] --> Testing translatepy.utils.importer")
    assert get_translator("GoogleTranslate") == GoogleTranslate
    assert get_translator("グーグル") == GoogleTranslate
    assert get_translator("yandex") == YandexTranslate
    assert get_translator("translatepy.translators.google.GoogleTranslate") == GoogleTranslate
    assert get_translator("translatepy.translators.yandex.YandexTranslate") == YandexTranslate

    with pytest.raises(UnknownTranslator):
        get_translator("AAAAAAAAA")
