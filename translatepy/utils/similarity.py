"""
Evaluating strings similarity
"""

from collections import Counter
from math import sqrt
from operator import itemgetter
import typing

class StringVector:
    def __init__(self, string: str, data: dict = None) -> None:
        self.string = str(string)
        if data is not None:
            self.set = data["s"]
            self.length = data["l"]
            self.counter = data["c"]
            # self.counter = Counter(self.string)
        else:
            self.counter = Counter(self.string)
            self.set = set(self.counter)
            self.length = sqrt(sum(char_count ** 2 for char_count in self.counter.values()))

    def __repr__(self) -> str:
        return "Vector: " + self.string


def fuzzy_search(search_source: typing.List, query: str) -> typing.Tuple[str, float]:
    """
    Finds the most similar string
    """
    results_dict = {}
    input_query = StringVector(query)
    for vector in search_source:
        summation = sum(vector.counter[character] * input_query.counter[character] for character in vector.set.intersection(input_query.set))
        length = vector.length * input_query.length
        similarity = (0 if length == 0 else summation / length)
        results_dict[vector] = similarity
    best_result = max(results_dict.items(), key=itemgetter(1))[0]  # Returns the max value
    return best_result.string, results_dict[best_result]
