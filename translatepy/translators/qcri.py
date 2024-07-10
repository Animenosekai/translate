"""
translatepy's implementation of <QCRI>
"""
import typing
import json

from translatepy import exceptions, models
from translatepy.language import Language
from translatepy.translators.base import (BaseTranslateException,
                                          BaseTranslator, C)
from translatepy.utils import request

from bs4 import BeautifulSoup


class QCRIException(BaseTranslateException):
    error_codes = {
        429: "Too many requests"  # add your own status codes and error
    }

    # you can use it like so in your endpoint:
    # raise TranslateNameException(request.status_code)


class QCRI(BaseTranslator):
    """
    translatepy's implementation of <QCRI>
    """

    _supported_languages = {"es", "en", "ar"}
    _base_url = "https://mt.qcri.org/api/v1/{endpoint}"

    def __init__(self, session: typing.Optional[request.Session] = None):
        super().__init__(session)
        page_request = self.session.get("https://mt.qcri.org/api")
        page_request.raise_for_status()
        soup = BeautifulSoup(page_request.text, "html.parser")
        script = soup.find("script", attrs={"type": "text/javascript"})

        self.lang_pairs = None
        self.api_key = None
        for line in str(script.text).lower().replace(" ", "").splitlines():
            try:
                if line.startswith("varglobal_langpairs"):
                    _, _, parsing = line.partition("=")
                    parsing = parsing[:-1]
                    self.lang_pairs = json.loads(parsing)
            except Exception:
                pass
            if line.startswith("vartranslationkey"):
                _, _, parsing = line.partition("=")
                self.api_key = parsing[:-1].strip('"')

        if self.api_key is None:
            raise RuntimeError("Couldn't get the API key")

        try:
            if self.lang_pairs:
                self._supported_languages.clear()
                for lang_pair in self.lang_pairs:
                    source, _, dest = lang_pair.partition("-")
                    self._supported_languages.add(source)
                    self._supported_languages.add(dest)
        except Exception:
            pass

    def _translate(self: C, text: str, dest_lang: typing.Any, source_lang: typing.Any, domain: str = "general") -> models.TranslationResult[C]:
        request = self.session.get(self._base_url.format(endpoint="translate"), params={
            "key": self.api_key,
            "langpair": "{}-{}".format(source_lang, dest_lang),
            "domain": domain,  # can be changed
            "text": text
        })
        request.raise_for_status()
        data = request.json()
        if not data["success"]:
            raise ValueError("Couldn't retrieve a suitable response")
        return models.TranslationResult(raw=data, translation=data["translatedText"])

    def _code_to_language(self, code: typing.Union[str, typing.Any]) -> Language:
        return Language(code)

    def _language_to_code(self, language: Language) -> typing.Union[str, typing.Any]:
        return language.alpha2

    def __str__(self) -> str:
        return "QCRI"
