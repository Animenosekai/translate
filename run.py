from nasse.utils.args import Args

from translatepy.server import language  # registering the endpoints
from translatepy.server import translation  # registering the endpoints
from translatepy.server.server import app

app.make_docs("./translatepy/server/docs")
if not Args.exists("--dry"):
    app.run()
