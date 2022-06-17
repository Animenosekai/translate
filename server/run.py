from os import environ
from nasse.logging import log, LogLevels
from translatepy.server import language, translation, server
from endpoints.translation import stream_fix

for path, endpoint in server.app.endpoints.items():
    if path == "/stream":
        endpoint.handler = stream_fix
        break

if __name__ == "__main__":
    log("🍡 Press Ctrl+C to quit", LogLevels.INFO)
    server.app.run(host=environ.get("HOST", "127.0.0.1"), port=environ.get("PORT", 5001))
