"""
translatepy

Translate, transliterate, get the language of texts in no time with the help of multiple APIs!

© Anime no Sekai — 2023
"""

from translatepy.language import Language
from translatepy.translate import Translate

# For backward compatibility
Translator = Translate

__version_tuple__ = (3, 0, '(alpha)')


def __version_string__():
    if isinstance(__version_tuple__[-1], str):
        return '.'.join(map(str, __version_tuple__[:-1])) + __version_tuple__[-1]
    return '.'.join(str(i) for i in __version_tuple__)


__author__ = 'Anime no Sekai'
__copyright__ = 'Copyright 2023, translatepy'
__credits__ = ['animenosekai']
__license__ = 'GNU General Public License v3 (GPLv3)'
__version__ = 'translatepy v{}'.format(__version_string__())
__maintainer__ = 'Anime no Sekai'
__email__ = 'niichannomail@gmail.com'
__status__ = 'Stable'
