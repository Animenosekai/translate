"""
Evaluating strings similarity
"""

from math import sqrt
from collections import Counter
from operator import itemgetter
from translatepy.utils.annotations import Tuple, List


class StringVector():
    def __init__(self, string: str, data: dict = None) -> None:
        self.string = str(string)
        self.count = Counter(self.string)
        if data is not None:
            self.set = set(data["set"])
            self.length = data["length"]
        else:
            self.set = set(self.count)
            self.length = sqrt(sum(char_count ** 2 for char_count in self.count.values()))

    def __repr__(self) -> str:
        return "Vector: " + self.string


def fuzzy_search(search_source: List, query: str) -> Tuple[str, float]:
    """
    Finds the most similar string
    """
    results_dict = {}
    InputQueryVector = StringVector(query)
    for vector in search_source:
        summation = sum(vector.count[character] * InputQueryVector.count[character] for character in vector.set.intersection(InputQueryVector.set))
        length = vector.length * InputQueryVector.length
        similarity = (0 if length == 0 else summation / length)
        results_dict[vector] = similarity
    bestResult = max(results_dict.items(), key=itemgetter(1))[0]  # Returns the max value
    return bestResult.string, results_dict[bestResult]
