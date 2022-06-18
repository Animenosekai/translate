from yuno import YunoClient, YunoDatabase

from schemas.stars import StarsCollection
from schemas.errors import ErrorsCollection
from schemas.timings import TimingsCollection


class TranslatepyDatabase(YunoDatabase):
    errors: ErrorsCollection
    timings: TimingsCollection
    stars: StarsCollection


class TranslatepyClient(YunoClient):
    """Translate client"""
    translatepy: TranslatepyDatabase
