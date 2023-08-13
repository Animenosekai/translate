from bson import ObjectId
from schemas.types import Datetime
from yuno import YunoDict, YunoCollection


class ServiceTimings(YunoDict):
    _id: ObjectId
    timings: dict[str, int]
    timestamp: Datetime


class TimingsCollection(YunoCollection):
    __type__ = ServiceTimings

    def __getitem__(self, name: str) -> ServiceTimings:
        return super().__getitem__(name)
