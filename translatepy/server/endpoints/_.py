"""translatepy's work endpoints"""
import inspect
import typing

import miko
from nasse import Endpoint, Error, Parameter, Return
from nasse.utils.boolean import to_bool

from translatepy import AUTOMATIC, Language, Translate, models
from translatepy.server.server import TRANSLATEPY_ENDPOINT, app
from translatepy.translators import base
from translatepy.utils import importer

_DEFAULT_TRANSLATE = Translate()

class TranslatorList:
    """A list of translators"""

    def __init__(self, value: str = "") -> None:
        self.raw = str(value).strip().split(",")
        self.translators = [importer.get_translator(val) for val in self.raw if val]

    @property
    def instance(self):
        """Returns an instance with the given translators"""
        if self.translators:
            return Translate(services_list=self.translators)
        return _DEFAULT_TRANSLATE

DEFAULT_TRANSLATORS = TranslatorList()


WORK_ENDPOINT = Endpoint(
    category="Work",
    endpoint=TRANSLATEPY_ENDPOINT,
    errors=[
        Error("TRANSLATEPY_EXCEPTION", "Generic exception raised when an error occured on translatepy"),
        Error("NO_RESULT", "When no result is returned from the translator(s)"),
        Error("UNKNOWN_LANGUAGE", "When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.", code=400),
        Error("UNKNOWN_TRANSLATOR", "When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.", code=400)
    ]
)


def auto_doc(func: base.T):
    """Automatically documents the given endpoint from the BaseTranslator function"""
    def wrapper(handler: typing.Callable):
        # Getting the handler signature
        signature = inspect.signature(handler)

        # Parsing the doc-string
        docs = miko.Docs(handler.__doc__ or "", signature)

        # Getting the overloads
        overloads = typing.get_overloads(inspect.unwrap(func))

        # Preparing the data
        data = {
            "methods": "GET",
            "endpoint": WORK_ENDPOINT,
            "description": docs.description,
            "parameters": [
                Parameter("translators", description="A comma-separated list of translators to use",
                          required=False, type=TranslatorList)
            ],
            "returns": []
        }

        for overload in overloads:
            overload = inspect.unwrap(overload)
            overload_docs = miko.Docs(overload.__doc__ or "")
            iterable = False

            for element in overload_docs.returns.elements.values():
                element_name = str(element.name)
                if element_name.startswith("LazyIterable"):
                    # We are inside the iterable version of the function
                    iterable = True
                    break
                else:
                    if element_name.startswith("list"):
                        element_name = element_name.strip("list").strip("[").strip("]")
                    model: models.Result = getattr(models, element_name)
                    data["returns"] = [Return(name=attr.name, description=attr.description, type=attr.annotation)
                                       for attr in model.attributes]
                    break

            if iterable:
                continue

            for element in docs.parameters.elements.values():
                if element.name in overload_docs.parameters.elements:
                    overload_element = overload_docs.parameters[element.name]
                    data["parameters"].append(Parameter(name=element.name,
                                                        description=overload_element.body,
                                                        required=not element.optional,
                                                        type=next(iter(element.types)) if element.types else None))

        app.route(**data)(handler)
        return handler

    return wrapper


@auto_doc(Translate.translate)
def translate(text: str, dest_lang: Language,
              source_lang: Language = AUTOMATIC, translators: TranslatorList = DEFAULT_TRANSLATORS):
    """Translates the text in the given language"""
    result = translators.instance.translate(text=text, dest_lang=dest_lang, source_lang=source_lang)
    return result.exported

# @auto_doc(Translate.alternatives)
# def alternatives(translators: TranslatorList, text: str, dest_lang: Language, source_lang: Language = AUTOMATIC):
#     pass


@auto_doc(Translate.transliterate)
def transliterate(text: str, dest_lang: Language,
                  source_lang: Language = AUTOMATIC, translators: TranslatorList = DEFAULT_TRANSLATORS):
    """Transliterates the text in the given language"""
    result = translators.instance.transliterate(text=text, dest_lang=dest_lang, source_lang=source_lang)
    return result.exported


@auto_doc(Translate.spellcheck)
def spellcheck(text: str, source_lang: Language = AUTOMATIC,
               translators: TranslatorList = DEFAULT_TRANSLATORS):
    """Spellchecks the given text"""
    result = translators.instance.spellcheck(text=text, source_lang=source_lang)
    return result.exported


@auto_doc(Translate.language)
def language(text: str, source_lang: Language = AUTOMATIC,
             translators: TranslatorList = DEFAULT_TRANSLATORS):
    """Retrieves the language of the given text"""
    result = translators.instance.language(text=text, source_lang=source_lang)
    return result.exported


@auto_doc(Translate.example)
def example(text: str, source_lang: Language = AUTOMATIC,
            translators: TranslatorList = DEFAULT_TRANSLATORS):
    """Finds examples for the given text"""
    results = translators.instance.example(text=text, source_lang=source_lang)
    return {"examples": [element.exported for element in results]}


@auto_doc(Translate.dictionary)
def dictionary(text: str, source_lang: Language = AUTOMATIC,
               translators: TranslatorList = DEFAULT_TRANSLATORS):
    """Retrieves meanings for the given text"""
    results = translators.instance.dictionary(text=text, source_lang=source_lang)
    return {"meanings": [element.exported for element in results]}


@auto_doc(Translate.text_to_speech)
def tts(text: str, source_lang: Language = AUTOMATIC, raw: to_bool = False,
        translators: TranslatorList = DEFAULT_TRANSLATORS):
    """Returns the speech version of the given text"""
    result = translators.instance.text_to_speech(text=text, source_lang=source_lang)
    return result.exported
