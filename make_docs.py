from nasse.docs.localization import EnglishLocalization, FrenchLocalization, JapaneseLocalization

from translatepy.server import language  # registering the endpoints
from translatepy.server import translation  # registering the endpoints
from translatepy.server.server import app


app.make_docs("./translatepy/server/docs")
app.make_docs("./docs/English/API Documentation", localization=EnglishLocalization)
app.make_docs("./docs/Français/Documentation d'API", localization=FrenchLocalization)
app.make_docs("./docs/日本語/APIドキュメント", localization=JapaneseLocalization)
