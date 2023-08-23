from textual.app import App, ComposeResult
from textual_textarea import TextArea


class TextApp(App):
    def compose(self) -> ComposeResult:
        yield TextArea()

    def on_mount(self) -> None:
        ta = self.query_one(TextArea)
        ta.focus()


app = TextApp()
app.run()
