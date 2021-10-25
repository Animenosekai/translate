"""
translatepy v2.2

© Anime no Sekai — 2021
"""
from multiprocessing.pool import ThreadPool
from threading import Thread
from typing import Union

from bs4 import BeautifulSoup
from bs4.element import NavigableString, PageElement, PreformattedString, Tag

from translatepy.exceptions import NoResult, ParameterTypeError, ParameterValueError
from translatepy.language import Language
from translatepy.models import (DictionaryResult, ExampleResult,
                                LanguageResult, SpellcheckResult,
                                TextToSpechResult, TranslationResult,
                                TransliterationResult)
from translatepy.translators import (BaseTranslator, BingTranslate,
                                     DeeplTranslate, GoogleTranslate,
                                     LibreTranslate, MyMemoryTranslate,
                                     ReversoTranslate, TranslateComTranslate,
                                     YandexTranslate)
from translatepy.utils.annotations import List
from translatepy.utils.queue import Queue
from translatepy.utils.request import Request
from translatepy.utils.sanitize import remove_spaces


class Translate():
    """
    A class which groups all of the APIs
    """

    def __init__(
        self,
        services_list: List[BaseTranslator] = [
            GoogleTranslate,
            BingTranslate,
            YandexTranslate,
            ReversoTranslate,
            DeeplTranslate,
            LibreTranslate,
            TranslateComTranslate,
            MyMemoryTranslate
        ],
        request: Request = Request(),
        fast: bool = False
    ) -> None:
        """
        A special Translator class grouping multiple translators to have better results.

        Parameters:
        ----------
            services_list : list
                A list of instanciated or not BaseTranslator subclasses to use as translators
            request : Request
                The Request class used to make requests
            fast : bool
                Enabling fast mode (concurrent processing) or not
        """

        if not isinstance(services_list, List):
            raise ParameterTypeError("Parameter 'services_list' must be a list, {} was given".format(type(services_list).__name__))

        if not services_list:
            raise ParameterValueError("Parameter 'services_list' must not be empty")

        self.FAST_MODE = fast

        if isinstance(request, type):  # is not instantiated
            self.request = request()
        else:
            self.request = request

        self.services = []
        for service in services_list:
            if not isinstance(service, BaseTranslator):  # not instantiated
                if not issubclass(service, BaseTranslator):
                    raise ParameterTypeError("{service} must be a child class of the BaseTranslator class".format(service=service))
            self.services.append(service)

    def _instantiate_translator(self, service: BaseTranslator, services_list: list, index: int):
        if not isinstance(service, BaseTranslator):  # not instantiated
            if "request" in service.__init__.__code__.co_varnames:  # check if __init__ wants a request parameter
                service = service(request=self.request)
            else:
                service = service()
            services_list[index] = service
        return service

    def translate(self, text: str, destination_language: str, source_language: str = "auto") -> TranslationResult:
        """
        Translates the given text to the given language

        i.e Good morning (en) --> おはようございます (ja)
        """
        dest_lang = Language(destination_language)
        source_lang = Language(source_language)

        def _translate(translator: BaseTranslator, index: int):
            translator = self._instantiate_translator(translator, self.services, index)
            result = translator.translate(
                text=text, destination_language=dest_lang, source_language=source_lang
            )
            if result is None:
                raise NoResult("{service} did not return any value".format(service=translator.__repr__()))
            return result

        def _fast_translate(queue: Queue, translator: BaseTranslator, index: int):
            try:
                queue.put(_translate(translator=translator, index=index))
            except Exception:
                pass

        if self.FAST_MODE:
            _queue = Queue()
            threads = []
            for index, service in enumerate(self.services):
                thread = Thread(target=_fast_translate, args=(_queue, service, index))
                thread.start()
                threads.append(thread)
            result = _queue.get(threads=threads)  # wait for a value and return it
            if result is None:
                raise NoResult("No service has returned a valid result")
            return result

        for index, service in enumerate(self.services):
            try:
                return _translate(translator=service, index=index)
            except Exception:
                continue
        else:
            raise NoResult("No service has returned a valid result")

    def translate_html(self, html: Union[str, PageElement, Tag, BeautifulSoup], destination_language: str, source_language: str = "auto", parser: str = "html.parser", threads_limit: int = 100) -> Union[str, PageElement, Tag, BeautifulSoup]:
        """
        Translates the given HTML string or BeautifulSoup object to the given language

        i.e
         English: `<div class="hello"><h1>Hello</h1> everyone and <a href="/welcome">welcome</a> to <span class="w-full">my website</span></div>`
         French: `<div class="hello"><h1>Bonjour</h1>tout le monde et<a href="/welcome">Bienvenue</a>à<span class="w-full">Mon site internet</span></div>`

        Note: This method is not perfect since it is not tag/context aware. Example: `<span>Hello <strong>everyone</strong></span>` will not be understood as
        "Hello everyone" with "everyone" in bold but rather "Hello" and "everyone" separately.

        Warning: If you give a `bs4.BeautifulSoup`, `bs4.element.PageElement` or `bs4.element.Tag` input (which are mutable), they will be modified.
        If you don't want this behavior, please make sure to pass the string version of the element:
        >>> result = Translate().translate_html(str(page_element), "French")

        Parameters:
        ----------
            html : str | bs4.element.PageElement | bs4.element.Tag | bs4.BeautifulSoup
                The HTML string to be translated. This can also be an instance of BeautifulSoup's `BeautifulSoup` element, `PageElement` or `Tag` element.
            destination_language : str
                The language the HTML string needs to be translated in.
            source_language : str, default = "auto"
                The language of the HTML string.
            parser : str, default = "html.parser"
                The parser that BeautifulSoup will use to parse the HTML string.
            threads_limit : int, default = 100
                The maximum number of threads that will be spawned by translate_html

        Returns:
        --------
            BeautifulSoup:
                The result will be the same element as the input `html` parameter with the values modified if the given
                input is of bs4.BeautifulSoup, bs4.element.PageElement or bs4.element.Tag instance.
            str:
                The result will be a string in any other case.

        """
        dest_lang = Language(destination_language)
        source_lang = Language(source_language)

        def _translate(node: NavigableString):
            try:
                node.replace_with(self.translate(str(node), destination_language=dest_lang, source_language=source_lang).result)
            except Exception:  # ignore if it couldn't find any result or an error occured
                pass

        if not isinstance(html, (PageElement, Tag, BeautifulSoup)):
            page = BeautifulSoup(str(html), str(parser))
        else:
            page = html
        # nodes = [tag.text for tag in page.find_all(text=True, recursive=True, attrs=lambda class_name: "notranslate" not in str(class_name).split()) if not isinstance(tag, (PreformattedString)) and remove_spaces(tag) != ""]
        nodes = [tag for tag in page.find_all(text=True, recursive=True) if not isinstance(tag, (PreformattedString)) and remove_spaces(tag) != ""]
        with ThreadPool(int(threads_limit)) as pool:
            pool.map(_translate, nodes)
        return page if isinstance(html, (PageElement, Tag, BeautifulSoup)) else str(page)

    def transliterate(self, text: str, destination_language: str = "en", source_language: str = "auto") -> TransliterationResult:
        """
        Transliterates the given text

        i.e おはよう --> Ohayou
        """
        dest_lang = Language(destination_language)
        source_lang = Language(source_language)

        def _transliterate(translator: BaseTranslator, index: int):
            translator = self._instantiate_translator(translator, self.services, index)
            result = translator.transliterate(
                text=text, destination_language=dest_lang, source_language=source_lang
            )
            if result is None:
                raise NoResult("{service} did not return any value".format(service=translator.__repr__()))
            return result

        def _fast_transliterate(queue: Queue, translator: BaseTranslator, index: int):
            try:
                queue.put(_transliterate(translator=translator, index=index))
            except Exception:
                pass

        if self.FAST_MODE:
            _queue = Queue()
            threads = []
            for index, service in enumerate(self.services):
                thread = Thread(target=_fast_transliterate, args=(_queue, service, index))
                thread.start()
                threads.append(thread)
            result = _queue.get(threads=threads)  # wait for a value and return it
            if result is None:
                raise NoResult("No service has returned a valid result")
            return result

        for index, service in enumerate(self.services):
            try:
                return _transliterate(translator=service, index=index)
            except Exception:
                continue
        else:
            raise NoResult("No service has returned a valid result")

    def spellcheck(self, text: str, source_language: str = "auto") -> SpellcheckResult:
        """
        Checks the spelling of a given text

        i.e God morning --> Good morning
        """
        source_lang = Language(source_language)

        def _spellcheck(translator: BaseTranslator, index: int):
            translator = self._instantiate_translator(translator, self.services, index)
            result = translator.spellcheck(
                text=text, source_language=source_lang
            )
            if result is None:
                raise NoResult("{service} did not return any value".format(service=translator.__repr__()))
            return result

        def _fast_spellcheck(queue: Queue, translator: BaseTranslator, index: int):
            try:
                queue.put(_spellcheck(translator=translator, index=index))
            except Exception:
                pass

        if self.FAST_MODE:
            _queue = Queue()
            threads = []
            for index, service in enumerate(self.services):
                thread = Thread(target=_fast_spellcheck, args=(_queue, service, index))
                thread.start()
                threads.append(thread)
            result = _queue.get(threads=threads)  # wait for a value and return it
            if result is None:
                raise NoResult("No service has returned a valid result")
            return result

        for index, service in enumerate(self.services):
            try:
                return _spellcheck(translator=service, index=index)
            except Exception:
                continue
        else:
            raise NoResult("No service has returned a valid result")

    def language(self, text: str) -> LanguageResult:
        """
        Returns the language of the given text

        i.e 皆さんおはようございます！ --> Japanese
        """
        def _language(translator: BaseTranslator, index: int):
            translator = self._instantiate_translator(translator, self.services, index)
            result = translator.language(
                text=text
            )
            if result is None:
                raise NoResult("{service} did not return any value".format(service=translator.__repr__()))
            return result

        def _fast_language(queue: Queue, translator: BaseTranslator, index: int):
            try:
                queue.put(_language(translator=translator, index=index))
            except Exception:
                pass

        if self.FAST_MODE:
            _queue = Queue()
            threads = []
            for index, service in enumerate(self.services):
                thread = Thread(target=_fast_language, args=(_queue, service, index))
                thread.start()
                threads.append(thread)
            result = _queue.get(threads=threads)  # wait for a value and return it
            if result is None:
                raise NoResult("No service has returned a valid result")
            return result

        for index, service in enumerate(self.services):
            try:
                return _language(translator=service, index=index)
            except Exception:
                continue
        else:
            raise NoResult("No service has returned a valid result")

    def example(self, text: str, destination_language: str, source_language: str = "auto") -> ExampleResult:
        """
        Returns a set of examples / use cases for the given word

        i.e Hello --> ['Hello friends how are you?', 'Hello im back again.']
        """
        dest_lang = Language(destination_language)
        source_lang = Language(source_language)

        def _example(translator: BaseTranslator, index: int):
            translator = self._instantiate_translator(translator, self.services, index)
            result = translator.example(
                text=text, destination_language=dest_lang, source_language=source_lang
            )
            if result is None:
                raise NoResult("{service} did not return any value".format(service=translator.__repr__()))
            return result

        def _fast_example(queue: Queue, translator: BaseTranslator, index: int):
            try:
                queue.put(_example(translator=translator, index=index))
            except Exception:
                pass

        if self.FAST_MODE:
            _queue = Queue()
            threads = []
            for index, service in enumerate(self.services):
                thread = Thread(target=_fast_example, args=(_queue, service, index))
                thread.start()
                threads.append(thread)
            result = _queue.get(threads=threads)  # wait for a value and return it
            if result is None:
                raise NoResult("No service has returned a valid result")
            return result

        for index, service in enumerate(self.services):
            try:
                return _example(translator=service, index=index)
            except Exception:
                continue
        else:
            raise NoResult("No service has returned a valid result")

    def dictionary(self, text: str, destination_language: str, source_language="auto") -> DictionaryResult:
        """
        Returns a list of translations that are classified between two categories: featured and less common

        i.e Hello --> {'featured': ['ハロー', 'こんにちは'], 'less_common': ['hello', '今日は', 'どうも', 'こんにちわ', 'こにちは', 'ほいほい', 'おーい', 'アンニョンハセヨ', 'アニョハセヨ'}
        """
        dest_lang = Language(destination_language)
        source_lang = Language(source_language)

        def _dictionary(translator: BaseTranslator, index: int):
            translator = self._instantiate_translator(translator, self.services, index)
            result = translator.dictionary(
                text=text, destination_language=dest_lang, source_language=source_lang
            )
            if result is None:
                raise NoResult("{service} did not return any value".format(service=translator.__repr__()))
            return result

        def _fast_dictionary(queue: Queue, translator: BaseTranslator, index: int):
            try:
                queue.put(_dictionary(translator=translator, index=index))
            except Exception:
                pass

        if self.FAST_MODE:
            _queue = Queue()
            threads = []
            for index, service in enumerate(self.services):
                thread = Thread(target=_fast_dictionary, args=(_queue, service, index))
                thread.start()
                threads.append(thread)
            result = _queue.get(threads=threads)  # wait for a value and return it
            if result is None:
                raise NoResult("No service has returned a valid result")
            return result

        for index, service in enumerate(self.services):
            try:
                return _dictionary(translator=service, index=index)
            except Exception:
                continue
        else:
            raise NoResult("No service has returned a valid result")

    def text_to_speech(self, text: str, speed: int = 100, gender: str = "female", source_language: str = "auto") -> TextToSpechResult:
        """
        Gives back the text to speech result for the given text

        Args:
          text: the given text
          source_language: the source language

        Returns:
            the mp3 file as bytes

        Example:
            >>> from translatepy import Translator
            >>> t = Translator()
            >>> result = t.text_to_speech("Hello, how are you?")
            >>> with open("output.mp3", "wb") as output: # open a binary (b) file to write (w)
            ...     output.write(result.result)
                    # or:
                    result.write_to_file(output)
            # Or you can just use write_to_file method:
            >>> result.write_to_file("output.mp3")
            >>> print("Output of Text to Speech is available in output.mp3!")

            # the result is an MP3 file with the text to speech output
        """
        source_lang = Language(source_language)

        def _text_to_speech(translator: BaseTranslator, index: int):
            translator = self._instantiate_translator(translator, self.services, index)
            result = translator.text_to_speech(
                text=text, speed=speed, gender=gender, source_language=source_lang
            )
            if result is None:
                raise NoResult("{service} did not return any value".format(service=translator.__repr__()))
            return result

        def _fast_text_to_speech(queue: Queue, translator: BaseTranslator, index: int):
            try:
                queue.put(_text_to_speech(translator=translator, index=index))
            except Exception:
                pass

        if self.FAST_MODE:
            _queue = Queue()
            threads = []
            for index, service in enumerate(self.services):
                thread = Thread(target=_fast_text_to_speech, args=(_queue, service, index))
                thread.start()
                threads.append(thread)
            result = _queue.get(threads=threads)  # wait for a value and return it
            if result is None:
                raise NoResult("No service has returned a valid result")
            return result

        for index, service in enumerate(self.services):
            try:
                return _text_to_speech(translator=service, index=index)
            except Exception:
                continue
        else:
            raise NoResult("No service has returned a valid result")

    def clean_cache(self) -> None:
        """
        Cleans caches

        Returns:
            None
        """
        for service in self.services:
            service.clean_cache()
