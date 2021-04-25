from time import time
from json import loads
from random import randint
from os.path import dirname, abspath
from typing import Union
from urllib.parse import quote

import pyuseragents
from safeIO import TextFile
from requests import get, post

from translatepy.models.languages import Language
from translatepy.utils.utils import convert_to_float
from translatepy.utils.annotations import Tuple, Dict

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
YT_KEYS = "trnsl.1.1.20181102T213252Z.15973c8fd1497069.dfef0ce2d1d66c4b3a560986cfd349cc27adceef,trnsl.1.1.20181102T213332Z.79148d90f1c6e2d5.c05d93cb4000e5eb194a8cb0302a2577e1786456,trnsl.1.1.20181102T213412Z.b7d99cd224b50875.78b25ec3b559d218c468a15718d62aa9160a6775,trnsl.1.1.20181102T213431Z.541628d09094c1a3.ff27af10a741cd223c176acde97e02d088e5f924,trnsl.1.1.20181102T213450Z.93ccf977a373c675.e773350d58a6b56434efb4e1192683e45462d7e9,trnsl.1.1.20181102T213509Z.f880b66413c0aaf3.9571c4386c6aeb148626ba31ec284691dec1ccaf,trnsl.1.1.20181102T213527Z.eb68115e91aab47f.4da25db7117bff3b15b1dc06fababa6a3c3a8535,trnsl.1.1.20181102T213549Z.ae5a65262a8dcd37.6d7ca0bc28077563a22044c73982101d802110ce,trnsl.1.1.20181102T213613Z.0bad11f72f75fcfa.5a93be6a7aa651b1ef3a36f1fe4ca9af3ac7e32b,trnsl.1.1.20181102T213633Z.a390634b03f595d9.451e188304339141a5c73bcd8b5c25bc0afa4dd9,trnsl.1.1.20181102T213652Z.d9d75034bf77120a.1737bc1c6984c39aeccf2e3581077be809b09b45,trnsl.1.1.20181102T213710Z.8b323dc6d80bba83.f83adcebeaca98ce4445a3d0d328acb59fb577a4,trnsl.1.1.20181102T213729Z.d50920bce790c915.e87f433ef69c108970909acd514734b31556ca4b,trnsl.1.1.20181102T213749Z.3e2b20c226adc8f7.fa0e8f8179d9824864262c0df8d98a222bf06e95,trnsl.1.1.20181102T213808Z.9c3b0910f60f8844.d7a5174868016700c629708e491842a4ff7dfff4,trnsl.1.1.20181102T213936Z.7c005f281fd3959e.a88a3f0411a0b373f941de434e960ec512f1892b,trnsl.1.1.20181102T214014Z.c351b40bd641f99c.114eb8303466d0add7fbca0f7a661d75def7f4c9,trnsl.1.1.20181102T214042Z.77ed3fa8560a999d.9001ccdb59651617814c0720a35dfc1c4ca32bc1,trnsl.1.1.20181102T214151Z.8c6ed1edcf6b527c.7a505097fe32ea5711ff27d44fadd1f84d64e87f,trnsl.1.1.20181102T204954Z.06a524538afb5370.d7c3461460c2e788cb6f67da941b076d65ee49f4,trnsl.1.1.20181102T205629Z.8c5a5671b2c94734.1cebf2b46d03aa6f21a3aada2c6f0dea72b2bb7c,trnsl.1.1.20181102T205740Z.53924bf8bf038b66.1497238b25def89dc7ef38dc919556eb18419aee,trnsl.1.1.20181102T205833Z.6fa2c1193d34ae03.095847fc36981d0abbc9f2d08ff4f2209ce4cbc9,trnsl.1.1.20181102T205859Z.f48f25f673c18de8.2662ca40ff4d9276e19d1a751353976374eb5027,trnsl.1.1.20181102T205922Z.8fcd584cb97e7b7b.96635d8adeb31ac33d8af5f1b84b94bca7785a1b,trnsl.1.1.20181102T205943Z.c107053b80b3da23.33f28db3a836c230ab1fb2ec519c94e6b07f9375,trnsl.1.1.20181102T210007Z.3aba0562159ceb75.5ff0ac290dbd2d01a62023b130581f594c65bd62,trnsl.1.1.20181102T210030Z.48694ecb9d7aef4e.39aa18ca356b09014ce79c7b8cda4f56e7646f58,trnsl.1.1.20181102T210101Z.8ca38ca32d1eeae2.9cf56256c908fd101a9e0bceccaf2ffd729099c4,trnsl.1.1.20181102T210122Z.14226828ff16677d.e64bf54ba3da5fa26a43d522a979e11760cb878a,trnsl.1.1.20181102T210145Z.3ff15c7295b2dec4.252e06955b1265504be710c4871b1b829166f7e9,trnsl.1.1.20181102T210207Z.9c8d671f4e895030.90514dfd6b7cc782e3ff2bcbd046835a661106d1,trnsl.1.1.20181102T210233Z.acd76b1b0033dd87.f0d1034c8b9a9ebd5abd89a0beee582b34a3ee7a,trnsl.1.1.20181102T210309Z.084714f2e6d4c8d6.2113ff52f70e8edb8d15e5dc6b5edc04882d4847,trnsl.1.1.20181102T214252Z.c7d523a692f21cf9.f061c197cf868b9bb22fa1000ed73a131a87a241,trnsl.1.1.20181102T214324Z.68589c5b7b1beaca.4887133744773fe4890cd25061e8619d5817e545,trnsl.1.1.20181102T214351Z.a5f4ec70259dfcdd.e657e0c9a59f33274144633d7cf42475077afb67,trnsl.1.1.20181102T214416Z.cc1f850655586c0f.b6d2866d529d2e001a0318180bc7e9e715f0a5b5,trnsl.1.1.20181102T214444Z.24553e66aa23b466.be6804cb85f09c6f64c5c5f3a17720cf47dc9e86,trnsl.1.1.20181102T214947Z.dfd66bd7b21dd3af.275de56c2ea7a5109ddd1fbc43406a9f485cca65,trnsl.1.1.20181102T215052Z.ec57c48f3cb24691.54a8091b9c8f364af1a9277a7aeb642356476d87,trnsl.1.1.20181102T215122Z.af8710eead58551a.97f86308053dccb2d148577e2c023c0a13489b54,trnsl.1.1.20181102T215154Z.ae797e662ffc0055.af3030fcbd863a5cc71b24afd8a3122b5a6bc2b2,trnsl.1.1.20181102T215230Z.23c8ec80d3d564ee.0285f07c82e3d91e03c274b72d889701a7de7485,trnsl.1.1.20181102T215258Z.3d6142281267b1ee.ef871a7bae00682a9225f34f40c2084aa0cd1f51,trnsl.1.1.20181102T215327Z.b0324d3620775026.f61c65f8c6c31b2f45973397e86eeb4af8ef7bc9,trnsl.1.1.20181102T215356Z.e72ddaaa2e5d3029.fc6d21d8bf367760164caf2073be332b87e558c5,trnsl.1.1.20181102T215421Z.e7bb329825ab40c2.6b4368f077ab1f36aca314f1f5d3855de9b7ffb4,trnsl.1.1.20181102T215447Z.3d4324e2958136ff.8d6085bf3873f653c02d07433ad2f336de64c23f,trnsl.1.1.20181102T215517Z.c17384773f356575.be5756d5d3ede5b0823a865aa8b2a401d5b1cf8d,trnsl.1.1.20181102T215548Z.89db0ce5c7b3bef8.c8407a45bc8655af5ab12da309f504475756371b,trnsl.1.1.20181102T215618Z.c22f22948a0fdbd1.876a5521c7737b41b6a43ca9af0b66e3f8166ab6,trnsl.1.1.20181102T215641Z.fe52de1dc3618d73.740023052cbd6a0bc98bd5bf5ff05a55770350be,trnsl.1.1.20181102T215711Z.9c77c09515106e89.72841b56546a7f19ed8f77b27b91a6dee93a59b1,trnsl.1.1.20181102T215736Z.162caa5087e102a8.6f8bbfcf5ef76652dc6c1b3249c35fc7cd944d19,trnsl.1.1.20181102T215811Z.6e967911b314d9f2.040c8dc577ac16ddea33e33225a2b334b8fd0be3,trnsl.1.1.20181102T215859Z.467b4f132813ab8a.5c04bd040c0ddbccdb9fd1be799384e6826a5635,trnsl.1.1.20181102T220047Z.ad0e4a72ac465775.9f9a21610f30534627db70c35c2c1e453cbc7c36,trnsl.1.1.20181102T220117Z.09ce6c0292c9761c.8cc1dfc8f30b6c3bf30c8e356088ef2685f37d86".split(',')

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
            # do nothing as we know that yandex will rate-limit us if we ping them too much
            return False
        except Exception:
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
        _dict.update({"User-Agent": pyuseragents.random()})
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
                url = self._base_url + "translate?id=" + self._sid + "-0-0&srv=tr-text&lang=" + str(source_language) + "-" + str(destination_language)  + "&reason=auto&format=text"
                request = get(url, headers=self._headers, data={'text': str(text), 'options': '4'})
                data = loads(request.text)
                if request.status_code < 400 and data["code"] == 200:
                    data = loads(request.text)
                    return str(data["lang"]).split("-")[0], data["text"][0]
                return None, None

            _lang, _text = _request()
            if _lang is None and _text is None:
                if self.refreshSID():
                    _lang, _text = _request()
            return _lang, _text
        except Exception:
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
        except Exception:
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
        except Exception:
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

            text = quote(str(text), safe='')

            url = self._base_url + "detect?sid=" + self._sid + "&srv=tr-text&text=" + text + "&options=1&hint=" + str(hint)

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
        except Exception:
            return None

    def __repr__(self) -> str:
        return "Yandex Translate"