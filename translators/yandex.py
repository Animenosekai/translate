from json import loads
from requests import get


HEADERS = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "translate.yandex.com",
    "Referer": "https://translate.yandex.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"
}

TRANSLIT_LANGS = [
    "am",
    "bn",
    "el",
    "gu",
    "he",
    "hi",
    "hy",
    "ja",
    "ka",
    "kn",
    "ko",
    "ml",
    "mr",
    "ne",
    "pa",
    "si",
    "ta",
    "te",
    "th",
    "yi",
    "zh"
]


class YandexTranslate():
    """
    A Python implementation of Yandex Translation's APIs
    """
    def __init__(self) -> None:
        self._base_url = "https://translate.yandex.net/api/v1/tr.json/"
        self._id = "1308a84a.6016deed.0c4881a2.74722d74657874-3-0"
        data = get("https://translate.yandex.com/", headers=HEADERS).text
        print(data)
        print(data.find("SID:"))
        data = data[data.find("SID: '"):]
        self._sid = data[:data.find("',")]


    def translate(self, text, destination_language, source_language="auto"):
        """
        Translates the given text to the given language
        """
        try:
            if source_language is None:
                source_language = "auto"
            url = self._base_url + "translate?id=" + self._id + "&srv=tr-text&lang=" + str(destination_language) +"&reason=" + str(source_language) + "&format=text"
            request = get(url, headers=HEADERS, data={'text': str(text), 'options': '4'})
            if request.status_code < 400 and request.json()["code"] == 200:
                return loads(request.text)["text"][0]
            else:
                return None
        except:
            return None

    def transliterate(self, text, source_language=None):
        """
        Transliterates the given text
        """
        try:
            if source_language is None:
                source_language = self.language(text)
                if source_language is None or source_language not in TRANSLIT_LANGS:
                    return None
            request = get("https://translate.yandex.net/translit/translit?sid=" + self._sid + "&srv=tr-text", headers=HEADERS, data={'text': str(text), 'lang': source_language})
            if request.status_code < 400:
                return request.text
            else:
                return None
        except:
            return None

    def spellcheck(self, text, source_language=None):
        """
        Spell checks the given text
        """
        try:
            if source_language is None:
                source_language = self.language(text)
                if source_language is None:
                    return None
            request = get("https://speller.yandex.net/services/spellservice.json/checkText?sid=" + self._sid + "&srv=tr-text", headers=HEADERS, data={'text': str(text), 'lang': source_language, 'options': 516})
            if request.status_code < 400:
                data = loads(request.text)
                for correction in data:
                    text = text[:correction.get("pos", 0)] + correction.get("s", [""])[0] + text[correction.get("pos", 0) + correction.get("len", 0):]
                return text
            else:
                return None
        except:
            return None

    def language(self, text, hint=None):
        """
        Gives back the language of the given text
        """
        try:
            if hint is None:
                hint = "en,ja"
            url = self._base_url + "detect?sid=" + self._sid + "&srv=tr-text&text=" + str(text) + "&options=1&hint=" + str(hint)
            request = get(url, headers=HEADERS)
            if request.status_code < 400 and request.json()["code"] == 200:
                return loads(request.text)["lang"]
            else:
                print(request.status_code)
                print(request.json())
                print(self._sid)
                return None
        except:
            return None