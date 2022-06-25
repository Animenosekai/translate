from nasse.utils.args import Args

from translatepy.server import language  # registering the endpoints
from translatepy.server import translation  # registering the endpoints
from translatepy.server.server import app

app.make_docs("./docs/CLI Usage/Server Documentation")
if not Args.exists("--dry"):
    app.run()
