from nasse import Nasse
from nasse.config import General

General.SANITIZE_USER_SENT = False  # this is needed for /html

app = Nasse("translatepy")
