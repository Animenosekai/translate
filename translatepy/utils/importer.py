"""
importer.py

A module to allow for dynamic importing of translators.
"""

import typing
import pydoc
from translatepy.exceptions import UnknownTranslator
# TODO
# from translatepy.language import LANGUAGE_CLEANUP_REGEX

from translatepy.translators import (BingTranslate, DeeplTranslate,
                                     GoogleTranslate, GoogleTranslateV1,
                                     GoogleTranslateV2, LibreTranslate,
                                     MicrosoftTranslate, MyMemoryTranslate,
                                     ReversoTranslate, TranslateComTranslate,
                                     YandexTranslate)
from translatepy.translators.base import BaseTranslator
from translatepy.utils.sanitize import remove_spaces
from translatepy.utils.similarity import fuzzy_search, StringVector
# from translatepy.utils._importer_data import VECTORS


def translator_from_name(name: str) -> typing.Type[BaseTranslator]:
    """Retrieves the given translate from its name"""
    if name == "GoogleTranslate":
        return GoogleTranslate
    elif name == "GoogleTranslateV1":
        return GoogleTranslateV1
    elif name == "GoogleTranslateV2":
        return GoogleTranslateV2
    elif name == "MicrosoftTranslate":
        return MicrosoftTranslate
    elif name == "YandexTranslate":
        return YandexTranslate
    elif name == "LibreTranslate":
        return LibreTranslate
    elif name == "BingTranslate":
        return BingTranslate
    elif name == "DeeplTranslate":
        return DeeplTranslate
    elif name == "MyMemoryTranslate":
        return MyMemoryTranslate
    elif name == "ReversoTranslate":
        return ReversoTranslate
    elif name == "TranslateComTranslate":
        return TranslateComTranslate
    raise ValueError(f"Couldn't get the translator {name}")


"""
for alias, data in VECTORS.items():
    Translator = translator_from_name(data['t'])
    if Translator is None:  # RUNTIME NON-CRITICAL ERROR: translator not found
        continue
    data["t"] = Translator

LOADED_VECTORS = [StringVector(alias, data=data) for alias, data in VECTORS.items()]
"""


def get_translator(translator: str,
                   threshold: float = 90,
                   forceload: bool = False) -> BaseTranslator:
    """
    Gets a translator object from the translator name or import path.

    Parameters
    ----------
    translator : str
        The translator name or import path.
    forceload : bool
        Whether to reload the module from disk (used by pydoc).

    Returns
    -------
    translator : translatepy.translators.BaseTranslator
        The translator object.

    Raises
    ------
    UnknownTranslator
        If the translator is not found.
    """
    translator = str(translator)
    try:
        result = pydoc.locate(translator, forceload=forceload)
        if not isinstance(result, BaseTranslator):
            raise ImportError
        return result
    except ImportError:  # this also catches ErrorDuringImport
        pass
    normalized = remove_spaces(LANGUAGE_CLEANUP_REGEX.sub("", translator.lower()))
    alias, similarity = fuzzy_search(LOADED_VECTORS, normalized)
    similarity *= 100
    result = VECTORS[alias]["t"]
    if similarity < threshold:
        raising_message = "Couldn't recognize the given translator ({0})\nDid you mean: {1} (Similarity: {2}%)?".format(translator, alias, round(similarity, 2))
        raise UnknownTranslator(result, similarity, raising_message)
    return result
