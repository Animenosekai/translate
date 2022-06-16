from yuno import YunoClient, YunoDatabase

from server.schemas.errors import ErrorsCollection
from server.schemas.timings import TimingsCollection


class TranslatepyDatabase(YunoDatabase):
    errors: ErrorsCollection
    timings: TimingsCollection


class TranslatepyClient(YunoClient):
    """Translate client"""
    translatepy: TranslatepyDatabase
