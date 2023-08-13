from schemas.types import Datetime
from yuno import YunoDict, YunoCollection


class Error(YunoDict):
    """
    This is the error class.
    """
    service: str
    error: str
    timestamp: Datetime


class ErrorsCollection(YunoCollection):
    __type__ = Error

    def __getitem__(self, name: str) -> Error:
        return super().__getitem__(name)
