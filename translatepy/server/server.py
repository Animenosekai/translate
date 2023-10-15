"""the translatepy server"""
import pathlib

from nasse import Endpoint, Login, Nasse, NasseConfig

app = Nasse("translatepy", NasseConfig(name="translatepy", sanitize_user_input=False))
"""The `nasse` server instance for `translatepy`"""

TRANSLATEPY_ENDPOINT = Endpoint(base_dir=pathlib.Path(__file__).parent / "endpoints",
                                login=Login(skip=True))
"""Base `translatepy` endpoint"""

SERVER_DOCS_PATH = pathlib.Path(__file__).parent / "docs"
"""The root path for the server offline docs"""
