"""
Google Translate

About _new_translate and _new_language:
    Both function are using Google's new batchexecute (JSONRPC) API.
    The code for the functions used (_request and _parse_response) come from https://github.com/ssut/py-googletrans/pull/255 with few adjustments
    Heavily inspired by ssut/googletrans and https://kovatch.medium.com/deciphering-google-batchexecute-74991e4e446c
"""

from typing import Union
from requests import get, post
from json import loads, dumps
from urllib.parse import quote
from traceback import print_exc

import pyuseragents
from translatepy.utils.gtoken import TokenAcquirer
from translatepy.utils.annotations import Tuple
from translatepy.utils.utils import convert_to_float

HEADERS = {
    'User-Agent': pyuseragents.random()
}


def _request(text, destination, source):
    """
    Makes a translation request to Google Translate RPC API

    Most of the code comes from https://github.com/ssut/py-googletrans/pull/255
    """
    rpc_request = dumps([[
        [
            'MkEWBc',
            dumps([[str(text), str(source), str(destination), True],[None]], separators=(',', ':')),
            None,
            'generic',
        ],
    ]], separators=(',', ':'))
    data = {
        "f.req": rpc_request
    }
    params = {
        'rpcids': "MkEWBc",
        'bl': 'boq_translate-webserver_20201207.13_p0',
        'soc-app': 1,
        'soc-platform': 1,
        'soc-device': 1,
        'rt': 'c',
    }
    request = post('https://translate.google.com/_/TranslateWebserverUi/data/batchexecute', params=params, data=data)
    if request.status_code < 400:
        return request.text
    return None

def _parse_response(data):
    """
    Parses the broken JSON response given by the new RPC API endpoint (batchexecute)

    Most of the code comes from https://github.com/ssut/py-googletrans/pull/255
    """
    token_found = False
    resp = ""
    opening_bracket = 0
    closing_bracket = 0
    # broken json parsing
    for line in data.split('\n'):
        token_found = token_found or '"MkEWBc"' in line[:30]
        if not token_found:
            continue

        is_in_string = False
        for index, char in enumerate(line):
            if char == '\"' and line[max(0, index - 1)] != '\\':
                is_in_string = not is_in_string
            if not is_in_string:
                if char == '[':
                    opening_bracket += 1
                elif char == ']':
                    closing_bracket += 1

        resp += line
        if opening_bracket == closing_bracket:
            break

    return loads(loads(resp)[0][2])


def _new_translate(text, destination_language, source_language):
    """
    Translates the given text to the destination language with the new batchexecute API

    Heavily inspired by ssut/googletrans and https://kovatch.medium.com/deciphering-google-batchexecute-74991e4e446c
    """
    try:
        request = _request(text, destination_language, source_language)    
        parsed = _parse_response(request)
        translated = (' ' if parsed[1][0][0][3] else '').join([part[0] for part in parsed[1][0][0][5]])

        source_language = str(source_language)
        try:
            source_language = parsed[2]
        except Exception: pass

        if source_language.lower() == 'auto':
            try:
                source_language = parsed[0][2]
            except Exception: pass

        if source_language == 'auto' or source_language is None:
            try:
                source_language = parsed[0][1][1][0]
            except Exception: pass

        return source_language, translated
    except Exception:
        return None, None


def _new_language(text):
    """
    Returns the language of the given text with the new batchexecute API

    Heavily inspired by ssut/googletrans and https://kovatch.medium.com/deciphering-google-batchexecute-74991e4e446c
    """
    try:
        request = _request(text, "en", "auto")    
        parsed = _parse_response(request)

        source_language = None
        try:
            source_language = parsed[2]
        except Exception: pass

        if source_language == 'auto' or source_language is None:
            try:
                source_language = parsed[0][2]
            except Exception: pass

        if source_language == 'auto' or source_language is None:
            try:
                source_language = parsed[0][1][1][0]
            except Exception: pass

        return source_language
    except Exception:
        return None

class GoogleTranslate():
    """A Python implementation of Google Translate's APIs"""
    def __init__(self) -> None:
        try:
            self.token_acquirer = TokenAcquirer()
        except Exception:
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
            if source_language is None:
                source_language = "auto"
            src, result = _new_translate(text, destination_language, source_language)
            if src is not None and result is not None:
                return src, result
            text = quote(str(text), safe='')
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
                    except Exception:
                        try:
                            return data[0][0][2], "".join(sentence for sentence in data[0][0][0][0])
                        except Exception:
                            pass
                
                request = get("https://translate.googleapis.com/translate_a/single?dt=t&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&dt=at&client=gtx&q=" + text + "&hl=" + str(destination_language) + "&sl=" + str(source_language) + "&tl=" + str(destination_language) + "&dj=1&source=bubble")
                if request.status_code < 400:
                    data = loads(request.text)
                    src = data.get("src", None)
                    if src is None:
                        src = data.get("ld_result", {}).get("srclangs", [None])[0]
                        if src is None:
                            src = data.get("ld_result", {}).get("extended_srclangs", [None])[0]
                    return src, " ".join([sentence["trans"] for sentence in data["sentences"] if "trans" in sentence])
                request = get("https://translate.googleapis.com/translate_a/single?client=gtx&dt=t&dt=bd&dj=1&source=input&q=" + text + "&sl=" + str(source_language) + "&tl=" + str(destination_language))
                if request.status_code < 400:
                    data = loads(request.text)
                    return data["src"], " ".join([sentence["trans"] for sentence in data["sentences"] if "trans" in sentence])
                return None, None
        except Exception:
            return None, None

    def transliterate(self, text, source_language=None) -> Union[Tuple[str, str], Tuple[None, None]]:
        """
        Transliterate the given text

        Args:
          text: param destination_language:
          source_language: Default value = "auto")

        Returns:
            Tuple(str, str) --> tuple with source_lang, translation
            None, None --> when an error occurs

        """
        try:
            if source_language is None:
                source_language = "auto"
            request = _request(text, "en", source_language)
            parsed = _parse_response(request)

            source_language = str(source_language)
            try:
                source_language = parsed[2]
            except Exception: pass

            if source_language.lower() == 'auto':
                try:
                    source_language = parsed[0][2]
                except Exception: pass

            if source_language == 'auto' or source_language is None:
                try:
                    source_language = parsed[0][1][1][0]
                except Exception: pass

            origin_pronunciation = None
            try:
                origin_pronunciation = parsed[0][0]
            except Exception: pass

            if origin_pronunciation is not None:
                return source_language, origin_pronunciation
            request = get("https://translate.googleapis.com/translate_a/single?dt=t&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&dt=at&client=gtx&q=" + text + "&hl=" + str(destination_language) + "&sl=" + str(source_language) + "&tl=" + str(destination_language) + "&dj=1&source=bubble")
            if request.status_code < 400:
                data = loads(request.text)
                src = data.get("src", None)
                if src is None:
                    src = data.get("ld_result", {}).get("srclangs", [None])[0]
                    if src is None:
                        src = data.get("ld_result", {}).get("extended_srclangs", [None])[0]
                return src, " ".join([sentence["src_translit"] for sentence in data["sentences"] if "src_translit" in sentence])
            return None, None
        except Exception:
            return None, None

    def define(self):
        """Returns the definition of the given word"""
        raise NotImplementedError

    def text_to_speech(self, text, source_language=None) -> Union[bytes, None]:
        """
        Gives back the text to speech result for the given text

        Args:
          text:

        Returns:
            bytes --> the mp3 file as bytes
            None --> when an error occurs
        """
        try:
            text = quote(str(text), safe='')
            if source_language is None:
                source_language = self.language(text)
                if source_language is None:
                    return None
            request = get("https://translate.googleapis.com/translate_tts?client=gtx&ie=UTF-8&tl=" + str(source_language) + "&q=" + text)
            if request.status_code == 200:
                return request.content
            request = get("https://translate.google.com/translate_tts?client=tw-ob&q=" + text + "&tl=" + str(source_language))
            if request.status_code == 200:
                return request.content
            if self.token_acquirer is None:
                return None
            textlen = len(text)
            token = self.token_acquirer.do(text)
            if token is None:
                return None
            request = get("https://translate.google.com/translate_tts?ie=UTF-8&q=" + text + "&tl=" + source_language + "&total=1&idx=0&textlen=" + textlen + "&tk=" + str(token) + "&client=webapp&prev=input&ttsspeed=" + str(convert_to_float(speed)))
            if request.status_code < 400:
                return request.content
            else:
                return None
        except Exception:
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
            lang = _new_language(text)
            if lang is not None:
                return lang
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
        except Exception:
            return None

    def __repr__(self) -> str:
        return "Google Translate"
