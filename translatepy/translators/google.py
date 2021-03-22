from typing import Union
from requests import get
from json import loads
from urllib.parse import quote
from traceback import print_exc

from translatepy.utils.gtoken import TokenAcquirer
from translatepy.utils.annotations import Tuple
from translatepy.utils.utils import convert_to_float

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
}

class GoogleTranslate():
    """A Python implementation of Google Translate's APIs"""
    def __init__(self) -> None:
        try:
            self.token_acquirer = TokenAcquirer()
        except:
            self.token_acquirer = None

    def translate(self, text, destination_language, source_language="auto") -> Union[Tuple[str, str], Tuple[None, None]]:
        """
        Translates the given text to the given language

        Args:
          text: param destination_language:
          source_language: Default value = "auto")
          destination_language: 

        Returns:
            Tuple(str, str) --> tuple with source_lang, translation
            None, None --> when an error occurs

        """
        try:
            text = quote(str(text), safe='')
            if source_language is None:
                source_language = "auto"
            request = get("https://translate.googleapis.com/translate_a/single?client=gtx&dt=t&sl=" + str(source_language) + "&tl=" + str(destination_language) + "&q=" + text)
            if request.status_code < 400:
                data = loads(request.text)
                return data[2], "".join([sentence[0] for sentence in data[0]])
            else:
                request = get("https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=" + str(source_language) + "&tl=" + str(destination_language) + "&q=" + text, headers=HEADERS)
                if request.status_code < 400:
                    data = loads(request.text)
                    try:
                        return data['ld_result']["srclangs"][0], "".join((sentence["trans"] if "trans" in sentence else "") for sentence in data["sentences"])
                    except:
                        return data[0][0][2], "".join(sentence for sentence in data[0][0][0][0])
                else:
                    return None, None
        except:
            return None, None

    def transliterate(self):
        """Transliterates the given text"""
        raise NotImplementedError

    def define(self):
        """Returns the definition of the given word"""
        raise NotImplementedError

    def text_to_speech(self, text, source_language=None, speed=1):
        """
        Gives back the text to speech result for the given text

        Args:
          text:

        Returns:
            bytes --> the mp3 file as bytes
            None --> when an error occurs

        !! Currently doesn't seem to work well because of the Token Generation methods.
            > Please refer to #234@ssut/py-googletrans if you have any problem
        """
        try:
            if self.token_acquirer is None:
                return None
            text = str(text)
            textlen = len(text)
            token = self.token_acquirer.do(text)
            if token is None:
                return None
            if source_language is None:
                source_language = self.language(text)
                if source_language is None:
                    return None
            text = quote(str(text), safe='')
            request = get("https://translate.google.com/translate_tts?ie=UTF-8&q=" + text + "&tl=" + source_language + "&total=1&idx=0&textlen=" + textlen + "&tk=" + str(token) + "&client=webapp&prev=input&ttsspeed=" + str(convert_to_float(speed)))
            if request.status_code < 400:
                return request.content
            else:
                return None
        except:
            print_exc()
            return None

    def language(self, text) -> Union[str, None]:
        """
        Gives back the language of the given text

        Args:
          text: 

        Returns:
            str --> the language code
            None --> when an error occurs

        """
        try:
            text = quote(str(text), safe='')
            request = get("https://translate.googleapis.com/translate_a/single?client=gtx&dt=t&sl=auto&tl=ja&q=" + text)
            if request.status_code < 400:
                return loads(request.text)[2]
            else:
                request = get("https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=auto&tl=ja&q=" + text, headers=HEADERS)
                if request.status_code < 400:
                    return loads(request.text)['ld_result']["srclangs"][0]
                else:
                    return None
        except:
            return None

    def __repr__(self) -> str:
        return "Google Translate"
