from yuno import YunoClient, YunoDatabase

from schemas.errors import ErrorsCollection
from schemas.timings import TimingsCollection


class TranslatepyDatabase(YunoDatabase):
    errors: ErrorsCollection
    timings: TimingsCollection


class TranslatepyClient(YunoClient):
    """Translate client"""
    translatepy: TranslatepyDatabase
