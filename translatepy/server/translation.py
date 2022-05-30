from nasse import Response
from nasse.models import Endpoint, Error, Param, Return, Login
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
        Error("UNKNOWN_LANGUAGE", "When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.", code=400),
        Error("UNKNOWN_TRANSLATOR", "When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.", code=400)
    ],
    login=Login(no_login=True)
)


def TranslatorList(value: str):
    return value.split(",")
    # return get_translator(value.split(","))

t = Translator()

@app.route("/translate", Endpoint(
    endpoint=base,
    name="Translate",
    description=t.translate.__doc__,
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
            message=str(err),
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

@app.route("/transliterate", Endpoint(
    endpoint=base,
    name="Transliterate",
    description=t.transliterate.__doc__,
    params=[
        Param("text", "The text to transliterate"),
        Param("dest", "The destination language", required=False),
        Param("source", "The source language", required=False),
        Param("translators", "The translator(s) to use. When providing multiple translators, the names should be comma-separated.", required=False, type=TranslatorList),
    ],
    returning=[
        Return("service", "Google", "The translator used"),
        Return("source", "おはよう", "The source text"),
        Return("sourceLang", "Japanese", "The source language"),
        Return("destLang", "English", "The destination language"),
        Return("result", "Ohayou", "The transliteration")
    ]
))
def transliterate(text: str, dest: str = "en", source: str = "auto", translators: list[str] = None):
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
        result = current_translator.transliterate(text=text, destination_language=dest, source_language=source)
    except UnknownLanguage as err:
        return Response(
            data={
                "guessed": str(err.guessed_language),
                "similarity": err.similarity,
            },
            message=str(err),
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


@app.route("/spellcheck", Endpoint(
    endpoint=base,
    name="Spellcheck",
    description=t.spellcheck.__doc__,
    params=[
        Param("text", "The text to spellcheck"),
        Param("source", "The source language", required=False),
        Param("translators", "The translator(s) to use. When providing multiple translators, the names should be comma-separated.", required=False, type=TranslatorList),
    ],
    returning=[
        Return("service", "Google", "The translator used"),
        Return("source", "God morning", "The source text"),
        Return("sourceLang", "English", "The source language"),
        Return("result", "Good morning", "The spellchecked text")
    ]
))
def spellcheck(text: str, source: str = "auto", translators: list[str] = None):
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
        result = current_translator.spellcheck(text=text, source_language=source)
    except UnknownLanguage as err:
        return Response(
            data={
                "guessed": str(err.guessed_language),
                "similarity": err.similarity,
            },
            message=str(err),
            error="UNKNOWN_LANGUAGE",
            code=400
        )
    return 200, {
        "service": str(result.service),
        "source": result.source,
        "sourceLang": result.source_language,
        "result": result.result
    }

@app.route("/language", Endpoint(
    endpoint=base,
    name="Language",
    description=t.language.__doc__,
    params=[
        Param("text", "The text to get the language of"),
        Param("translators", "The translator(s) to use. When providing multiple translators, the names should be comma-separated.", required=False, type=TranslatorList),
    ],
    returning=[
        Return("service", "Google", "The translator used"),
        Return("source", "Hello world", "The source text"),
        Return("result", "jpa", "The resulting language alpha-3 code")
    ]
))
def language(text: str, translators: list[str] = None):
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

    result = current_translator.language(text=text)
    
    return 200, {
        "service": str(result.service),
        "source": result.source,
        "result": result.result
    }

@app.route("/tts", Endpoint(
    endpoint=base,
    name="Text to Speech",
    description=t.text_to_speech.__doc__,
    params=[
        Param("text", "The text to convert to speech"),
        Param("source", "The source language", required=False),
        Param("speed", "The speed of the speech", required=False, type=int),
        Param("gender", "The gender of the speech", required=False),
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
def language(text: str, translators: list[str] = None):
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

    result = current_translator.language(text=text)
    
    return 200, {
        "service": str(result.service),
        "source": result.source,
        "result": result.result
    }
