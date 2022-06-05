from nasse import Response
from nasse.models import Dynamic, Endpoint, Error, Login, Param, Return
from nasse.utils.boolean import to_bool
from translatepy.exceptions import UnknownLanguage
from translatepy.language import (LANGUAGE_CLEANUP_REGEX, LOADED_VECTORS,
                                  VECTORS, Language)
from translatepy.server.server import app
from translatepy.utils.sanitize import remove_spaces
from translatepy.utils.similarity import StringVector

base = Endpoint(
    section="Language",
    errors=[
        Error("TRANSLATEPY_EXCEPTION", "Generic exception raised when an error occured on translatepy. This is the base class for the other exceptions raised by translatepy."),
        Error("UNKNOWN_LANGUAGE", "When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.", code=400)
    ],
    login=Login(no_login=True)
)

EXAMPLE_ENGLISH = {
    "id": "eng",
    "alpha2": "en",
    "alpha3b": "eng",
    "alpha3t": "eng",
    "alpha3": "eng",
    "name": "English",
    "foreign": {
        "af": "Engels",
        "sq": "Anglisht",
        "am": "እንግሊዝኛ",
        "ar": "الإنجليزية",
        "hy": "Անգլերեն",
        "...": "...",
        "zh": "英语",
        "he": "אנגלית",
        "jv": "Inggris",
        "en": "English"
    },
    "extra": {
        "type": "Living",
        "scope": None
    }
}

EXAMPLE_JAPANESE = {
    "id": "jpn",
    "alpha2": "ja",
    "alpha3b": "jpn",
    "alpha3t": "jpn",
    "alpha3": "jpn",
    "name": "Japanese",
    "extra": {
        "type": "Living",
        "scope": None
    },
    "in_foreign_languages": {
        "af": "Japanese",
        "sq": "Japonez",
        "am": "ጃፓንኛ",
        "ar": "اليابانية",
        "hy": "Ճապոնական",
        "...": "...",
        "zh": "日本",
        "he": "יַפָּנִית",
        "jv": "Jepang",
        "en": "Japanese"
    }
}


def Bool(value):
    """A boolean value with True by default"""
    return to_bool(value, default=True)


PARAM_FOREIGN = PARAM_FOREIGN

language_details_endpoint = Endpoint(
    endpoint=base,
    name="Language Details",
    description="Retrieving details about the given language",
    params=[
        Param("threshold", "The similarity threshold to use when searching for similar languages", required=False, type=float),
        PARAM_FOREIGN
    ],
    returning=[
        Return("id", example="eng", description="The language id"),
        Return("alpha2", nullable=True, example="en", description="The language alpha2 code"),
        Return("alpha3b", nullable=True, example="eng", description="The language alpha3b code"),
        Return("alpha3t", nullable=True, example="eng", description="The language alpha3t code"),
        Return("alpha3", example="eng", description="The language alpha3 code"),
        Return("name", example="English", description="The language name"),
        Return("foreign", nullable=True, description="The language in foreign languages", type="dict", example={'af': 'Engels', 'sq': 'Anglisht', 'am': 'እንግሊዝኛ', 'ar': 'الإنجليزية', 'hy': 'Անգլերեն', "...": "...", 'zh': '英语', 'he': 'אנגלית', 'jv': 'Inggris', 'en': 'English'}),
        Return(
            "extra",
            example={
                "type": "Living",
                "scope": None,
            },
            description="The language extra data",
            children=[
                Return("type", nullable=True, example="Living", description="The language type"),
                Return("scope", nullable=True, example="Individual", description="The language scope")
            ]
        )
    ]
)


@app.route("/language/details", Endpoint(
    endpoint=language_details_endpoint,
    params=[Param("lang", "The language to lookup")] + language_details_endpoint.params
))
def language_details(lang: str, threshold: float = 93, foreign: bool = True):
    try:
        result = Language(lang, threshold)
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
        "id": result.id,
        "similarity": result.similarity,
        "alpha2": result.alpha2,
        "alpha3b": result.alpha3b,
        "alpha3t": result.alpha3t,
        "alpha3": result.alpha3,
        "name": result.name,
        "foreign": (result.in_foreign_languages if foreign else None),
        "extra": {
            "type": result.extra.type.name if result.extra.type is not None else None,
            "scope": result.extra.scope.name if result.extra.scope is not None else None
        }
    }


@app.route("/language/search", Endpoint(
    endpoint=base,
    name="Language Search",
    description="Searching for a language",
    returning=Return(
        name="languages",
        example=[
            {
                "string": "English",
                "similarity": 100,
                "language": EXAMPLE_ENGLISH
            }
        ],
        description="The languages found"
    ),
    params=[
        Param("lang", "The language to lookup"),
        Param("limit", "The limit of languages to return. (max: 100, default: 10)", required=False, type=int),
        PARAM_FOREIGN
    ]
))
def language_search(lang: str, foreign: bool = True, limit: int = 10):
    limit = max(min(limit, 100), 0)

    normalized_language = StringVector(remove_spaces(LANGUAGE_CLEANUP_REGEX.sub("", lang.lower())))

    results_dict = {}
    for vector in LOADED_VECTORS:
        summation = sum(vector.counter[character] * normalized_language.counter[character] for character in vector.set.intersection(normalized_language.set))
        length = vector.length * normalized_language.length
        similarity = (0 if length == 0 else summation / length)
        results_dict[vector] = similarity

    results = sorted(results_dict.items(), key=lambda x: x[1], reverse=True)[:limit]

    return 200, {
        "languages": [
            {
                "string": str(vector.string),
                "similarity": similarity,
                "language": Language(VECTORS[vector.string]["i"]).as_dict(foreign)
            }
            for vector, similarity in results
        ]
    }


@app.route("/language/details/<language>", Endpoint(
    endpoint=language_details_endpoint,
    name="Language Details (dynamic)",
    dynamics=Dynamic("language", "The language to lookup")
))
def language_details_dynamic(language: str, threshold: float = 93, foreign: bool = True):
    try:
        result = Language(language, threshold)
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
        "id": result.id,
        "similarity": result.similarity,
        "alpha2": result.alpha2,
        "alpha3b": result.alpha3b,
        "alpha3t": result.alpha3t,
        "alpha3": result.alpha3,
        "name": result.name,
        "foreign": (result.in_foreign_languages if foreign else None),
        "extra": {
            "type": result.extra.type.name if result.extra.type is not None else None,
            "scope": result.extra.scope.name if result.extra.scope is not None else None
        }
    }
