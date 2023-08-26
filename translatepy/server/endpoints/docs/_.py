"""Sends the docs"""
import pathlib

from translatepy import Language
from translatepy.server.server import TRANSLATEPY_ENDPOINT, app

DOCS_PATH = pathlib.Path(__file__).parent.parent.parent / "docs"


@app.route("/docs/<path:path>", endpoint=TRANSLATEPY_ENDPOINT, category="Documentation")
def __path__(path: str, language: Language):
    return {"markdown": (DOCS_PATH / language.id / path).read_text()}
