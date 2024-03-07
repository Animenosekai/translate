"""
Promt Translate

This implementation, based on a reverse-engineered Android client, was created by 'Zhymabek Roman' specifically for translatepy.
"""
import re
import uuid
import hashlib
import xml.etree.ElementTree as ET
from warnings import warn

from translatepy.language import Language
from translatepy.translators.base import BaseTranslateException, BaseTranslator
from translatepy.utils.request import Request

PROMT_ACC_ID = "PMTAndroid"
PROMT_ACC_KEY = "C3FC7A3D-FE52-4063-B11C-1565C627B7AD"

# Source reverse engineered file: Slid.smal
class Slid:
    _index_prefix = {}
    _index_id = {}
    _index_rfc = {}
    _lang_name = {}

    def __init__(self, id, prefix, rfc_prefix, py_locale, beta=False, ocr_prefix=None):
        self.id = id
        self.prefix = prefix
        self.rfc_prefix = rfc_prefix
        self.py_locale = py_locale
        self.beta = beta
        self.ocr_prefix = ocr_prefix or py_locale

        # Populate indexes
        Slid._index_prefix[prefix] = self
        Slid._index_id[id] = self
        Slid._index_rfc[rfc_prefix] = self

    @classmethod
    def from_id(cls, id):
        return cls._index_id.get(id, "Unknown")

    @classmethod
    def from_prefix(cls, prefix):
        return cls._index_prefix.get(prefix.lower(), "Auto")

    @classmethod
    def from_rfc_prefix(cls, rfc_prefix):
        return cls._index_rfc.get(rfc_prefix.lower(), "Unknown")

    @classmethod
    def get_lang_name(cls, id):
        return cls._lang_name.get(id, "Unknown Language")


class PromtHelper:
    # register languages
    Auto = Slid(0, "a", "Auto", "")
    Unknown = Slid(-1, "", "", "")
    English = Slid(1, "e", "en", "en_US")
    Russian = Slid(2, "r", "ru", "ru_RU")
    German = Slid(4, "g", "de", "de_DE")
    French = Slid(8, "f", "fr", "fr_FR")
    Italian = Slid(16, "i", "it", "it_IT")
    Spanish = Slid(32, "s", "es", "es_ES")
    Portuguese = Slid(64, "p", "pt", "pt_PT")
    Ukrainian = Slid(128, "u", "uk", "uk_UA")
    Lithuanian = Slid(256, "l", "lt", "lt_LT")
    Chinese = Slid(512, "zh-cn", "zh-cn", "zh_CN")
    TChinese = Slid(1024, "zh-tw", "zh-tw", "zh_TW")
    EnglishUS = Slid(1025, "en_us", "en_us", "en_US")
    EnglishGB = Slid(1026, "en_gb", "en_gb", "en_GB")
    Latvian = Slid(1027, "lv", "lv", "lv_LV")
    Polish = Slid(1028, "pl", "pl", "pl_PL")
    Kazakh = Slid(1029, "kz", "kk", "kk_KZ")
    Japanese = Slid(1030, "ja", "ja", "ja_JP")
    Dutch = Slid(1031, "nl", "nl", "nl_NL")
    Turkish = Slid(1032, "t", "tr", "tr_TR")
    Swedish = Slid(1033, "sv", "sv", "sv_SE")
    Norwegian = Slid(1034, "no", "no", "no_NO")
    Danish = Slid(1035, "da", "da", "da_DK")
    EnglishCA = Slid(1036, "en_ca", "en_ca", "en_CA")
    Bulgarian = Slid(1037, "bg", "bg", "bg_BG")
    Finnish = Slid(1038, "fi", "fi", "fi_FI")
    Arabic = Slid(1039, "ar", "ar", "ar_AR")
    Korean = Slid(1040, "ko", "ko", "ko_KR")
    SpanishMX = Slid(1041, "es_mx", "es_mx", "es_MX")
    FrenchCA = Slid(1042, "fr_ca", "fr_ca", "fr_CA")
    EnglishAU = Slid(1043, "en_au", "en_au", "en_AU")
    Greek = Slid(1047, "el", "el", "el_GR")
    Estonian = Slid(1048, "et", "et", "et_EE")
    Hungarian = Slid(1049, "hu", "hu", "hu_HU")
    Armenian = Slid(1050, "hy", "hy", "hy_AM")
    Georgian = Slid(1051, "ka", "ka", "ka_GE")
    Romanian = Slid(1052, "ro", "ro", "ro_RO")
    Slovak = Slid(1053, "sk", "sk", "sk_SK")
    Uzbek = Slid(1054, "uz", "uz", "uz_UZ")
    Vietnamese = Slid(1055, "vi", "vi", "vi_VN")
    Azeri = Slid(1056, "az", "az", "az_AZ")
    Hebrew = Slid(1057, "he", "he", "he_IL")
    Catalan = Slid(1058, "ca", "ca", "ca_ES")
    Czech = Slid(1059, "cs", "cs", "cs_CZ")
    HaitianCreole = Slid(1060, "ht", "ht", "ht_HT")
    Hindi = Slid(1061, "hi", "hi", "hi_IN")
    HmongDaw = Slid(1062, "mww", "mww", "mww_MWW")
    Indonesian = Slid(1063, "id", "id", "id_ID")
    Klingon = Slid(1064, "tlh", "tlh", "tlh_TLH")
    Klingon_pIqaD = Slid(1065, "tlh_Qaak", "tlh_Qaak", "tlh_Qaak")
    Malay = Slid(1066, "ms", "ms", "ms_MY")
    Maltese = Slid(1067, "mt", "mt", "mt_MT")
    Persian = Slid(1068, "fa", "fa", "fa_IR")
    Slovenian = Slid(1069, "sl", "sl", "sl_SI")
    Thai = Slid(1070, "th", "th", "th_TH")
    Urdu = Slid(1071, "ur", "ur", "ur_PK")
    Welsh = Slid(1072, "cy", "cy", "cy_CY")

    def _get_supported_languages(self):
        _languages_list = {Slid._index_rfc[rfc].rfc_prefix for rfc in Slid._index_rfc}
        _languages_list.add("auto")
        return _languages_list

    @staticmethod
    def _parse_language_pair(language_pair: str):
        if len(language_pair) == 2:
            source_language_code = language_pair[0]
            destination_language_code = language_pair[1]
        else:
            # Adjusted pattern to correctly match "[fi]e", "r[kz]", and "[zh-cn]e"
            match = re.match(r"(?:\[([a-z-]+)\]|([a-z]))(?:\[([a-z-]+)\]|([a-z]))", language_pair)
            if match:
                source_language_code = match.group(1) if match.group(1) else match.group(2)
                destination_language_code = match.group(3) if match.group(3) else match.group(4)
            else:
                raise ValueError(f"Invalid language pair: {language_pair}")

        source_language = Slid.from_prefix(source_language_code).rfc_prefix
        destination_language = Slid.from_prefix(destination_language_code).rfc_prefix

        return source_language, destination_language


class PromtTranslate(BaseTranslator):
    """
    Promt Translate Implementation.

    !!!Attention!!! Do not modify the order of the headers, as it may result in a "Bad request" error from the server. This is due to certain legacy server constraints.
    """

    _helper = PromtHelper()
    _soap_endpoint_url = "https://www.translate.ru/services/9.0/Translator.asmx"
    _supported_languages = _helper._get_supported_languages()
    _language_pair = {}

    def __init__(self, request: Request = Request()):
        self.session = request
        self.session_req_id = None

        self._initialize()
        if not self._language_pair:
            self._generate_lang_pair()

    def _initialize(self) -> str:
        headers = {
                'Host': 'www.translate.ru',
                'Connection': 'Keep-Alive',
                'Content-Type': 'text/xml; charset=utf-8',
                'SOAPAction': '"http://tempuri.org/Initialize"',
        }

        payload = "<?xml version=\"1.0\" encoding=\"utf-8\"?><soap:Envelope xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\">\t<soap:Body><Initialize xmlns=\"http://tempuri.org/\">\t<lang>en</lang></Initialize>\t</soap:Body></soap:Envelope>"

        request = self.session.post(self._soap_endpoint_url, headers=headers, data=payload)
        self._set_req_id(request.content)

    def _set_req_id(self, content: str) -> str:
        root = ET.fromstring(content)
        req_id_element = root.find('.//reqId')
        if not req_id_element.text:
            return
        self.session_req_id = req_id_element.text
        return req_id_element.text

    def _generate_auth_headers(self):
        auth_headers = {"PROMT-REQID": self.session_req_id, "PROMT-CODE": hashlib.md5((PROMT_ACC_ID + self.session_req_id + PROMT_ACC_KEY).encode('utf-8')).hexdigest(), "PROMT-ACCID": PROMT_ACC_ID}
        return auth_headers

    def _generate_lang_pair(self):
        service_response = self._get_service()
        root = ET.fromstring(service_response)
        directions = root.findall('.//direction')
        for direction in directions:
            direction_code = direction.find('id').text
            direction_pair = PromtHelper._parse_language_pair(direction_code)
            
            self._language_pair.update({f"{direction_pair[0]}-{direction_pair[1]}": direction_code})

    def _get_service(self) -> str:
        auth_headers = self._generate_auth_headers()
        headers = {**auth_headers, **{
                'Host': 'www.translate.ru',
                'Connection': 'Keep-Alive',
                'Content-Type': 'text/xml; charset=utf-8',
                'SOAPAction': '"http://tempuri.org/GetServices"',
        }}

        payload = "<?xml version=\"1.0\" encoding=\"utf-8\"?><soap:Envelope xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\">\t<soap:Body><GetServices xmlns=\"http://tempuri.org/\">\t<lang>en</lang></GetServices>\t</soap:Body></soap:Envelope>"

        request = self.session.post(self._soap_endpoint_url, headers=headers, data=payload)
        self._set_req_id(request.content)
        return request.content

    def _translate(self, text: str, destination_language: str, source_language: str) -> str:
        if source_language == "auto":
            source_language = "a"

            destination_language = Slid.from_rfc_prefix(destination_language).prefix
            language_pair = f"{source_language}{destination_language}"
        else:
            language_pair = self._language_pair.get(f"{source_language}-{destination_language}")

        if not language_pair:
            raise BaseTranslateException("Language pair not supported")

        auth_headers = self._generate_auth_headers()
        headers = {**auth_headers, **{
                'Host': 'www.translate.ru',
                'Connection': 'Keep-Alive',
                'Content-Type': 'text/xml; charset=utf-8',
                'SOAPAction': '"http://tempuri.org/Translate"',
        }}

        # TODO: refactor
        text = text.replace("&", "&amp;")
        text = text.replace("<", "&lt;")
        text = text.replace(">", "&gt;")
        text = text.replace('\"', "&quot;")
        text = text.replace("\'", "&#39;")

        payload = f"<?xml version=\"1.0\" encoding=\"utf-8\"?><soap:Envelope xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\">\t<soap:Body><Translate xmlns=\"http://tempuri.org/\">\t<dirCode>{language_pair}</dirCode>\t<tmplCode>General</tmplCode>\t<sText>{text}</sText>\t<format>word</format><paramsXML>&lt;params&gt;&lt;param&gt;&lt;id&gt;1&lt;/id&gt;&lt;name&gt;Roaming&lt;/name&gt;&lt;value&gt;off&lt;/value&gt;&lt;/param&gt;&lt;param&gt;&lt;id&gt;2&lt;/id&gt;&lt;name&gt;MinimizeTrafficInRoaming&lt;/name&gt;&lt;value&gt;off&lt;/value&gt;&lt;/param&gt;&lt;param&gt;&lt;id&gt;3&lt;/id&gt;&lt;name&gt;TextSource&lt;/name&gt;&lt;value&gt;TEXT&lt;/value&gt;&lt;/param&gt;&lt;/params&gt;</paramsXML>\t<lang>en</lang></Translate>\t</soap:Body></soap:Envelope>"
        request = self.session.post(self._soap_endpoint_url, headers=headers, data=payload)
        self._set_req_id(request.content)

        try:
            root = ET.fromstring(request.text)
            c = root.find('.//strResult').text

            try:
                cdata = ET.fromstring(c)
                translation = cdata.findall(".//translation")[0].find("result").text
            except Exception as ex:
                translation = c

            translation = translation.replace("&amp;", "&")
            translation = translation.replace("&lt;", "<")
            translation = translation.replace("&gt;", ">")
            translation = translation.replace("&quot;", "\"")
            translation = translation.replace("&#39;", "'")
        except Exception as ex:
            warn(f"Can't parse result. Exception: {ex}. Response: {request.text}. Try to set source language manually instead of automatic")
            translation = None

        if source_language == "a":
            source_language = "auto"

        return source_language, translation

    def _language_normalize(self, language):
        return language.alpha2

    def _language_denormalize(self, language_code):
        return Language(language_code)

    def __str__(self) -> str:
        return "Promt"
