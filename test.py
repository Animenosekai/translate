from translatepy.server.server import app
from translatepy.server.endpoints import _
from rich.console import Console

console = Console()

console.print(app.endpoints)
app.make_docs("translatepy/server/docs")
app.run(debug=True)