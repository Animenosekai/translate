from translatepy import Language


def test_language():
    print("[test] --> Testing translatepy.Language")
    assert Language("French").alpha2 == "fr"
    assert Language("Japanese").alpha2 == "ja"
    assert Language("en").name.lower() == "english"
    assert Language("japanese").alpha2 == "ja"
    assert Language("自动").name.lower() == "automatic"
