"""
importer.py

A module to allow for dynamic importing of translators.
"""

import builtins
import sys
from translatepy.exceptions import UnknownTranslator
from translatepy.language import LANGUAGE_CLEANUP_REGEX

from translatepy.translators import (BingTranslate, DeeplTranslate,
                                     GoogleTranslate, GoogleTranslateV1,
                                     GoogleTranslateV2, LibreTranslate,
                                     MicrosoftTranslate, MyMemoryTranslate,
                                     ReversoTranslate, TranslateComTranslate,
                                     YandexTranslate)
from translatepy.translators.base import BaseTranslator
from translatepy.utils.sanitize import remove_spaces
from translatepy.utils.similarity import fuzzy_search, StringVector
from translatepy.utils._importer_data import VECTORS


def translator_from_name(name: str) -> BaseTranslator:
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
    return None


for alias, data in VECTORS.items():
    translator = translator_from_name(data['t'])
    if translator is None:  # RUNTIME NON-CRITICAL ERROR: translator not found
        continue
    data["t"] = translator


LOADED_VECTORS = [StringVector(alias, data=data) for alias, data in VECTORS.items()]


class ErrorDuringImport(ImportError):
    """
    Errors that occurred while trying to import something to document it.

    Notes
    -----
    - This is a subclass of ImportError
    - The code comes from pydoc
        https://github.com/python/cpython/blob/3680ebed7f3e529d01996dd0318601f9f0d02b4b/Lib/pydoc.py#L393
    """

    def __init__(self, filename, exc_info):
        self.filename = filename
        self.exc, self.value, self.tb = exc_info

    def __str__(self):
        exc = self.exc.__name__
        return 'problem in %s - %s: %s' % (self.filename, exc, self.value)


def safeimport(path: str, forceload: bool = False, cache: dict = {}):
    """
    Import a module; handle errors; return None if the module isn't found.
    If the module *is* found but an exception occurs, it's wrapped in an
    ErrorDuringImport exception and reraised.  Unlike __import__, if a
    package path is specified, the module at the end of the path is returned,
    not the package at the beginning.  If the optional 'forceload' argument
    is 1, we reload the module from disk (unless it's a dynamic extension).

    Notes
    -----
    - The code comes from pydoc
        https://github.com/python/cpython/blob/3680ebed7f3e529d01996dd0318601f9f0d02b4b/Lib/pydoc.py#L421
    """
    try:
        # If forceload is 1 and the module has been previously loaded from
        # disk, we always have to reload the module.  Checking the file's
        # mtime isn't good enough (e.g. the module could contain a class
        # that inherits from another module that has changed).
        if forceload and path in sys.modules:
            if path not in sys.builtin_module_names:
                # Remove the module from sys.modules and re-import to try
                # and avoid problems with partially loaded modules.
                # Also remove any submodules because they won't appear
                # in the newly loaded module's namespace if they're already
                # in sys.modules.
                subs = [m for m in sys.modules if m.startswith(path + '.')]
                for key in [path] + subs:
                    # Prevent garbage collection.
                    cache[key] = sys.modules[key]
                    del sys.modules[key]
        module = __import__(path)
    except:
        # Did the error occur before or after the module was found?
        (exc, value, tb) = info = sys.exc_info()
        if path in sys.modules:
            # An error occurred while executing the imported module.
            raise ErrorDuringImport(sys.modules[path].__file__, info)
        elif exc is SyntaxError:
            # A SyntaxError occurred before we could execute the module.
            raise ErrorDuringImport(value.filename, info)
        elif issubclass(exc, ImportError) and value.name == path:
            # No such module in the path.
            return None
        else:
            # Some other error occurred during the importing process.
            raise ErrorDuringImport(path, sys.exc_info())
    for part in path.split('.')[1:]:
        try:
            module = getattr(module, part)
        except AttributeError:
            return None
    return module


def locate(path: str, forceload: bool = False):
    """
    Locate an object by name or dotted path, importing as necessary.

    Notes
    -----
    - The code comes from pydoc
        https://github.com/python/cpython/blob/3680ebed7f3e529d01996dd0318601f9f0d02b4b/Lib/pydoc.py#L1718
    """
    parts = [part for part in path.split('.') if part]
    module, n = None, 0
    while n < len(parts):
        nextmodule = safeimport('.'.join(parts[:n + 1]), forceload)
        if nextmodule:
            module, n = nextmodule, n + 1
        else:
            break
    if module:
        object = module
    else:
        object = builtins
    for part in parts[n:]:
        try:
            object = getattr(object, part)
        except AttributeError:
            return None
    return object


def get_translator(translator: str, threshold: float = 90, forceload: bool = False) -> BaseTranslator:
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
        result = locate(translator, forceload)
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
