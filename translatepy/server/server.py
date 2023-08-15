"""the translatepy server"""
from nasse import Nasse, NasseConfig, Endpoint, Login
import pathlib

app = Nasse("translatepy", NasseConfig(sanitize_user_input=False))
TRANSLATEPY_ENDPOINT = Endpoint(base_dir=pathlib.Path(__file__).parent / "endpoints", login=Login(skip=True))
