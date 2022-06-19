from os import environ
import typing

from nasse.logging import LogLevels, log
from nasse.utils.boolean import to_bool
from yuno import MongoDB

from schemas.client import TranslatepyClient

if not to_bool(environ.get("TRANSLATEPY_DB_DISABLED", False)):
    MONGO_URI = environ.get("TRANSLATEPY_MONGO_URI", None)
    if MONGO_URI is None:
        mongo = MongoDB()
        log("Starting MongoDB", LogLevels.INFO)
        mongo.start()
        MONGO_URI = mongo

    client = TranslatepyClient(MONGO_URI, connect=False)
else:
    client = {}

if typing.TYPE_CHECKING:
    client = TranslatepyClient("")