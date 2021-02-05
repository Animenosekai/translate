"""
Evaluating strings similarity
"""

from math import sqrt
from collections import Counter
from operator import itemgetter
from data.data import LANGUAGES_NAME_TO_CODE_INTERNATIONAL

class StringVector():
    def __init__(self, string) -> None:
        self.string = str(string)
        self.count = Counter(self.string)
        self.set = set(self.count)
        self.length = sqrt(sum(char_count ** 2 for char_count in self.count.values()))

    def __repr__(self) -> str:
        return "Vector: " + str(self.string)

INTERNATIONAL_VECTORS = {StringVector(language):LANGUAGES_NAME_TO_CODE_INTERNATIONAL[language] for language in LANGUAGES_NAME_TO_CODE_INTERNATIONAL}

def language_search(query):
    """
    Finds the most similar language
    """
    results_dict = {}
    InputVector = StringVector(query)
    for vector in INTERNATIONAL_VECTORS:
        summation = sum(vector.count[character] * InputVector.count[character] for character in vector.set.intersection(InputVector.set))
        length = vector.length * InputVector.length
        similarity = (0 if length == 0 else summation/length)
        results_dict[vector] = similarity
    bestResult = max(results_dict.items(), key=itemgetter(1))[0] # Returns the max value
    return bestResult.string, INTERNATIONAL_VECTORS[bestResult], results_dict[bestResult]
