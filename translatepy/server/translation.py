from nasse import Response
from nasse.models import Endpoint, Error, Param, Return
from translatepy import Translator
from translatepy.exceptions import UnknownLanguage, UnknownTranslator
from translatepy.server.server import app


base = Endpoint(
    section="Translation",
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
    return value.split(",")
    # return get_translator(value.split(","))

t = Translator()

@app.route("/translate", Endpoint(
    endpoint=base,
    name="Translate",
    params=[
        Param("text", "The text to translate"),
        Param("dest", "The destination language"),
        Param("source", "The source language", required=False),
        Param("translators", "The translator(s) to use. When providing multiple translators, the names should be comma-separated.", required=False, type=TranslatorList),
    ],
    returning=[
        Return("service", "Google", "The translator used"),
        Return("source", "Hello world", "The source text"),
        Return("sourceLang", "English", "The source language"),
        Return("destLang", "Japanese", "The destination language"),
        Return("result", "こんにちは世界", "The translated text")
    ]
))
def translate(text: str, dest: str, source: str = "auto", translators: list[str] = None):
    current_translator = t
    if translators is not None:
        try:
            current_translator = Translator(translators)
        except UnknownTranslator as err:
            return Response(
                data={
                    "guessed": str(err.guessed_translator),
                    "similarity": err.similarity,
                },
                message="translatepy could not find the given translator",
                error="UNKNOWN_TRANSLATOR",
                code=400
            )

    try:
        result = current_translator.translate(text=text, destination_language=dest, source_language=source)
    except UnknownLanguage as err:
        return Response(
            data={
                "guessed": str(err.guessed_language),
                "similarity": err.similarity,
            },
            message="translatepy could not understand the given language ({})".format(dest),
            error="UNKNOWN_LANGUAGE",
            code=400
        )
    return 200, {
        "service": str(result.service),
        "source": result.source,
        "sourceLang": result.source_language,
        "destLang": result.destination_language,
        "result": result.result
    }
