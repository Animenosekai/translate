from json import loads
from requests import post

HEADERS = {
    "Host": "www.bing.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Referer": "https://www.bing.com/",
    "Content-Type": "application/x-www-form-urlencoded",
    "Connection": "keep-alive"
}
PARAMS = {'IG' : '839D27F8277F4AA3B0EDB83C255D0D70', 'IID' : 'translator.5033.3'}

class BingTranslate():
    """
    A Python implementation of Microsoft Bing Translation's APIs
    """
    def __init__(self) -> None:
        pass

    def translate(self, text, destination_language, source_language="auto-detect"):
        """
        Translates the given text to the given language
        """
        try:
            if source_language is None:
                source_language = "auto-detect"
            request = post("https://www.bing.com/ttranslatev3", headers=HEADERS, params=PARAMS, data={'text': str(text), 'fromLang': str(source_language), 'to': str(destination_language)})
            if request.status_code < 400:
                return loads(request.text)[0]["translations"][0]["text"]
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