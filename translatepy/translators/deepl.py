"""
DeepL

About the translation and the language endpoints:
    This implementation of DeepL follows Marocco2's implementation of DeepL's JSONRPC API\n
    Arrangements and optimizations have been made\n
    Refer to Issue Animenosekai/translate#7 on GitHub for further details

© Anime no Sekai — 2021
"""

from time import time
from re import compile
from typing import Union
from random import randint
from json import loads, dumps

import requests
import pyuseragents
from bs4 import BeautifulSoup

from translatepy.models.languages import Language
from translatepy.utils.annotations import Tuple, Dict

SENTENCES_SPLITTING_REGEX = compile('(?<=[.!:?]) +')

class getClientState():
    def __init__(self):
        self.id_number = randint(100, 9999) * 10000
        self.user_agent = pyuseragents.random()
        self.headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Host": "www.deepl.com",
            "Connection": "keep-alive",
            "Referer": "https://www.deepl.com/translator",
            "Content-Type": "application/json",
            "User-Agent": self.user_agent
        }

    def dump(self):
        self.id_number += 1
        data = {
            "id": self.id_number,
            "jsonrpc": "2.0",
            "method": "getClientState",
            "params": {
                "v": "20180814"
            }
        }
        return data

    def get(self):
        """
        Returns a new Client State ID
        """

        """ NO SUPPORT FOR PROXIES FOR NOW
        proxies = None
        _proxies = {}
        if proxies:
            try:
                _proxies["http"] = proxies["http"]
                _proxies["https"] = proxies["https"]
            except Exception:
                proxies = str(proxies)
                _proxies["http"] = proxies
                _proxies["https"] = proxies
        resp = loads(requests.post("https://www.deepl.com/PHP/backend/clientState.php?request_type=jsonrpc&il=EN", data=self.dump(), headers=self.headers, proxies=_proxies).content)
        """

        resp = loads(requests.post("https://www.deepl.com/PHP/backend/clientState.php?request_type=jsonrpc&il=EN", data=dumps(self.dump()).encode("utf-8"), headers=self.headers).content)
        return resp.get("id", None)



class JSONRPCRequest():
    """
    JSONRPC Request Sender for DeepL
    """
    def __init__(self) -> None:
        self.client_state = getClientState()
        self.headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Host": "www2.deepl.com",
            "Origin": "https://www.deepl.com",
            "Referer": "https://www.deepl.com/",
            "Content-Type": "application/json",
            "User-Agent": self.client_state.user_agent
        }
        self.id_number = self.client_state.get()
        if not self.id_number:
            self.id_number = 1

    def dump(self, method, params):
        self.id_number += 1
        data = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params,
            "id": self.id_number
        }
        return data

    def send_jsonrpc(self, method, params):
        try:
            resp = loads(requests.post("https://www2.deepl.com/jsonrpc", data=dumps(self.dump(method, params)).encode("utf-8"), headers=self.headers).content)
            return resp.get("result", None)
        except Exception:
            return None


class DeepL():
    def __init__(self, preferred_langs=None) -> None:
        self.jsonrpc = JSONRPCRequest()
        self.user_preferred_langs = ([] if preferred_langs is None else preferred_langs)

    def split_into_sentences(self, text, destination_language, source_language) -> Union[Tuple[list[str], str], Tuple[list[str], None]]:
        """
        Split a string into sentences using the DeepL API.\n
        Fallbacks to a simple Regex splitting if an error occurs or no result is found

        Returned tuple: (Result, Computed Language (None if same as source_language))
        """
        params = {
            "texts": [text.strip()],
            "lang": {
                "lang_user_selected": source_language,
                "user_preferred_langs": list(set(self.user_preferred_langs + [destination_language]))
            }
        }
        resp = self.jsonrpc.send_jsonrpc("LMT_split_into_sentences", params)

        if resp is not None:
            if source_language != resp["lang"]:
                return resp["splitted_texts"][0], resp["lang"]
            
            return resp["splitted_texts"][0], None
            
        return SENTENCES_SPLITTING_REGEX.split(text), None

    def translate(self, text, destination_language, source_language=None, priority=1, quality="", compute_splitting=False) -> Union[Tuple[str, str], Tuple[None, None]]:
        """
        Translates the given text to the given language

        Args:
          text: A string corresponding to the given text
          destination_language: The destination language
          source_language: Default value = None
          priority: The DeepL API priority, Default value = 1
          quality: The DeepL API quality, Default value = "" (excludes the quality parameter from the request)
          compute_splitting: Wether translatepy should ask to split the sentences to the DeepL API or it should split it using Regex, Default value = False

        Returns:
            Tuple(str, str) --> tuple with source_lang, translation
            None, None --> when an error occurs

        """
        try:
            if isinstance(destination_language, Language):
                destination_language = destination_language.deepl
            if isinstance(source_language, Language):
                source_language = source_language.deepl
            elif source_language is None:
                source_language = "AUTO"
            
            text = str(text)

            # splitting the text into sentences
            if compute_splitting:
                sentences, computed_lang = self.split_into_sentences(text, destination_language, source_language)
            else:
                sentences = SENTENCES_SPLITTING_REGEX.split(text)
                computed_lang = None

            # building the a job per sentence
            jobs = _build_jobs(sentences, quality)

            # timestamp generation
            i_count = 1
            for sentence in sentences:
                i_count += sentence.count("i")
            ts = int(time() * 10) * 100 + 1000

            # params building
            params = {
                "jobs": jobs,
                "lang": {
                    "target_lang": destination_language,
                    "user_preferred_langs": [destination_language]
                },
                "priority": priority,
                "timestamp": ts + (i_count - ts % i_count)
            }

            if computed_lang is not None:
                params["lang"]["source_lang_computed"] = computed_lang
                params["lang"]["user_preferred_langs"].append(computed_lang)
            else:
                params["lang"]["source_lang_user_selected"] = source_language

            results = self.jsonrpc.send_jsonrpc("LMT_handle_jobs", params)

            if results is not None:
                translations = results["translations"]
                return results["source_lang"], " ".join(obj["beams"][0]["postprocessed_sentence"] for obj in translations if obj["beams"])
            return None, None
        except:
            return None, None

    def language(self, text, priority=1, quality="", compute_splitting=False) -> Union[str, None]:
        """
        Gives out the language of the given text

        Args:
          text: A string corresponding to the given text

        Returns:
            str --> the language code
            None --> when an error occurs

        """
        text = str(text)

        try:

            # splitting the text into sentences
            if compute_splitting:
                sentences, computed_lang = self.split_into_sentences(text, "AUTO", "EN")
            else:
                sentences = SENTENCES_SPLITTING_REGEX.split(text)
                computed_lang = None

            # building the a job per sentence
            jobs = _build_jobs(sentences, quality)

            # timestamp generation
            i_count = 1
            for sentence in sentences:
                i_count += sentence.count("i")
            ts = int(time() * 10) * 100 + 1000

            # params building
            params = {
                "jobs": jobs,
                "lang": {
                    "target_lang": "EN",
                    "user_preferred_langs": ["EN"]
                },
                "priority": priority,
                "timestamp": ts + (i_count - ts % i_count)
            }

            if computed_lang is not None:
                params["lang"]["source_lang_computed"] = computed_lang
                params["lang"]["user_preferred_langs"].append(computed_lang)
            else:
                params["lang"]["source_lang_user_selected"] = "AUTO"

            results = self.jsonrpc.send_jsonrpc("LMT_handle_jobs", params)

            if results is not None:
                return results["source_lang"]
            return None
        except:
            return None


    def dictionary(self, text, destination_language, source_language=None) -> Union[Tuple[str, Dict], Tuple[None, None]]:
        """
        Gives out a list of translations
        
        > destination_language and source_language both need to be the full english name

        Args:
          text: param destination_language:
          source_language: Default value = None)
          destination_language: 

        Returns:
            Tuple(str, Dict({
                featured: featured translations,
                less_common: less common translations,
                _html: the raw HTML response,
                _response: the BeautifulSoup object for the given HTML
            })) --> tuple with source_lang, results
            None, None --> when an error occurs

        """
        try:
            if isinstance(destination_language, Language):
                dl = destination_language.english
                if dl is None:
                    dl = destination_language.name
                destination_language = dl
            if isinstance(source_language, Language):
                sl = source_language.english
                if sl is None:
                    sl = source_language.name
                source_language = sl

            if source_language is None or source_language == "auto":
                source_language = self.language(text)
                if source_language is None:
                    return None, None
                try:
                    source_language = Language(source_language).english
                except Exception:
                    return None, None

            request = requests.post("https://dict.deepl.com/" + str(source_language) + "-" + str(destination_language) + "/search?ajax=1&source=" + str(source_language) + "&onlyDictEntries=1&translator=dnsof7h3k2lgh3gda&delay=800&jsStatus=0&kind=full&eventkind=keyup&forleftside=true", data={"query": str(text)})
            if request.status_code < 400:
                response = BeautifulSoup(request.text, "html.parser")
                results = {}
                results["_html"] = request.text
                results["_response"] = response
                results["featured"] = []
                results["less_common"] = []
                for element in response.find_all("a"):
                    if element.has_attr('class'):
                        if "dictLink" in element["class"]:
                            if "featured" in element["class"]:
                                results["featured"].append(str(element.text).replace("\n", ""))
                            else:
                                results["less_common"].append(str(element.text).replace("\n", ""))
                return source_language, results
            else:
                print(request.text)
                return None, None
        except Exception:
            return None, None


def _build_jobs(sentences, quality=""):
    """
    Builds a job for each sentence for DeepL
    """
    jobs = []
    for index, sentence in enumerate(sentences):
        if index == 0:
            try:
                before = []
                after = [sentences[index + 1]]
            except IndexError: # index == len(sentences) - 1
                before = []
                after = []
        else:
            if len(before) > 4:
                before.pop(0) # the "before" array cannot be more than 5 elements long i guess?
            before.extend([sentences[index - 1]])
            if index > len(sentences) - 2:
                after = []
            else:
                after = [sentences[index + 1]]

        job = {
            "kind": "default",
            "raw_en_context_after": after.copy(),
            "raw_en_context_before": before.copy(),
            "raw_en_sentence": sentence,
        }
        if quality != "":
            job["quality"] = quality
        jobs.append(job)

    return jobs