"""
Google Translate

Class GoogleTranslateV1 are using Google's new batchexecute (JSONRPC) API.
The code for the functions used (_request and _parse_response) come from https://github.com/ssut/py-googletrans/pull/255 with few adjustments
Heavily inspired by ssut/googletrans and https://kovatch.medium.com/deciphering-google-batchexecute-74991e4e446c

Class GoogleTranslateV2 uses official API methods that are used in Google Translate mobile and web applications
"""

from json import dumps, loads

from translatepy.exceptions import ServiceURLError, UnsupportedMethod
from translatepy.language import Language
from translatepy.translators.base import BaseTranslator
from translatepy.utils.gtoken import TokenAcquirer
from translatepy.utils.request import Request
from translatepy.utils.utils import convert_to_float

# a set is used to avoid having a O(n) lookup time complexity (a set should have a O(1) lookup time complexity)
DOMAINS = {
    "translate.google.ac", "translate.google.ad", "translate.google.ae", "translate.google.al", "translate.google.am", "translate.google.as",
    "translate.google.at", "translate.google.az", "translate.google.ba", "translate.google.be", "translate.google.bf", "translate.google.bg",
    "translate.google.bi", "translate.google.bj", "translate.google.bs", "translate.google.bt", "translate.google.by", "translate.google.ca",
    "translate.google.cat", "translate.google.cc", "translate.google.cd", "translate.google.cf", "translate.google.cg", "translate.google.ch",
    "translate.google.ci", "translate.google.cl", "translate.google.cm", "translate.google.cn", "translate.google.co.ao", "translate.google.co.bw",
    "translate.google.co.ck", "translate.google.co.cr", "translate.google.co.id", "translate.google.co.il", "translate.google.co.in", "translate.google.co.jp",
    "translate.google.co.ke", "translate.google.co.kr", "translate.google.co.ls", "translate.google.co.ma", "translate.google.co.mz", "translate.google.co.nz",
    "translate.google.co.th", "translate.google.co.tz", "translate.google.co.ug", "translate.google.co.uk", "translate.google.co.uz", "translate.google.co.ve",
    "translate.google.co.vi", "translate.google.co.za", "translate.google.co.zm", "translate.google.co.zw", "translate.google.co", "translate.google.com.af",
    "translate.google.com.ag", "translate.google.com.ai", "translate.google.com.ar", "translate.google.com.au", "translate.google.com.bd", "translate.google.com.bh",
    "translate.google.com.bn", "translate.google.com.bo", "translate.google.com.br", "translate.google.com.bz", "translate.google.com.co", "translate.google.com.cu",
    "translate.google.com.cy", "translate.google.com.do", "translate.google.com.ec", "translate.google.com.eg", "translate.google.com.et", "translate.google.com.fj",
    "translate.google.com.gh", "translate.google.com.gi", "translate.google.com.gt", "translate.google.com.hk", "translate.google.com.jm", "translate.google.com.kh",
    "translate.google.com.kw", "translate.google.com.lb", "translate.google.com.lc", "translate.google.com.ly", "translate.google.com.mm", "translate.google.com.mt",
    "translate.google.com.mx", "translate.google.com.my", "translate.google.com.na", "translate.google.com.ng", "translate.google.com.ni", "translate.google.com.np",
    "translate.google.com.om", "translate.google.com.pa", "translate.google.com.pe", "translate.google.com.pg", "translate.google.com.ph", "translate.google.com.pk",
    "translate.google.com.pr", "translate.google.com.py", "translate.google.com.qa", "translate.google.com.sa", "translate.google.com.sb", "translate.google.com.sg",
    "translate.google.com.sl", "translate.google.com.sv", "translate.google.com.tj", "translate.google.com.tr", "translate.google.com.tw", "translate.google.com.ua",
    "translate.google.com.uy", "translate.google.com.vc", "translate.google.com.vn", "translate.google.com", "translate.google.cv", "translate.google.cx",
    "translate.google.cz", "translate.google.de", "translate.google.dj", "translate.google.dk", "translate.google.dm", "translate.google.dz",
    "translate.google.ee", "translate.google.es", "translate.google.eu", "translate.google.fi", "translate.google.fm", "translate.google.fr",
    "translate.google.ga", "translate.google.ge", "translate.google.gf", "translate.google.gg", "translate.google.gl", "translate.google.gm",
    "translate.google.gp", "translate.google.gr", "translate.google.gy", "translate.google.hn", "translate.google.hr", "translate.google.ht",
    "translate.google.hu", "translate.google.ie", "translate.google.im", "translate.google.io", "translate.google.iq", "translate.google.is",
    "translate.google.it", "translate.google.je", "translate.google.jo", "translate.google.kg", "translate.google.ki", "translate.google.kz",
    "translate.google.la", "translate.google.li", "translate.google.lk", "translate.google.lt", "translate.google.lu", "translate.google.lv",
    "translate.google.md", "translate.google.me", "translate.google.mg", "translate.google.mk", "translate.google.ml", "translate.google.mn",
    "translate.google.ms", "translate.google.mu", "translate.google.mv", "translate.google.mw", "translate.google.ne", "translate.google.nf",
    "translate.google.nl", "translate.google.no", "translate.google.nr", "translate.google.nu", "translate.google.pl", "translate.google.pn",
    "translate.google.ps", "translate.google.pt", "translate.google.ro", "translate.google.rs", "translate.google.ru", "translate.google.rw",
    "translate.google.sc", "translate.google.se", "translate.google.sh", "translate.google.si", "translate.google.sk", "translate.google.sm",
    "translate.google.sn", "translate.google.so", "translate.google.sr", "translate.google.st", "translate.google.td", "translate.google.tg",
    "translate.google.tk", "translate.google.tl", "translate.google.tm", "translate.google.tn", "translate.google.to", "translate.google.tt",
    "translate.google.us", "translate.google.vg", "translate.google.vu", "translate.google.ws",

}

_google_supported_languages = {'auto', 'af', 'sq', 'am', 'ar', 'hy', 'az', 'eu', 'be', 'bn', 'bs', 'bg', 'my', 'ca', 'ca', 'ceb', 'zh-cn', 'co', 'cs', 'da', 'nl', 'nl', 'en', 'eo', 'et', 'fi', 'fr', 'fy', 'ka', 'de', 'gd', 'gd', 'ga', 'gl', 'el', 'gu', 'ht', 'ht', 'ha', 'haw', 'he', 'hi', 'hr', 'hu', 'ig', 'is', 'id', 'it', 'jw', 'ja', 'kn', 'kk', 'km', 'ky', 'ky', 'ko', 'ku', 'lo', 'la', 'lv', 'lt', 'lb', 'lb', 'mk', 'ml', 'mi', 'mr', 'ms', 'mg', 'mt', 'mn', 'ne', 'no', 'ny', 'ny', 'ny', 'or', 'pa', 'pa', 'fa', 'pl', 'pt', 'ps', 'ps', 'ro', 'ro', 'ro', 'ru', 'si', 'si', 'sk', 'sl', 'sm', 'sn', 'sd', 'so', 'st', 'es', 'es', 'sr', 'su', 'sw', 'sv', 'ta', 'te', 'tg', 'tl', 'th', 'tr', 'ug', 'ug', 'uk', 'ur', 'uz', 'vi', 'cy', 'xh', 'yi', 'yo', 'zu', 'zh-CN', 'zh-TW'}


# For backward compatibility
class GoogleTranslate(BaseTranslator):

    _supported_languages = _google_supported_languages

    def __init__(self, request: Request = Request(), service_url: str = "translate.google.com"):

        if service_url not in DOMAINS:
            raise ServiceURLError("{url} is not a valid service URL".format(url=str(service_url)))

        google_v1 = GoogleTranslateV1(service_url=service_url, request=request)
        google_v2 = GoogleTranslateV2(service_url=service_url, request=request)

        self.services = [google_v1, google_v2]

    def _translate(self, text, destination_language, source_language):
        for service in self.services:
            try:
                return service._translate(text, destination_language, source_language)
            except Exception as err:
                continue
        raise err

    def _transliterate(self, text, destination_language, source_language):
        for service in self.services:
            try:
                return service._transliterate(text, destination_language, source_language)
            except Exception as err:
                continue
        raise err

    def _language(self, text):
        for service in self.services:
            try:
                return service._language(text)
            except Exception as err:
                continue
        raise err

    def _language_normalize(self, language: Language):
        if language.id == "zho":
            return "zh-cn"
        elif language.id == "och":
            return "zh-tw"
        return language.alpha2

    def _language_denormalize(self, language_code):
        if str(language_code).lower() == "zh-cn":
            return Language("zho")
        elif str(language_code).lower() == "zh-tw":
            return Language("och")
        return Language(language_code)

    def _spellcheck(self, text, source_language):
        # TODO: Implement
        raise UnsupportedMethod()

    def _text_to_speech(self, text, speed, gender, source_language):
        for service in self.services:
            try:
                return service._text_to_speech(text, speed, gender, source_language)
            except Exception as err:
                continue
        raise err

    def __str__(self):
        return "Google"


class GoogleTranslateV1(BaseTranslator):
    """
    A Python implementation of Google Translate's RPC API
    """

    _supported_languages = _google_supported_languages

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
            except Exception:
                pass

        if source_language == 'auto':
            try:
                source_language = parsed[0][2]
            except Exception:
                pass

        if source_language == 'auto' or source_language is None:
            try:
                source_language = parsed[0][1][1][0]
            except Exception:
                pass

        return source_language, translated

    def _transliterate(self, text: str, destination_language: str, source_language: str) -> str:
        request = self._request(text, destination_language, source_language)
        parsed = self._parse_response(request)

        try:
            origin_pronunciation = parsed[0][0]
            if origin_pronunciation is None:
                raise ValueError("translatepy internal exception: Origin Pronounciation is None")
        except Exception:
            origin_pronunciation = text

        if source_language == 'auto' or source_language is None:
            try:
                source_language = parsed[2]
            except Exception:
                pass

        if source_language == 'auto':
            try:
                source_language = parsed[0][2]
            except Exception:
                pass

        if source_language == 'auto' or source_language is None:
            try:
                source_language = parsed[0][1][1][0]
            except Exception:
                pass

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

    def _language_normalize(self, language: Language):
        if language.id == "zho":
            return "zh-CN"
        elif language.id == "och":
            return "zh-TW"
        return language.alpha2

    def _language_denormalize(self, language_code):
        if str(language_code).lower() == "zh-cn":
            return Language("zho")
        elif str(language_code).lower() == "zh-tw":
            return Language("och")
        return Language(language_code)

    def __str__(self):
        return "Google"


class GoogleTranslateV2(BaseTranslator):
    """
    A Python implementation of Google Translate's APIs
    """

    _supported_languages = _google_supported_languages

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
            result = " ".join([sentence["src_translit"] for sentence in response["sentences"] if "src_translit" in sentence])
            return _detected_language, (result if (result is not None and result != "") else text)

    # def define(self):  # XXX: What for need this? --> because I saw on Google Translate that there is a definition feature
    #     """Returns the definition of the given word"""
    #     raise NotImplementedError

    def _text_to_speech(self, text: str, speed: int, gender: str, source_language: str) -> bytes:
        if source_language == "auto":
            source_language = self._language(text)

        params = {"client": "gtx", "ie": "UTF-8", "tl": source_language, "q": text}
        request = self.session.get("https://translate.googleapis.com/translate_tts", params=params)
        if request.status_code == 200:
            return source_language, request.content

        params = {"client": "tw-ob", "q": text, "tl": source_language}
        request = self.session.get("https://translate.google.com/translate_tts", params=params)
        if request.status_code == 200:
            return source_language, request.content

        textlen = len(text)
        token = self.token_acquirer.do(text)
        params = {"ie": "UTF-8", "q": text, "tl": source_language, "total": "1", "idx": "0", "textlen": textlen, "tk": token, "client": "webapp", "prev": "input", "ttsspeed": convert_to_float(speed)}
        request = self.session.get("https://translate.google.com/translate_tts", params=params)
        if request.status_code < 400:
            return source_language, request.content

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

    def _language_normalize(self, language: Language):
        if language.id == "zho":
            return "zh-CN"
        elif language.id == "och":
            return "zh-TW"
        return language.alpha2

    def _language_denormalize(self, language_code):
        if str(language_code).lower() == "zh-cn":
            return Language("zho")
        elif str(language_code).lower() == "zh-tw":
            return Language("och")
        return Language(language_code)

    def __str__(self) -> str:
        return "Google"
