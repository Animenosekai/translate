"""Serves the website"""

import pathlib

from flask import send_from_directory

from translatepy.server.server import app

WEBSITE_DIR = (pathlib.Path(__file__).parent.parent / "website").resolve().absolute()


@app.route("/", name="Index", category="Website")
def index():
    return send_from_directory(WEBSITE_DIR, "index.html")


@app.route("/<path:path>", category="Website")
def website(path: str):
    """Serves the website pages and assets"""
    try:
        return send_from_directory(WEBSITE_DIR, path)
    except Exception:
        return send_from_directory(WEBSITE_DIR, path + ".html")
