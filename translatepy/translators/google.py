"""
Google Translate

This both uses the mobile version of Google Translate, extension endpoints and the `batchexecute` (JSONRPC) API
The `batchexecute` implementation is heavily inspired by ssut/py-googletrans#255 and https://kovatch.medium.com/deciphering-google-batchexecute-74991e4e446c
"""

import json
import typing

from translatepy import models
from translatepy.exceptions import ServiceURLError
from translatepy.language import Language
from translatepy.translators.base import BaseTranslator, C
from translatepy.translators.base_aggregator import BaseTranslatorAggregator
from translatepy.utils import request
from translatepy.utils.gtoken import TokenAcquirer
from translatepy.utils.utils import convert_to_float

# Sets have O(1) time complexity when using the `in` keyword
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
    "translate.google.us", "translate.google.vg", "translate.google.vu", "translate.google.ws"
}

SUPPORTED_LANGUAGES = {'af', 'am', 'ar', 'auto', 'az', 'be', 'bg', 'bn', 'bs', 'ca', 'ceb', 'co', 'cs', 'cy', 'da', 'de', 'el', 'en', 'eo', 'es',
                       'et', 'eu', 'fa', 'fi', 'fr', 'fy', 'ga', 'gd', 'gl', 'gu', 'ha', 'haw', 'he', 'hi', 'hr', 'ht', 'hu', 'hy', 'id', 'ig',
                       'is', 'it', 'ja', 'jw', 'ka', 'kk', 'km', 'kn', 'ko', 'ku', 'ky', 'la', 'lb', 'lo', 'lt', 'lv', 'mg', 'mi', 'mk', 'ml',
                       'mn', 'mr', 'ms', 'mt', 'my', 'ne', 'nl', 'no', 'ny', 'or', 'pa', 'pl', 'ps', 'pt', 'ro', 'ru', 'sd', 'si', 'sk', 'sl',
                       'sm', 'sn', 'so', 'sq', 'sr', 'st', 'su', 'sv', 'sw', 'ta', 'te', 'tg', 'th', 'tl', 'tr', 'ug', 'uk', 'ur', 'uz', 'vi',
                       'xh', 'yi', 'yo', 'zh-CN', 'zh-TW', 'zh-cn', 'zu'}


class GoogleTranslate(BaseTranslatorAggregator):
    """An aggregation of Google Translate translators"""

    def __init__(self, session: typing.Optional[request.Session] = None, service_url: str = "translate.google.com", *args, **kwargs):
        if service_url not in DOMAINS:
            raise ServiceURLError("{url} is not a valid service URL".format(url=str(service_url)))

        google_v1 = GoogleTranslateV1(service_url=service_url, session=session)
        google_v2 = GoogleTranslateV2(service_url=service_url, session=session)

        services_list = [google_v1, google_v2]

        super().__init__(services_list, session, *args, **kwargs)

    def __str__(self) -> str:
        return "Google Translate"


class GoogleTranslateV1(BaseTranslator):
    """
    A Python implementation of Google Translate's JSONRPC API
    """

    _supported_languages = SUPPORTED_LANGUAGES

    def __init__(self, session: typing.Optional[request.Session] = None, service_url: str = "translate.google.com"):
        super().__init__(session)
        self.service_url = service_url

    def _request(self, text, destination, source):
        """
        Makes a translation request to Google Translate RPC API

        Most of the code comes from https://github.com/ssut/py-googletrans/pull/255
        """
        rpc_request = json.dumps([[
            [
                'MkEWBc',
                json.dumps([[text, source, destination, True], [None]], separators=(',', ':')),
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
        request.raise_for_status()
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

        return json.loads(json.loads(resp)[0][2])

    def _translate(self: C, text: str, dest_lang: typing.Any, source_lang: typing.Any) -> models.TranslationResult[C]:
        """
        Translates the given text to the destination language with the new `batchexecute` API

        Heavily inspired by ssut/googletrans and https://kovatch.medium.com/deciphering-google-batchexecute-74991e4e446c
        """
        request = self._request(text, dest_lang, source_lang)
        parsed = self._parse_response(request)
        translated = (' ' if parsed[1][0][0][3] else '').join([part[0] for part in parsed[1][0][0][5]])

        if source_lang == 'auto' or source_lang is None:
            try:
                source_lang = parsed[2]
            except Exception:
                pass

        if source_lang == 'auto':
            try:
                source_lang = parsed[0][2]
            except Exception:
                pass

        if source_lang == 'auto' or source_lang is None:
            try:
                source_lang = parsed[0][1][1][0]
            except Exception:
                pass

        return models.TranslationResult(source_lang=source_lang, translation=translated, raw=parsed)

    def _transliterate(self: C, text: str, dest_lang: typing.Any, source_lang: typing.Any) -> models.TransliterationResult[C]:
        request = self._request(text, dest_lang, source_lang)
        parsed = self._parse_response(request)

        try:
            origin_pronunciation = parsed[0][0]
            if origin_pronunciation is None:
                raise ValueError("translatepy internal exception: Origin Pronounciation is None")
        except Exception:
            origin_pronunciation = text

        if source_lang == 'auto' or source_lang is None:
            try:
                source_lang = parsed[2]
            except Exception:
                pass

        if source_lang == 'auto':
            try:
                source_lang = parsed[0][2]
            except Exception:
                pass

        if source_lang == 'auto' or source_lang is None:
            try:
                source_lang = parsed[0][1][1][0]
            except Exception:
                pass

        return models.TransliterationResult(source_lang=source_lang, raw=parsed, transliteration=origin_pronunciation)

    def _language(self: C, text: str) -> models.LanguageResult[C]:
        """
        Returns the language of the given text with the new batchexecute API

        Heavily inspired by ssut/googletrans and https://kovatch.medium.com/deciphering-google-batchexecute-74991e4e446c
        """
        request = self._request(text, "en", "auto")
        parsed = self._parse_response(request)

        try:
            source_lang = parsed[2]
        except Exception:
            source_lang = None

        if source_lang == 'auto' or source_lang is None:
            try:
                source_lang = parsed[0][2]
            except Exception:
                pass

        if source_lang == 'auto' or source_lang is None:
            try:
                source_lang = parsed[0][1][1][0]
            except Exception:
                pass

        return models.LanguageResult(language=source_lang, raw=parsed)

    def _language_to_code(self, language: Language) -> typing.Union[str, typing.Any]:
        if language.id == "zho":
            return "zh-CN"
        elif language.id == "och":
            return "zh-TW"
        return language.alpha2

    def _code_to_language(self, code: typing.Union[str, typing.Any]) -> Language:
        language_code = str(code).lower()
        if language_code == "zh-cn":
            return Language("zho")
        elif language_code == "zh-tw":
            return Language("och")
        return Language(language_code)

    def __str__(self) -> str:
        return "Google Translate (batchexecute)"


class GoogleTranslateV2(BaseTranslator):
    """
    A Python implementation of Google Translate's APIs
    """

    _supported_languages = SUPPORTED_LANGUAGES

    def __init__(self, session: typing.Optional[request.Session] = None, service_url: str = "translate.google.com"):
        super().__init__(session)
        self.service_url = service_url
        self.token_acquirer = TokenAcquirer(service_url)

    def _translate(self: C, text: str, dest_lang: typing.Any, source_lang: typing.Any) -> models.TranslationResult[C]:
        params = {"client": "gtx", "dt": "t", "sl": source_lang, "tl": dest_lang, "q": text}
        request = self.session.get("https://translate.googleapis.com/translate_a/single", params=params)
        if request.status_code < 400:
            response = request.json()
            try:
                _detected_language = response[2]
            except Exception:
                _detected_language = source_lang
            return models.TranslationResult(source_lang=_detected_language, translation="".join([sentence[0] for sentence in response[0]]), raw=response)

        params = {"client": "dict-chrome-ex", "sl": source_lang, "tl": dest_lang, "q": text}
        request = self.session.get("https://clients5.google.com/translate_a/t", params=params)

        if request.status_code < 400:
            response = request.json()
            try:
                try:
                    _detected_language = response['ld_result']["srclangs"][0]
                except Exception:
                    _detected_language = source_lang
                return models.TranslationResult(source_lang=_detected_language,
                                                translation="".join((sentence["trans"] if "trans" in sentence else "") for sentence in response["sentences"]),
                                                raw=response)
            except Exception:
                try:
                    try:
                        _detected_language = response[0][0][2]
                    except Exception:
                        _detected_language = source_lang
                    return models.TranslationResult(source_lang=_detected_language,
                                                    translation="".join(sentence for sentence in response[0][0][0][0]),
                                                    raw=response)
                except Exception:  # if it fails, continue with the other endpoints
                    pass

        params = {"dt": ["t", "bd", "ex", "ld", "md", "qca", "rw", "rm", "ss", "t", "at"],
                  "client": "gtx",
                  "q": text,
                  "hl": dest_lang,
                  "sl": source_lang,
                  "tl": dest_lang,
                  "dj": "1",
                  "source": "bubble"}
        request = self.session.get("https://translate.googleapis.com/translate_a/single", params=params)
        if request.status_code < 400:
            response = request.json()
            try:
                _detected_language = response.get("src", None)
                if _detected_language is None:
                    _detected_language = response.get("ld_result", {}).get("srclangs", [None])[0]
                    if _detected_language is None:
                        _detected_language = response.get("ld_result", {}).get("extended_srclangs", [None])[0]
            except Exception:
                _detected_language = source_lang
            return models.TranslationResult(source_lang=_detected_language,
                                            translation=" ".join([sentence["trans"] for sentence in response["sentences"] if "trans" in sentence]),
                                            raw=response)

        params = {"client": "gtx",
                  "dt": ["t", "bd"],
                  "dj": "1",
                  "source": "input",
                  "q": text,
                  "sl": source_lang,
                  "tl": dest_lang}
        request = self.session.get("https://translate.googleapis.com/translate_a/single", params=params)
        if request.status_code < 400:
            response = request.json()
            try:
                _detected_language = response["src"]
            except Exception:
                _detected_language = source_lang
            return models.TranslationResult(source_lang=_detected_language,
                                            translation="".join([sentence["trans"] for sentence in response["sentences"] if "trans" in sentence]),
                                            raw=response)

    def _transliterate(self: C, text: str, dest_lang: typing.Any, source_lang: typing.Any) -> models.TransliterationResult[C]:
        params = {"dt": ["t", "bd", "ex", "ld", "md", "qca", "rw", "rm", "ss", "t", "at"],
                  "client": "gtx",
                  "q": text,
                  "hl": dest_lang,
                  "sl": source_lang,
                  "tl": dest_lang,
                  "dj": "1",
                  "source": "bubble"}
        request = self.session.get("https://translate.googleapis.com/translate_a/single", params=params)
        request.raise_for_status()
        response = request.json()
        try:
            _detected_language = response.get("src", None)
            if _detected_language is None:
                _detected_language = response.get("ld_result", {}).get("srclangs", [None])[0]
                if _detected_language is None:
                    _detected_language = response.get("ld_result", {}).get("extended_srclangs", [None])[0]
        except Exception:
            _detected_language = source_lang
        result = " ".join([sentence["src_translit"] for sentence in response["sentences"] if "src_translit" in sentence])
        return models.TransliterationResult(source_lang=_detected_language,
                                            transliteration=(result if (result is not None and result != "") else text),
                                            raw=response)

    # TODO: `dictionary`

    def _text_to_speech(self: C, text: str, speed: int, gender: models.Gender, source_lang: typing.Any) -> models.TextToSpeechResult[C]:
        if source_lang == "auto":
            source_lang = self._language_to_code(self.language(text).language)

        params = {"client": "gtx", "ie": "UTF-8", "tl": source_lang, "q": text}
        request = self.session.get("https://translate.googleapis.com/translate_tts", params=params)
        if request.status_code == 200:
            return models.TextToSpeechResult(source_lang=source_lang, result=request.content)

        params = {"client": "tw-ob", "q": text, "tl": source_lang}
        request = self.session.get("https://translate.google.com/translate_tts", params=params)
        if request.status_code == 200:
            return models.TextToSpeechResult(source_lang=source_lang, result=request.content)

        textlen = len(text)
        token = self.token_acquirer.do(text)
        params = {"ie": "UTF-8", "q": text, "tl": source_lang, "total": "1", "idx": "0", "textlen": textlen, "tk": token, "client": "webapp", "prev": "input", "ttsspeed": convert_to_float(speed)}
        request = self.session.get("https://translate.google.com/translate_tts", params=params)
        request.raise_for_status()
        return models.TextToSpeechResult(source_lang=source_lang, result=request.content)

    def _language(self: C, text: str) -> models.LanguageResult[C]:
        translation = self.translate(text=text,
                                     dest_lang="Japanese")

        models.LanguageResult(language=translation.source_lang, raw=translation.raw)

    def _language_to_code(self, language: Language) -> typing.Union[str, typing.Any]:
        if language.id == "zho":
            return "zh-CN"
        elif language.id == "och":
            return "zh-TW"
        return language.alpha2

    def _code_to_language(self, code: typing.Union[str, typing.Any]) -> Language:
        language_code = str(code).lower()
        if language_code == "zh-cn":
            return Language("zho")
        elif language_code == "zh-tw":
            return Language("och")
        return Language(language_code)

    def __str__(self) -> str:
        return "Google Translate (API)"
