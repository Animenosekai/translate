"""
Google Translate

Class GoogleTranslateV1 are using Google's new batchexecute (JSONRPC) API.
The code for the functions used (_request and _parse_response) come from https://github.com/ssut/py-googletrans/pull/255 with few adjustments
Heavily inspired by ssut/googletrans and https://kovatch.medium.com/deciphering-google-batchexecute-74991e4e446c

Class GoogleTranslateV2 uses official API methods that are used in Google Translate mobile and web applications
"""

from json import loads, dumps

from translatepy.translators.base import BaseTranslator
from translatepy.exceptions import UnsupportedMethod
from translatepy.utils.gtoken import TokenAcquirer
from translatepy.utils.utils import convert_to_float
from translatepy.utils.request import Request
from translatepy.language import Language


# For backward compatibility
class GoogleTranslate(BaseTranslator):
    def __init__(self, request: Request = Request(), service_url: str = "translate.google.com"):
        google_v1 = GoogleTranslateV1(service_url=service_url, request=request)
        google_v2 = GoogleTranslateV2(service_url=service_url, request=request)

        self.services = [google_v1, google_v2]

    def _translate(self, text, destination_language, source_language):
        for service in self.services:
            try:
                return service._translate(text, destination_language, source_language)
            except Exception:
                continue

    def _transliterate(self, text, destination_language, source_language):
        for service in self.services:
            try:
                return service._transliterate(text, destination_language, source_language)
            except Exception:
                continue

    def _language(self, text):
        for service in self.services:
            try:
                return service._language(text)
            except Exception:
                continue

    def _supported_languages(self):
        raise UnsupportedMethod()

    def _example(self, text, destination_language, source_language):
        raise UnsupportedMethod()

    def _dictionary(self, text, destination_language, source_language):
        raise UnsupportedMethod()

    def _language_normalize(self, language):
        return language.google

    def _language_denormalize(self, language_code):
        return Language.by_google(language_code)

    def _spellcheck(self, text, source_language):
        raise UnsupportedMethod()

    def __repr__(self):
        return "Google Translate"


class GoogleTranslateV1(BaseTranslator):
    """
    A Python implementation of Google Translate's RPC API
    """
    def __init__(self, request: Request = Request(), service_url: str = "translate.google.com"):
        self.session = request
        self.service_url = service_url

    def _request(self, text, destination, source):
        """
        Makes a translation request to Google Translate RPC API

        Most of the code comes from https://github.com/ssut/py-googletrans/pull/255
        """
        rpc_request = dumps([[
            [
                'MkEWBc',
                dumps([[text, source, destination, True], [None]], separators=(',', ':')),
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
        request = self.session.post('https://{}/_/TranslateWebserverUi/data/batchexecute'.format(self.service_url), params=params, data=data)
        if request.status_code < 400:
            return request.text

    def _parse_response(self, data):
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

    def _translate(self, text: str, destination_language: str, source_language: str) -> str:
        """
        Translates the given text to the destination language with the new batchexecute API

        Heavily inspired by ssut/googletrans and https://kovatch.medium.com/deciphering-google-batchexecute-74991e4e446c
        """
        request = self._request(text, destination_language, source_language)
        parsed = self._parse_response(request)
        translated = (' ' if parsed[1][0][0][3] else '').join([part[0] for part in parsed[1][0][0][5]])

        if source_language == 'auto' or source_language is None:
            try:
                source_language = parsed[2]
            except Exception: pass

        if source_language == 'auto':
            try:
                source_language = parsed[0][2]
            except Exception: pass

        if source_language == 'auto' or source_language is None:
            try:
                source_language = parsed[0][1][1][0]
            except Exception: pass

        return source_language, translated

    def _transliterate(self, text: str, destination_language: str, source_language: str) -> str:
        request = self._request(text, destination_language, source_language)
        parsed = self._parse_response(request)

        try:
            origin_pronunciation = parsed[0][0]
        except Exception:
            origin_pronunciation = text

        if source_language == 'auto' or source_language is None:
            try:
                source_language = parsed[2]
            except Exception: pass

        if source_language == 'auto':
            try:
                source_language = parsed[0][2]
            except Exception: pass

        if source_language == 'auto' or source_language is None:
            try:
                source_language = parsed[0][1][1][0]
            except Exception: pass

        return source_language, origin_pronunciation

    def _language(self, text):
        """
        Returns the language of the given text with the new batchexecute API

        Heavily inspired by ssut/googletrans and https://kovatch.medium.com/deciphering-google-batchexecute-74991e4e446c
        """
        request = self._request(text, "en", "auto")
        parsed = self._parse_response(request)

        try:
            source_language = parsed[2]
        except Exception:
            source_language = None

        if source_language == 'auto' or source_language is None:
            try:
                source_language = parsed[0][2]
            except Exception:
                pass

        if source_language == 'auto' or source_language is None:
            try:
                source_language = parsed[0][1][1][0]
            except Exception:
                pass

        return source_language

    def _supported_languages(self):
        raise UnsupportedMethod()

    def _example(self, text, destination_language, source_language):
        raise UnsupportedMethod()

    def _dictionary(self, text, destination_language, source_language):
        raise UnsupportedMethod()

    def _language_normalize(self, language):
        return language.google

    def _language_denormalize(self, language_code):
        return Language.by_google(language_code)

    def _spellcheck(self, text, source_language):
        raise UnsupportedMethod()

    def __repr__(self):
        return "Google Translate"


class GoogleTranslateV2(BaseTranslator):
    """
    A Python implementation of Google Translate's APIs
    """
    def __init__(self, request: Request = Request(), service_url: str = "translate.google.com"):
        self.session = request
        self.service_url = service_url
        self.token_acquirer = TokenAcquirer(service_url)

    def _translate(self, text: str, destination_language: str, source_language: str) -> str:
        params = {"client": "gtx", "dt": "t", "sl": source_language, "tl": destination_language, "q": text}
        request = self.session.get("https://translate.googleapis.com/translate_a/single", params=params)
        response = request.json()
        if request.status_code < 400:
            try:
                _detected_language = response[2]
            except Exception:
                _detected_language = source_language
            return _detected_language, "".join([sentence[0] for sentence in response[0]])

        params = {"client": "dict-chrome-ex", "sl": source_language, "tl": destination_language, "q": text}
        request = self.session.get("https://clients5.google.com/translate_a/t", params=params)
        response = request.json()
        if request.status_code < 400:
            try:
                try:
                    _detected_language = response['ld_result']["srclangs"][0]
                except Exception:
                    _detected_language = source_language
                return "".join((sentence["trans"] if "trans" in sentence else "") for sentence in response["sentences"])
            except Exception:
                try:
                    try:
                        _detected_language = response[0][0][2]
                    except Exception:
                        _detected_language = source_language
                    return "".join(sentence for sentence in response[0][0][0][0])
                except Exception:  # if it fails, continue with the other endpoints
                    pass

        params = {"dt": ["t", "bd", "ex", "ld", "md", "qca", "rw", "rm", "ss", "t", "at"], "client": "gtx", "q": text, "hl": destination_language, "sl": source_language, "tl": destination_language, "dj": "1", "source": "bubble"}
        request = self.session.get("https://translate.googleapis.com/translate_a/single", params=params)
        response = request.json()
        if request.status_code < 400:
            try:
                _detected_language = response.get("src", None)
                if _detected_language is None:
                    _detected_language = response.get("ld_result", {}).get("srclangs", [None])[0]
                    if _detected_language is None:
                        _detected_language = response.get("ld_result", {}).get("extended_srclangs", [None])[0]
            except Exception:
                _detected_language = source_language
            return _detected_language, " ".join([sentence["trans"] for sentence in response["sentences"] if "trans" in sentence])

        params = {"client": "gtx", "dt": ["t", "bd"], "dj": "1", "source": "input", "q": text, "sl": source_language, "tl": destination_language}
        request = self.session.get("https://translate.googleapis.com/translate_a/single", params=params)
        response = request.json()
        if request.status_code < 400:
            try:
                _detected_language = response["src"]
            except Exception:
                _detected_language = source_language
            return _detected_language, "".join([sentence["trans"] for sentence in response["sentences"] if "trans" in sentence])

    def _transliterate(self, text: str, destination_language: str, source_language: str) -> str:
        params = {"dt": ["t", "bd", "ex", "ld", "md", "qca", "rw", "rm", "ss", "t", "at"], "client": "gtx", "q": text, "hl": destination_language, "sl": source_language, "tl": destination_language, "dj": "1", "source": "bubble"}
        request = self.session.get("https://translate.googleapis.com/translate_a/single", params=params)
        response = request.json()
        if request.status_code < 400:
            try:
                _detected_language = response.get("src", None)
                if _detected_language is None:
                    _detected_language = response.get("ld_result", {}).get("srclangs", [None])[0]
                    if _detected_language is None:
                        _detected_language = response.get("ld_result", {}).get("extended_srclangs", [None])[0]
            except Exception:
                _detected_language = source_language
            return _detected_language, " ".join([sentence["src_translit"] for sentence in response["sentences"] if "src_translit" in sentence])

    # def define(self):  # XXX: What for need this? --> because I saw on Google Translate that there is a definition feature
    #     """Returns the definition of the given word"""
    #     raise NotImplementedError

    def _text_to_speech(self, text: str, speed: int, source_language="auto") -> bytes:
        if source_language == "auto":
            source_language = self._language(text)

        params = {"client": "gtx", "ie": "UTF-8", "tl": source_language, "q": text}
        request = self.session.get("https://translate.googleapis.com/translate_tts", params=params)
        if request.status_code == 200:
            return request.content

        params = {"client": "tw-ob", "q": text, "tl": source_language}
        request = self.session.get("https://translate.google.com/translate_tts", params=params)
        if request.status_code == 200:
            return request.content

        textlen = len(text)
        token = self.token_acquirer.do(text)
        params = {"ie": "UTF-8", "q": text, "tl": source_language, "total": "1", "idx": "0", "textlen": textlen, "tk": token, "client": "webapp", "prev": "input", "ttsspeed": convert_to_float(speed)}
        request = self.session.get("https://translate.google.com/translate_tts", params=params)
        if request.status_code < 400:
            return request.content

    def _language(self, text: str) -> str:
        params = {"client": "gtx", "dt": "t", "sl": "auto", "tl": "ja", "q": text}
        request = self.session.get("https://translate.googleapis.com/translate_a/single", params=params)
        response = request.json()
        if request.status_code < 400:
            return response[2]

        params = {"client": "dict-chrome-ex", "sl": "auto", "tl": "ja", "q": text}
        request = self.session.get("https://clients5.google.com/translate_a/t", params=params)
        response = request.json()
        if request.status_code < 400:
            return response['ld_result']["srclangs"][0]

    def _supported_languages(self):
        raise UnsupportedMethod()

    def _example(self, text, destination_language, source_language):
        raise UnsupportedMethod()

    def _dictionary(self, text, destination_language, source_language):
        raise UnsupportedMethod()

    def _language_normalize(self, language):
        return language.google

    def _language_denormalize(self, language_code):
        return Language.by_google(language_code)

    def _spellcheck(self, text, source_language):
        raise UnsupportedMethod()

    def __repr__(self):
        return "Google Translate"
