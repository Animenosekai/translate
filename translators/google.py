from requests import get
from json import loads

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
}

class GoogleTranslate():
    """
    A Python implementation of Google Translate's APIs
    """
    def __init__(self) -> None:
        pass

    def translate(self, text, destination_language, source_language="auto"):
        """
        Translates the given text to the given language
        """
        try:
            if source_language is None:
                source_language = "auto"
            request = get("https://translate.googleapis.com/translate_a/single?client=gtx&dt=t&sl=" + str(source_language) + "&tl=" + str(destination_language) + "&q=" + str(text))
            if request.status_code < 400:
                return loads(request.text)[0][0][0]
            else:
                request = get("https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=" + str(source_language) + "&tl=" + str(destination_language) + "&q=" + str(text), headers=HEADERS)
                if request.status_code < 400:
                    return loads(request.text)['alternative_translations'][0]['alternative'][0]['word_postproc']
                else:
                    return None
        except:
            return None

    def transliterate():
        """
        Transliterates the given text
        """
        raise NotImplementedError

    def define():
        """
        Returns the definition of the given word
        """
        raise NotImplementedError

    def language(self, text):
        """
        Gives back the language of the given text
        """
        try:
            request = get("https://translate.googleapis.com/translate_a/single?client=gtx&dt=t&sl=auto&tl=ja&q=" + str(text))
            if request.status_code < 400:
                return loads(request.text)[2]
            else:
                request = get("https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=auto&tl=ja&q=" + str(text), headers=HEADERS)
                if request.status_code < 400:
                    return loads(request.text)['ld_result']["srclangs"][0]
                else:
                    return None
        except:
            return None