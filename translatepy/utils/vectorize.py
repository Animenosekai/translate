"""Handles vectors"""
import collections
import dataclasses
import math
import re
import typing

import cain

from translatepy.utils import sanitize

CLEANUP_REGEX = re.compile(r"\(.+\)")


def string_preprocessing(string: str) -> str:
    """internal function to preprocess the given string for fuzzy search"""
    return sanitize.remove_spaces(CLEANUP_REGEX.sub("", str(string).lower()))


class Vector(cain.Object):
    """A string vector"""
    id: str
    string: str
    value: float

    @property
    def counter(self):
        """Returns a counter for the vector"""
        return collections.Counter(self.string)

    @property
    def set(self):
        """Returns a set for the vector"""
        return set(self.string)

A = list[Vector]

def vectorize(id: str, string: str):
    """Vectorizes the given string"""
    string = string_preprocessing(string)
    return Vector({
        "id": str(id),
        "string": string,
        "value": math.sqrt(sum(char_count ** 2 for char_count in collections.Counter(string).values()))
    })


@dataclasses.dataclass
class SearchResult:
    """A result from the `search` function"""
    vector: Vector
    """The actual vector"""
    similarity: float
    """The similarity with the search query"""


def search(query: str, data: typing.List[Vector]) -> typing.List[SearchResult]:
    """Searches `query` through `data`"""
    query_vector = vectorize(id="", string=query)
    results: typing.List[SearchResult] = []
    for vector in data:
        summation = sum(vector.counter[character] * query_vector.counter[character]
                        for character in vector.set.intersection(query_vector.set))
        try:
            similarity = (summation / (vector.value * query_vector.value)) * 100
        except ZeroDivisionError:
            similarity = 0
        results.append(SearchResult(vector=vector, similarity=similarity))

    return sorted(results, key=lambda element: element.similarity, reverse=True)
