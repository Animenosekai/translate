from schemas.types import Datetime
from yuno import YunoDict, YunoCollection


class StarredTranslationLanguage(YunoDict):
    """Starred translation language"""
    source: str
    dest: str


class StarredTranslation(YunoDict):
    """User starred translations"""
    _id: str  # translation ID
    language: StarredTranslationLanguage = {}
    source: str = ""  # source text
    result: str = ""  # translated text
    services: list[str] = []
    users: dict[str, Datetime] = {}


class StarsCollection(YunoCollection):
    __type__ = StarredTranslation

    def __getitem__(self, name: str) -> StarredTranslation:
        return super().__getitem__(name)
