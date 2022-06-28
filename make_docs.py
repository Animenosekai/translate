from nasse.docs.localization import EnglishLocalization, FrenchLocalization, JapaneseLocalization

from translatepy.server import language  # registering the endpoints
from translatepy.server import translation  # registering the endpoints
from translatepy.server.server import app


app.make_docs("./translatepy/server/docs")
app.make_docs("./docs/English/CLI Usage/Server Documentation", localization=EnglishLocalization)
app.make_docs("./docs/Français/Utilisation par CLI/Documentation du Serveur", localization=FrenchLocalization)
app.make_docs("./docs/日本語/CLIでの利用/サーバーのドキュメント", localization=JapaneseLocalization)

import os
os.environ["TRANSLATEPY_DB_DISABLED"] = "True"

import sys
sys.path.append("./server")

from server.endpoints import stars, stats
from server.endpoints.translation import stream_fix

for path, endpoint in app.endpoints.items():
    if path == "/stream":
        endpoint.handler = stream_fix
        break

app.make_docs("./server/docs", curl=False, javascript=False, python=False)
app.make_docs("./docs/English/API Documentation", localization=EnglishLocalization)
app.make_docs("./docs/Français/Documentation d'API", localization=FrenchLocalization)
app.make_docs("./docs/日本語/APIドキュメント", localization=JapaneseLocalization)
