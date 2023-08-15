"""
importer.py

A module to allow for dynamic importing of translators.
"""

import copy
import pathlib
import pydoc
import typing

import cain

from translatepy import exceptions, translators
from translatepy.translators.base import BaseTranslator
from translatepy.utils import lru, vectorize

IMPORTER_CACHE = lru.LRUDictCache(512)

IMPORTER_DATA_DIR = pathlib.Path(__file__).parent.parent / "data" / "translators"
with open(IMPORTER_DATA_DIR / "vectors.cain", "b+r") as f:
    IMPORTER_VECTORS = cain.load(f, typing.List[vectorize.Vector])


# registry of all exported translators
NAMED_TRANSLATORS = {}
for element in dir(translators):
    obj = getattr(translators, element)
    try:
        if issubclass(obj, BaseTranslator):
            NAMED_TRANSLATORS[vectorize.string_preprocessing(element)] = obj
    except TypeError:
        continue


def translator_from_name(name: str) -> typing.Type[BaseTranslator]:
    """Retrieves the given translate from its name"""
    try:
        return NAMED_TRANSLATORS[vectorize.string_preprocessing(name)]
    except KeyError as err:
        raise ValueError(f"Couldn't get the translator {name}") from err


def get_translator(query: str,
                   threshold: float = 90,
                   forceload: bool = False) -> typing.Type[BaseTranslator]:
    """Searches the given translator"""
    query = vectorize.string_preprocessing(str(query or ""))
    if not query:
        raise exceptions.UnknownTranslator(BaseTranslator, 0, "Couldn't find a nameless translator")

    # Check the incoming language, whether it is in the cache, then return the values from the cache
    cache_result = IMPORTER_CACHE.get(query)
    if cache_result:
        return cache_result

    try:
        result = pydoc.locate(query, forceload=forceload)
        try:
            if not issubclass(result, BaseTranslator):
                raise ImportError
        except TypeError:
            if not isinstance(result, BaseTranslator):
                raise ImportError
            result = result.__class__
        return result
    except ImportError:  # this also catches ErrorDuringImport
        pass

    try:
        return translator_from_name(query)
    except ValueError:
        pass

    results = sorted(vectorize.search(query, IMPORTER_VECTORS), key=lambda element: element.similarity, reverse=True)

    if not results:
        raising_message = f"Couldn't recognize the given translator `{query}`"
        raise exceptions.UnknownTranslator(BaseTranslator, 0, raising_message)

    result = translator_from_name(results[0].vector.id)
    similarity = results[0].similarity
    IMPORTER_CACHE[query] = copy.copy(result)
    if similarity < threshold:
        raising_message = f"Couldn't recognize the given translator ({query})\nDid you mean: {results[0].vector.string} (Similarity: {round(similarity, 2)}%)?"
        raise exceptions.UnknownTranslator(result, similarity, raising_message)

    return result
