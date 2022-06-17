from bson import ObjectId
from datetime import datetime
from yuno import YunoDict, YunoCollection


class Datetime(datetime):
    def __new__(self, *args, **kwargs) -> datetime:
        print(args, kwargs)
        if len(args) > 0 and isinstance(args[0], datetime):
            return args[0]
        return datetime(*args, **kwargs)


class ServiceTimings(YunoDict):
    _id: ObjectId
    timings: dict[str, int]
    timestamp: Datetime


class TimingsCollection(YunoCollection):
    __type__ = ServiceTimings

    def __getitem__(self, name: str) -> ServiceTimings:
        return super().__getitem__(name)
