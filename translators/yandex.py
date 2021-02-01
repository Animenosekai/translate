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


class YandexTranslate():
    """
    A Python implementation of Yandex Translation's APIs
    """
    def __init__(self) -> None:
        self._base_url = "https://translate.yandex.net/api/v1/tr.json/translate"
        self._id = "1308a84a.6016deed.0c4881a2.74722d74657874-3-0"

    def translate(self, text, destination_language, source_language="auto"):
        """
        Translates the given text to the given language
        """
        try:
            if source_language is None:
                source_language = "auto"
            url = "?id=" + self._id + "&srv=tr-text&lang=" + str(destination_language) +"&reason=" + str(source_language) + "&format=text"
            request = get(url, headers=HEADERS, data={'text': str(text), 'options': '4'})
            if request.status_code < 400 and request.json()["code"] == 200:
                return loads(request.text)["text"][0]
            else:
                return None
        except:
            return None

    def transliterate():
        """
        Transliterates the given text
        """
        pass

    def define():
        """
        Returns the definition of the given word
        """
        pass

    def language():
        """
        Gives back the language of the given text
        """
        pass