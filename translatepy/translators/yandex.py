"""
Yandex Translate

This implementation was made specifically for translatepy from 'Zhymabek Roman', based on 'Anime no Seka' version.

"""

from typing import Union
from urllib.parse import quote
import uuid

from requests import get, post

from translatepy.models.languages import Language
from translatepy.utils.annotations import Tuple
from translatepy.utils.lru_cacher import timed_lru_cache

# TODO: Implement getting a list of supported languages by querying Yandex Translate API request

HEADERS = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Referer": "https://translate.yandex.com/",
    "User-Agent": "ru.yandex.translate/3.20.2024"
}

TRANSLIT_LANGS = ['am', 'bn', 'el', 'gu', 'he', 'hi', 'hy', 'ja', 'ka', 'kn', 'ko', 'ml', 'mr', 'ne', 'pa', 'si', 'ta', 'te', 'th', 'yi', 'zh']


class YandexTranslate():
    """A Python implementation of Yandex Translation's APIs"""
    def __init__(self) -> None:
        self._base_url = "https://translate.yandex.net/api/v1/tr.json/"

    # TODO: Make @property
    @timed_lru_cache(60)  # Store UUID value within 60 seconds
    def _ucid(self) -> str:
        """
        Generates UUID (UCID) for Yandex Translate API requests (USID analogue)

        Args:

        Returns:
            str --> new generated UUID value
        """
        # Yandex Translate generally generates UUID V5, but API can accepts UUID V4 (bug or feature !?)
        _uuid = str(uuid.uuid4())
        _ucid = _uuid.replace("-", "")
        return _ucid

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
                    # TODO: Raise exception
                    return None, None
            if isinstance(source_language, Language):
                source_language = source_language.yandex_translate

            def _request():
                url = self._base_url + "translate?ucid=" + self._ucid() + "&srv=android" + "&format=text"
                request = post(url, headers=HEADERS, data={'text': str(text), 'lang': str(source_language) + "-" + str(destination_language)})
                data = request.json()
                if request.status_code < 400 and data["code"] == 200:
                    return str(data["lang"]).split("-")[0], data["text"][0]
                return None, None  # TODO: Raise exception by YT returned status code

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

            def _request(text):
                request = post("https://speller.yandex.net/services/spellservice.json/checkText?ucid=" + self._ucid() + "&srv=android", headers=HEADERS, data={'text': str(text), 'lang': source_language, 'options': 516})
                if request.status_code < 400:
                    data = request.json()
                    for correction in data:
                        text = text[:correction.get("pos", 0)] + correction.get("s", [""])[0] + text[correction.get("pos", 0) + correction.get("len", 0):]
                    return source_language, text
                else:
                    return None, None

            _lang, _text = _request(text)

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

            text = quote(str(text), safe='')

            url = self._base_url + "detect?ucid=" + self._ucid() + "&srv=android&text=" + text + "&hint=" + str(hint)

            def _request():
                request = get(url, headers=HEADERS)
                data = request.json()
                if request.status_code < 400 and data["code"] == 200:
                    return data["lang"]
                else:
                    return None

            _lang = _request()

            return _lang
        except Exception:
            return None

    def __repr__(self) -> str:
        return "Yandex Translate"
