"""
translatepy

Translate, transliterate, get the language of texts in no time with the help of numerous APIs!

✨ Anime no Sekai, 2023
"""
__all__ = [
    # Information
    "__author__",
    "__copyright__",
    "__license__",
    "__version__",

    # Exports
    "Language",
    "Translate",
    "BaseTranslator",

    # Server
    "server",

    # Logger
    "logger",
    "log",
    "debug",
    "warn",

    # Translate
    "t",  # shared instance
    "translate",
    "alternatives",
    "transliterate",
    "spellcheck",
    "language",
    "example",
    "dictionary",
    "text_to_speech",
    "Translator",  # alias for `translatepy.Translate`

    # Languages
    "AUTOMATIC",
    "ENGLISH"
]

# Imports
from .__info__ import __author__, __copyright__, __license__, __version__
from translatepy.language import Language
from translatepy.translate import Translate
from translatepy.translators.base import BaseTranslator
from translatepy.server.server import app as server

# Logger
logger = server.logger
log = server.logger.log
debug = server.logger.debug
warn = server.logger.warn

t = Translate()
"""A shared instance of `translatepy.Translate`"""

# Functions
translate = t.translate
alternatives = t.alternatives
transliterate = t.transliterate
spellcheck = t.spellcheck
language = t.language
example = t.example
dictionary = t.dictionary
text_to_speech = t.text_to_speech

# For backward compatibility
Translator = Translate

# Languages

AUTOMATIC = Language("auto")
ENGLISH = Language("eng")
