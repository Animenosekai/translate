from datetime import datetime
from yuno import YunoDict, YunoCollection


class StarredTranslation(YunoDict):
    """User starred translations"""
    _id: str  # translation ID
    timestamp: datetime
    services: list[str]
    users: list[str]


class StarsCollection(YunoCollection):
    __type__ = StarredTranslation

    def __getitem__(self, name: str) -> StarredTranslation:
        return super().__getitem__(name)
