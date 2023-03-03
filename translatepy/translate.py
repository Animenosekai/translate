"""
translatepy v3.0

© Anime no Sekai — 2023
"""
import inspect
import typing
from multiprocessing.pool import ThreadPool
from threading import Thread

from bs4 import BeautifulSoup
from bs4.element import NavigableString, PageElement, PreformattedString, Tag

from translatepy import exceptions, models
from translatepy.language import Language
from translatepy.translators import (PONS, QCRI, BaseTranslator, Bing, DeepL,
                                     Google, Libre, Microsoft, MyMemory,
                                     Reverso, TranslateCom, Yandex)
from translatepy.translators.base import BaseTranslator, C
from translatepy.utils import importer, queue, request


class Translate(BaseTranslator):
    """
    A class which groups all of the translators
    """

    def __init__(self, session: typing.Optional[request.Session] = None, services_list: typing.Optional[typing.List[BaseTranslator]] = None, fast: bool = False):
        """
        A special `Translator` class which groups multiple translators to have better results.

        Parameters
        ----------
        services_list: list[Type | BaseTranslator]
            A list of instanciated `BaseTranslator` or subclasses of `BaseTranslator` to use as translators
        session: utils.request.Session
            The `Session` object used to make all of the requests
        fast: bool
            Enables fast mode (concurrent processing)
        """
        super().__init__(session)
        self.services_list = services_list or [Google, Yandex, Microsoft, Reverso, Bing,
                                               DeepL, Libre, TranslateCom, MyMemory, PONS, QCRI]

        try:
            _ = iter(self.services_list)
        except Exception as err:
            raise exceptions.ParameterTypeError("Parameter 'services_list' must be iterable, {} was given".format(type(services_list).__name__)) from err

        self.FAST_MODE = fast

        if isinstance(session, type):  # is not instantiated
            self.session = session()
        else:
            self.session = session

        self.services = []
        for service in self.services_list:
            if isinstance(service, str):
                service = importer.get_translator(service)
            if not isinstance(service, BaseTranslator):  # not instantiated
                if not issubclass(service, BaseTranslator):
                    raise exceptions.ParameterTypeError("{service} must be a child class of the BaseTranslator class".format(service=service))
                # avoiding to instantiate anything because it might not be used
            self.services.append(service)

    def _instantiate_translator(self, service: BaseTranslator, services_list: list, index: int):
        if not isinstance(service, BaseTranslator):  # not instantiated
            try:
                service = service(session=self.session)  # it should want `session` because that's how `BaseTranslator` is implemented
            except TypeError:
                service = service()
            services_list[index] = service
        return service

    def _apply(self, work: str, *args, **kwargs):
        """
        Tests `work` on all of the services

        Parameters
        ----------
        work: str
            The function name to call
        *args
        **kwargs
            The arguments to give to `work`
        """

        def worker(translator: BaseTranslator, index: int):
            translator = self._instantiate_translator(translator, self.services, index)
            try:
                result = getattr(translator, work)(*args, **kwargs)
            except Exception:
                raise exceptions.NoResult("{service} did not return any value".format(service=translator.__repr__()))
            if not result:
                pass
            return result

        def fast_work(queue: queue.Queue, translator: BaseTranslator, index: int):
            try:
                queue.put(worker(translator=translator, index=index))
            except Exception:
                pass

        if self.FAST_MODE:
            _queue = queue.Queue()
            threads = []
            for index, service in enumerate(self.services):
                thread = Thread(target=fast_work, args=(_queue, service, index))
                thread.start()
                threads.append(thread)
            result = _queue.get(threads=threads)  # wait for a value and return it
            if result is None:
                raise exceptions.NoResult("No service has returned a valid result")
            return result

        for index, service in enumerate(self.services):
            try:
                return worker(service, index=index)
            except Exception:
                continue

        raise exceptions.NoResult("No service has returned a valid result")

    def _translate(self: C, text: str, dest_lang: typing.Any, source_lang: typing.Any, *args, **kwargs) -> models.TranslationResult[C]:
        return self._apply("translate", text=text, dest_lang=dest_lang, source_lang=source_lang, *args, **kwargs)

    def _alternatives(self: C, translation: models.TranslationResult, *args, **kwargs) -> typing.Union[models.TranslationResult[C], typing.List[models.TranslationResult[C]]]:
        return self._apply("alternatives", translation=translation, *args, **kwargs)

    def _transliterate(self: C, text: str, dest_lang: typing.Any, source_lang: typing.Any, *args, **kwargs) -> models.TransliterationResult[C]:
        return self._apply("transliterate", text=text, dest_lang=dest_lang, source_lang=source_lang, *args, **kwargs)

    def _spellcheck(self: C, text: str, source_lang: typing.Any, *args, **kwargs) -> typing.Union[models.SpellcheckResult[C], models.RichSpellcheckResult[C]]:
        return self._apply("spellcheck", text=text, source_lang=source_lang, *args, **kwargs)

    def _language(self: C, text: str, *args, **kwargs) -> models.LanguageResult[C]:
        return self._apply("language", text=text, *args, **kwargs)

    def _example(self: C, text: str, source_lang: typing.Any, *args, **kwargs) -> typing.Union[models.ExampleResult[C], typing.List[models.ExampleResult[C]]]:
        return self._apply("example", text=text, source_lang=source_lang, *args, **kwargs)

    def _dictionary(self: C, text: str, source_lang: typing.Any, *args, **kwargs) -> typing.Union[typing.Union[models.DictionaryResult[C], models.RichDictionaryResult[C]], typing.List[typing.Union[models.DictionaryResult[C], models.RichDictionaryResult[C]]]]:
        return self._apply("dictionary", text=text, source_lang=source_lang, *args, **kwargs)

    def _text_to_speech(self: C, text: str, speed: int, gender: models.Gender, source_lang: typing.Any, *args, **kwargs) -> models.TextToSpechResult[C]:
        return self._apply("text_to_speech", text=text, speed=speed, gender=gender, source_lang=source_lang, *args, **kwargs)

    def _code_to_language(self, code: Language) -> Language:
        return code

    def _language_to_code(self, language: Language) -> Language:
        return language
