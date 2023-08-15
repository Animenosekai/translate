"""translatepy's language endpoints"""
from nasse import Endpoint, Error

from translatepy import Language
from translatepy.server.server import TRANSLATEPY_ENDPOINT, app

from translatepy.language import LANGUAGE_CLEANUP_REGEX, LOADED_VECTORS, Language, VECTORS
from translatepy.utils.sanitize import remove_spaces
from translatepy.utils.similarity import StringVector

LANGUAGE_ENDPOINT = Endpoint(
    category="Language",
    endpoint=TRANSLATEPY_ENDPOINT,
    errors=[
        Error("TRANSLATEPY_EXCEPTION", "Generic exception raised when an error occured on translatepy"),
        Error("UNKNOWN_LANGUAGE", "When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.", code=400),
    ]
)


@app.route(endpoint=LANGUAGE_ENDPOINT)
def __language__(language: Language):
    return language.as_dict()


@app.route
def search(query: str, limit: int = 10):
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

