from os import environ
from translatepy.server import language, translation, server
from server.endpoints.translation import stream_fix

for path, endpoint in server.app.endpoints.items():
    if path == "/stream":
        endpoint.handler = stream_fix
        break

server.app.run(host=environ.get("HOST", "127.0.0.1"), port=environ.get("PORT", 5000))
