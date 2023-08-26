"""the translatepy server"""
import pathlib

from nasse import Endpoint, Login, Nasse, NasseConfig

app = Nasse("translatepy", NasseConfig(sanitize_user_input=False, cors="http://localhost:3000"))
"""The `nasse` server instance for `translatepy`"""

TRANSLATEPY_ENDPOINT = Endpoint(base_dir=pathlib.Path(__file__).parent / "endpoints",
                                login=Login(skip=True))
"""Base `translatepy` endpoint"""
