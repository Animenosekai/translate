"""Sends the docs"""
import pathlib

from translatepy import Language
from translatepy.server.server import TRANSLATEPY_ENDPOINT, SERVER_DOCS_PATH, app


@app.route("/docs/<path:path>", endpoint=TRANSLATEPY_ENDPOINT, category="Documentation")
def __path__(path: str, language: Language):
    return {"markdown": (SERVER_DOCS_PATH / language.id / path).read_text()}
