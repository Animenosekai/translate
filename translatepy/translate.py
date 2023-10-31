"""
translatepy v3.0

© Anime no Sekai — 2023
"""

import typing

from translatepy.translators import (PONS, QCRI, BaseTranslator, Bing, DeepL,
                                     Google, Libre, Microsoft, MyMemory,
                                     Papago, Reverso, TranslateCom, Yandex)
from translatepy.translators.base_aggregator import BaseTranslatorAggregator
from translatepy.utils import request

DEFAULT_TRANSLATORS = [Google, Yandex, Microsoft, Reverso, Bing,
                       DeepL, Libre, TranslateCom, MyMemory, PONS, QCRI, Papago]
"""A list of default translators to use with the translators aggregation"""


class Translate(BaseTranslatorAggregator):
    """
    A class which groups all of the translators
    """

    def __init__(self, services_list: typing.Optional[typing.List[typing.Union[BaseTranslator, typing.Type[BaseTranslator]]]] = None, session: typing.Optional[request.Session] = None, fast: bool = False):
        services_list = services_list or DEFAULT_TRANSLATORS
        super().__init__(services_list, session, fast)
