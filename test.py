import translatepy

t = translatepy.Translator()

def test_translate():
    print("[test] --> Testing Translator.translate")
    assert t.translate("Hello", "Japanese", "French") is not None
    assert t.translate("", "Japanese", "French") is None
    assert t.translate("    ", "Japanese", "French") is None
    assert t.translate("Hello", "French", "Japanese") is not None
    assert t.translate("Hello", "ja", "fr") is not None

def test_language():
    print("[test] --> Testing Translator.language")
    assert t.language("Hello") is not None
    
def test_Language():
    print("[test] --> Testing translatepy.Language")
    assert translatepy.Language("French").language == "fr"
    assert translatepy.Language("Japanese").language == "ja"
    assert translatepy.Language("en").language == "en"
    assert translatepy.Language("japanese").language == "ja"
    assert translatepy.AUTOMATIC.japanese == "自動"


def test_spellcheck():
    print("[test] --> Testing Translator.spellcheck")
    assert t.spellcheck("Hello") is not None
    assert t.spellcheck("God morning") is not None

def test_example():
    print("[test] --> Testing Translator.example")
    assert t.example("Hello", "japanese") is not None

def test_dictionary():
    print("[test] --> Testing Translator.dictionary")
    #assert t.dictionary("Hello", "Japanese") is not None
    # I can't test dictionary as DeepL is very strict on their rate-limit

def test_imports():
    print("[test] --> Testing imports")
    from translatepy.data import data
    from translatepy.models import exceptions
    from translatepy.models import languages
    from translatepy.translators import bing
    from translatepy.translators import deepl
    from translatepy.translators import google
    from translatepy.translators import reverso
    from translatepy.translators import unselected
    from translatepy.translators import yandex
    from translatepy.utils import annotations
    from translatepy.utils import similarity
    from translatepy import translate
    import translatepy

def test_yandex_sid():
    print("[test] --> Testing Translator.yandex_translate._sid")
    t = translatepy.Translator()
    assert t.yandex_translate._sid == translatepy.Translator().yandex_translate._sid