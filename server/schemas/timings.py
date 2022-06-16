from bson import ObjectId
from datetime import datetime
from yuno import YunoDict, YunoCollection


class ServiceTimings(YunoDict):
    _id: ObjectId
    timings: dict[str, int]
    timestamp: datetime


class TimingsCollection(YunoCollection):
    __type__ = ServiceTimings

    def __getitem__(self, name: str) -> ServiceTimings:
        return super().__getitem__(name)
