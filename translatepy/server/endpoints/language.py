"""translatepy's language endpoints"""
from nasse import Endpoint, Error, Response, Return

from translatepy import Language
from translatepy.server.server import TRANSLATEPY_ENDPOINT, app

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
    return language._cain_value


@app.route(endpoint=LANGUAGE_ENDPOINT)
def search(query: str, limit: int = 10) -> Response[Return("languages", description="The language search results", type=list)]:
    limit = max(min(limit, 100), 0)
    results = Language.search(query)

    return Response({
        "languages": [
            {
                "string": result.vector.string,
                "similarity": result.similarity,
                "language": result.vector.id
            }
            for result in results[:limit]
        ]
    })
