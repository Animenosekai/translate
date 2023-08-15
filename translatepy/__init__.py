"""
translatepy

Translate, transliterate, get the language of texts in no time with the help of multiple APIs!

© Anime no Sekai — 2023
"""

from .__info__ import __author__, __copyright__, __license__, __version__
from translatepy.language import Language
from translatepy.translate import Translate

# For backward compatibility
Translator = Translate

# Languages

AUTOMATIC = Language("auto")
ENGLISH = Language("eng")
