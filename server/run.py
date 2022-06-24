from os import environ
from nasse.logging import log, LogLevels
from nasse.utils.boolean import to_bool
from endpoints import stars, stats
from translatepy.server import language, translation, server
from endpoints.translation import stream_fix

for path, endpoint in server.app.endpoints.items():
    if path == "/stream":
        endpoint.handler = stream_fix
        break

if __name__ == "__main__":
    if to_bool(environ.get("TRANSLATEPY_GENERATE_DOCS", False)):
        server.app.make_docs("./server/docs", curl=False, javascript=False, python=False)
    log("🍡 Press Ctrl+C to quit", LogLevels.INFO)
    server.app.run(host=environ.get("HOST", "127.0.0.1"), port=environ.get("PORT", 5001))
