from os import environ
import typing

from db import client
from exceptions import DatabaseDisabled, Forbidden, NotFound
from nasse import Response, Request
from nasse.models import Dynamic, Endpoint, Error, Login, Param, Return
from nasse.utils.boolean import to_bool
from translatepy.server.server import app

from datetime import datetime

from yuno.security.hash import Hasher
from yuno.security.token import TokenManager
from yuno.security.encrypt import AES

hasher = Hasher()
aes = AES(bytes.fromhex(environ["TRANSLATEPY_AES_KEY"]), prefix="translatepy")
token_manager = TokenManager(key=bytes.fromhex(environ["TRANSLATEPY_JWT_KEY"]), sign=bytes.fromhex(environ["TRANSLATEPY_JWT_SIGN"]))


base = Endpoint(
    section="Stars",
    errors=Error(name="DATABASE_DISABLED", description="When the server disabled any database interaction", code=501),
    login=Login(no_login=True)
)


if not to_bool(environ.get("TRANSLATEPY_DB_DISABLED", False)):
    stars = client.translatepy.stars
else:
    stars = {}

if typing.TYPE_CHECKING:
    stars = client.translatepy.stars


def generate_ip_hash(ip: str):
    return hasher.hash_string(
        "{ip}{salt}".format(
            ip=ip,
            salt=environ.get("TRANSLATEPY_IP_SALT", "")
        )
    )


@app.route("/stars", endpoint=Endpoint(
    endpoint=base,
    description="Get all starred translations"
))
def stars_handler(request: Request):
    if to_bool(environ.get("TRANSLATEPY_DB_DISABLED", False)):
        raise DatabaseDisabled

    query = stars.find({
        "users.{hash}".format(hash=generate_ip_hash(request.client_ip)): {
            "$exists": True
        }
    })
    results = []
    for document in query:
        result = document.copy()
        result["services"] = document["services"].copy()
        result["language"] = document["language"].copy()
        result["users"] = len(document["users"].keys())
        results.append(result)
    return Response(
        data={
            "stars": results
        },
        message="Here are your starred translations"
    )


def TranslationToken(value: str):
    return token_manager.decode(value, encryption=aes)


@app.route("/stars/<translation_id>", Endpoint(
    name="Translation Star",
    endpoint=base,
    methods=["GET", "POST", "DELETE"],
    description={
        "GET": "Get the stars for a translation",
        "POST": "Star a translation",
        "DELETE": "Unstar a translation"
    },
    params=[
        Param(name="token", description="The token to authenticate the translation", type=TranslationToken, methods="POST")
    ],
    dynamics=[
        Dynamic(name="translation_id", description="The ID of the translation to star", methods="POST"),
        Dynamic(name="translation_id", description="The ID of the translation to get", methods="GET"),
        Dynamic(name="translation_id", description="The ID of the translation to unstar", methods="DELETE"),
    ],
    errors=[
        Error(name="FORBIDDEN", description="You are not allowed to star this translation", code=403),
        Error(name="NOT_FOUND", description="The translation could not be found", code=404)
    ] + base.errors,
    returning=[
        Return(name="source", description="The source text", methods=["GET", "POST"]),
        Return(name="result", description="The result text", methods=["GET", "POST"]),
        Return(name="language", description="The translation languages", children=[
            Return(name="source", description="The source language", methods=["GET", "POST"]),
            Return(name="dest", description="The destination language", methods=["GET", "POST"])
        ], methods=["GET", "POST"]),
        Return(name="users", description="The number of users who starred the translation", type=int, methods=["GET", "POST"])
    ]
))
def stars__translation_id__(request: Request, method: str, translation_id: str, token: dict = None):
    if to_bool(environ.get("TRANSLATEPY_DB_DISABLED", False)):
        raise DatabaseDisabled

    current_ip_hash = generate_ip_hash(request.client_ip)

    if method == "DELETE":
        stars.update({
            "_id": translation_id  # query
        }, {
            "$unset": {  # command
                "users.{hash}".format(hash=current_ip_hash): ""
            }
        })
        return "Removed the star"

    try:
        translation = stars[translation_id]
    except KeyError as err:
        raise NotFound("We couldn't find the given translation")

    if method == "POST":
        # token body
        # {
        #     "sub": "user hash",
        #     "data": {
        #         "translationID": "translation ID",
        #         "source": "source text",
        #         "result": "result text",
        #         "language": {
        #             "source": "source language",
        #             "dest": "destination language"
        #         }
        #     }
        # }
        if current_ip_hash != token["sub"]:
            raise Forbidden("You are not allowed to star this translation")

        token_data = token["data"]
        if translation_id != token_data["translationID"]:
            raise Forbidden("You are not allowed to star this translation")

        if len(translation.users) <= 0:
            translation.update({
                "source": token_data["source"],
                "result": token_data["result"],
                "language": token_data["language"],
            })

        translation.users[current_ip_hash] = datetime.utcnow()

    result = translation.copy()
    result["services"] = translation.services.copy()
    result["language"] = translation.language.copy()
    result["users"] = len(translation["users"].keys())
    return Response(result)
