from os import environ
from yuno import MongoDB
from server.schemas.client import TranslatepyClient

MONGO_URI = environ.get("MONGO_URI", None)
if MONGO_URI is None:
    mongo = MongoDB()
    mongo.start()
    MONGO_URI = mongo

client = TranslatepyClient(MONGO_URI)
