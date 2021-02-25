from time import time
from json import loads
from random import randint
from os.path import dirname, abspath
from typing import Union

from safeIO import TextFile
from requests import get, post

from translatepy.models.languages import Language
from translatepy.models.userAgents import USER_AGENTS
from translatepy.utils.utils import convert_to_float
from translatepy.utils.annotations import List, Tuple, Dict

FILE_LOCATION = dirname(abspath(__file__))

HEADERS = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Referer": "https://translate.yandex.com/",
    "User-Agent": "Mozilla: Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.3 Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/43.4"
}

TRANSLIT_LANGS = ['am', 'bn', 'el', 'gu', 'he', 'hi', 'hy', 'ja', 'ka', 'kn', 'ko', 'ml', 'mr', 'ne', 'pa', 'si', 'ta', 'te', 'th', 'yi', 'zh']

class YandexTranslate():
    """A Python implementation of Yandex Translation's APIs"""
    def __init__(self, sid_refresh=False) -> None:
        self._base_url = "https://translate.yandex.net/api/v1/tr.json/"
        self._sid_cache = TextFile(FILE_LOCATION + "/_yandex_sid.translatepy", blocking=False)
        self._last_tried_cache = TextFile(FILE_LOCATION + "/_yandex_last_tried.translatepy", blocking=False)
        with self._sid_cache as cache:
            self._sid = str(cache.read())
        with self._last_tried_cache as cache:
            self._last_tried = convert_to_float(cache.read())
        self._headers = self._header()
        self._check_increment = 600 # defaults to 10 minutes
        if sid_refresh:
            self.refreshSID()
        
    def refreshSID(self) -> bool:
        """
        Refreshes the SID used for requests to Yandex Translation API
        
        See issue #4 for more information
        Randomness is used to prevent bot detection

        Args:

        Returns:
            Bool --> wether it succeded or not

        """
        try:
            if time() - self._last_tried > self._check_increment: # if the duration between the last time we tried to get the SID and now is greater than 10 minutes for the first pass
                data = get("https://translate.yandex.com/", headers=self._headers).text
                sid_position = data.find("Ya.reqid = '")
                if sid_position != -1:
                    data = data[sid_position + 12:]
                    self._sid = data[:data.find("';")]
                    self._sid_cache.write(self._sid)
                    
                    self._check_increment = self._check_increment / 2 + randint(0, 1000) / 1000 # decrementing because it might work decremented
                    self._last_tried = time() # maybe keep that in a file
                    self._last_tried_cache.write(self._last_tried)
                    return True
                else:
                    self._check_increment = self._check_increment * 2 + randint(0, 1000) / 1000 # incrementing the waiting time
                    self._last_tried = time() # maybe keep that in a file
                    self._last_tried_cache.write(self._last_tried)
            # else
            # do nothing as we know that yandex will rate-limit us if we ping too much their website
            return False
        except:
            return False

    def _header(self) -> Dict:
        """
        Creates a new header
        
        _header might not be appropriate if the _sid is linked to the User-Agent header

        Args:

        Returns:
            Dict --> the new headers

        """
        _dict = HEADERS.copy()
        randomChoice = randint(0, 7499)
        _dict.update({"User-Agent": USER_AGENTS[randomChoice]})
        return _dict

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
            # preparing the request
            if source_language is None or str(source_language) == "auto":
                source_language = self.language(text)
                if source_language is None:
                    return None, None
            if isinstance(source_language, Language):
                source_language = source_language.yandex_translate
            # check if we have an _sid
            if self._sid.replace(" ", "") == "" and not self.refreshSID():
                return None, None

            def _request():
                """ """
                url = self._base_url + "translate?id=" + self._sid + "-0-0&srv=tr-text&lang=" + str(source_language) +"-" + str(destination_language)  + "&reason=auto&format=text"
                request = get(url, headers=self._headers, data={'text': str(text), 'options': '4'})
                data = loads(request.text)
                if request.status_code < 400 and data["code"] == 200:
                    data = loads(request.text)
                    return str(data["lang"]).split("-")[0], data["text"][0]
                return None, None

            _lang, _text = _request()
            if _lang is None or _text is None:
                if self.refreshSID():
                    _lang, _text = _request()
            return _lang, _text
        except:
            return None, None

    def transliterate(self, text, source_language=None) -> Union[Tuple[str, str], Tuple[None, None]]:
        """
        Transliterates the given text

        Args:
          text: param source_language:  (Default value = None)
          source_language: (Default value = None)

        Returns:
            Tuple(str, str) --> tuple with source_lang, transliteration
            None, None --> when an error occurs

        """
        try:
            if source_language is None:
                source_language = self.language(text)
                if source_language is None or source_language not in TRANSLIT_LANGS:
                    return None, None
                    
            if self._sid.replace(" ", "") == "" and not self.refreshSID():
                return None, None

            def _request():
                """ """
                request = post("https://translate.yandex.net/translit/translit?sid=" + self._sid + "&srv=tr-text", headers=self._headers, data={'text': str(text), 'lang': source_language})
                if request.status_code < 400:
                    return source_language, request.text[1:-1]
                else:
                    return None, None
                    
            _lang, _text = _request()
            if _lang is None or _text is None:
                if self.refreshSID():
                    _lang, _text = _request()
            return _lang, _text
        except:
            return None, None

    def spellcheck(self, text, source_language=None) -> Union[Tuple[str, str], Tuple[None, None]]:
        """
        Spell checks the given text

        Args:
          text: param source_language:  (Default value = None)
          source_language: (Default value = None)

        Returns:
            Tuple(str, str) --> tuple with source_lang, spellchecked_text
            None, None --> when an error occurs

        """
        try:
            if source_language is None:
                source_language = self.language(text)
                if source_language is None:
                    return None, None

            if self._sid.replace(" ", "") == "" and not self.refreshSID():
                return None, None

            def _request():
                """ """
                request = post("https://speller.yandex.net/services/spellservice.json/checkText?sid=" + self._sid + "&srv=tr-text", headers=self._headers, data={'text': str(text), 'lang': source_language, 'options': 516})
                if request.status_code < 400:
                    data = loads(request.text)
                    for correction in data:
                        text = text[:correction.get("pos", 0)] + correction.get("s", [""])[0] + text[correction.get("pos", 0) + correction.get("len", 0):]
                    return source_language, text
                else:
                    return None, None

            _lang, _text = _request()
            if _lang is None or _text is None:
                if self.refreshSID():
                    _lang, _text = _request()
            return _lang, _text
        except:
            return None, None

    def language(self, text, hint=None) -> Union[str, None]:
        """
        Gives back the language of the given text

        Args:
          text: param hint:  (Default value = None)
          hint: (Default value = None)

        Returns:
            str --> the language code
            None --> when an error occurs

        """
        try:
            if hint is None:
                hint = "en,ja"

            if self._sid.replace(" ", "") == "" and not self.refreshSID():
                return None

            url = self._base_url + "detect?sid=" + self._sid + "&srv=tr-text&text=" + str(text) + "&options=1&hint=" + str(hint)

            def _request():
                """ """
                request = get(url, headers=self._headers)
                if request.status_code < 400 and request.json()["code"] == 200:
                    return loads(request.text)["lang"]
                else:
                    return None
            
            _lang = _request()
            if _lang is None:
                if self.refreshSID():
                    _lang = _request()
            return _lang
        except:
            return None

    def __repr__(self) -> str:
        return "Yandex Translate"