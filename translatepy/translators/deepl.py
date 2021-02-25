from typing import Union
from translatepy.models.languages import Language
from requests import post
from json import loads
from time import time
from traceback import print_exc
from bs4 import BeautifulSoup
from warnings import warn

class NotImplementYet(Warning):
    """ """
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


# not in use for now
FROM = ['auto', 'zh', 'nl', 'en', 'fr', 'de', 'it', 'ja', 'pl', 'pt', 'ru', 'es']
TO = ['en-US', 'en-GB', 'zh-ZH', 'nl-NL', 'fr-FR', 'de-DE', 'it-IT', 'ja-JA', 'pl-PL', 'pt-PT', 'pt-BR', 'ru-RU', 'es-ES']
FORMALITY_SUPPORT = ['nl-NL', 'fr-FR', 'de-DE', 'it-IT', 'pl-PL', 'pt-PT', 'pt-BR', 'ru-RU', 'es-ES']
FORMALITY = [
    ["Formal tone", "formal"],
    ["Informal tone", "informal"],
    ["Automatic", "auto"]
]

class DeepL():
    """A Python implementation of DeepL APIs"""
    def __init__(self) -> None:
        pass

    def translate(self, text, destination_language, source_language="auto", formality=None) -> Union[tuple[str, str], tuple[None, None]]:
        """
        Translates the given text to the given language

        Args:
          text: param destination_language:
          source_language: Default value = "auto")
          formality: Default value = None)
          destination_language: 

        Returns:
            Tuple(str, str) --> tuple with source_lang, translation
            None, None --> when an error occurs

        """
        try:
            if isinstance(destination_language, Language):
                destination_language = destination_language.deepl
            if isinstance(source_language, Language):
                source_language = source_language.deepl
            
            if formality is not None:
                warning_message = "[translatepy] Warning: formality has not been implemented yet and won't have any effect to the translation"
                warn(NotImplementYet(warning_message))
            if source_language is None:
                source_language = "auto"
            payload = {"jsonrpc":"2.0","method": "LMT_handle_jobs","params":{"jobs":[{"kind":"default","raw_en_sentence":str(text),"raw_en_context_before":[],"raw_en_context_after":[],"preferred_num_beams":4,"quality":"fast"}],"lang":{"user_preferred_langs":["JA","FR","EN"],"source_lang_user_selected":str(source_language),"target_lang":str(destination_language)},"priority":-1,"commonJobParams":{},"timestamp":int(time())},"id":63710028}
            request = post("https://www2.deepl.com/jsonrpc", json=payload, cookies={})
            if request.status_code < 400:
                data = loads(request.text)
                return data["result"]["source_lang"], data["result"]["translations"][0]["beams"][0]["postprocessed_sentence"]
            else:
                print(request.text)
                return None, None
        except:
            print_exc()
            return None, None

    def dictionary(self, text, destination_language, source_language=None) -> Union[tuple[str, dict], tuple[None, None]]:
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
                except:
                    return None, None

            request = post("https://dict.deepl.com/" + str(source_language) + "-" + str(destination_language) + "/search?ajax=1&source=" + str(source_language) + "&onlyDictEntries=1&translator=dnsof7h3k2lgh3gda&delay=800&jsStatus=0&kind=full&eventkind=keyup&forleftside=true", data={"query": str(text)})
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
        except:
            print_exc()
            return None, None

    def language(self, text) -> Union[str, None]:
        """
        Gives out the language of the given text

        Args:
          text: 

        Returns:
            str --> the language code
            None --> when an error occurs

        """
        try:
            payload = {"jsonrpc":"2.0","method": "LMT_handle_jobs","params":{"jobs":[{"kind":"default","raw_en_sentence":str(text),"raw_en_context_before":[],"raw_en_context_after":[],"preferred_num_beams":4,"quality":"fast"}],"lang":{"user_preferred_langs":["JA","FR","EN"],"source_lang_user_selected":"auto","target_lang":"JA","priority":-1,"commonJobParams":{},"timestamp":int(time())},"id":63710028}}
            request = post("https://www2.deepl.com/jsonrpc", json=payload, cookies={})
            if request.status_code < 400:
                data = loads(request.text)
                return data["result"]["source_lang"]
            else:
                print(request.text)
                return None
        except:
            print_exc()
            return None


    def __repr__(self) -> str:
        return "DeepL Translate"
