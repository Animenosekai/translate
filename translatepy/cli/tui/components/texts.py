"""Text components"""

from textual.widgets import Label
from nasse.tui.widget import Widget


class SectionTitle(Widget):
    """A section title"""

    DEFAULT_CSS = """
    SectionTitle {
        height: auto;
        margin-top: 2;
        margin-bottom: 1;
        margin-left: 1;
    }
    """

    def __init__(self, title: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.title = str(title)

    def compose(self):
        yield Label(f"[underline][bold]{self.title}[/bold][/underline]")
