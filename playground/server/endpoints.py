from pathlib import Path
from nasse.models import Endpoint, Param, Return, Error

from translatepy import Translator
from translatepy.server.server import app
from translatepy.translators.base import BaseTranslator
from translatepy.utils.importer import get_translator

t = Translator()
base = Endpoint(
    base_dir=Path(__file__).parent,
    errors=[
        Error("TRANSLATEPY_EXCEPTION", "Generic exception raised when an error occured on translatepy. This is the base class for the other exceptions raised by translatepy."),
        Error("NO_RESULT", "When no result is returned from the translator(s)"),
        Error("PARAMETER_ERROR", "When a parameter is missing or invalid"),
        Error("PARAMETER_TYPE_ERROR", "When a parameter is of the wrong type"),
        Error("PARAMETER_VALUE_ERROR", "When a parameter is of the wrong value"),
        Error("TRANSLATION_ERROR", "When a translation error occurs"),
        Error("UNKNOWN_LANGUAGE", "When one of the provided language could not be understood by translatpy. Extra information like the string similarity and the most similar string are provided in `data`."),
        Error("UNKNOWN_TRANSLATOR", "When one of the provided translator/service could not be understood by translatpy. Extra information like the string similarity and the most similar string are provided in `data`.")
    ]
)


def TranslatorList(value: str):
    return get_translator(value.split(","))


@app.route(endpoint=Endpoint(
    endpoint=base,
    params=[
        Param("text", "The text to translate"),
        Param("dest", "The destination language"),
        Param("source", "The source language", required=False),
        Param("services", "The translator(s) to use. When providing multiple translators, the names should be comma-separated.", required=False, type=TranslatorList),
    ],
    returning=[
        Return("service", "Google", "The translator used"),
        Return("source", "Hello world", "The source text"),
        Return("sourceLang", "English", "The source language"),
        Return("destLang", "Japanese", "The destination language"),
        Return("result", "こんにちは世界", "The translated text")
    ]
))
def translate(text: str, dest: str, source: str = "auto", services: list[BaseTranslator] = None):
    if services is not None:
        t = Translator(services)
    result = t.translate(text=text, destination_language=dest, source_language=source)
    return 200, {
        "service": str(result.service),
        "source": result.source,
        "sourceLang": result.source_language,
        "destLang": result.destination_language,
        "result": result.result
    }
