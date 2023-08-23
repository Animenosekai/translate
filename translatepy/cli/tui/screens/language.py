"""The language selection screen"""

import typing

from nasse.localization import EnglishLocalization, Localization
from textual import events
from textual.containers import Container
from textual.screen import ModalScreen
from translatepy import Language
from textual.widgets import Button, Label, Static, OptionList
from textual.containers import VerticalScroll
from translatepy.cli.tui.components.inputs import Input, DefaultInput


class LanguageSelection(ModalScreen):
    """Screen with a dialog to select a language."""

    DEFAULT_CSS = """
    LanguageSelection {
        align: center middle;
    }

    #dialog {
        padding: 0 1;
        width: 80vw;
        max-width: 100;
        height: 80vh;
        border: thick $background 80%;
        background: $surface;
    }

    Button {
        width: 100%;
    }
    """

    def __init__(self, localization: typing.Type[Localization] = EnglishLocalization, on_selection: typing.Optional[typing.Callable[[Language], typing.Any]] = None, **kwargs) -> None:
        super().__init__(**kwargs)
        self.localization = localization
        self.on_selection = on_selection

    def compose(self):
        yield Container(
            Input(id="language-input", on_key=self.load_results),
            OptionList(id="language-results"),
            id="dialog",
        )

    def load_results(self, event: events.Key, input: DefaultInput):
        """Loads the language results and displays them"""
        if not event.is_printable:
            return
        results = Language.search(input.value)
        scroll = self.query_one("#language-results", OptionList)
        scroll.clear_options()
        scroll.add_options((
            f"{result.vector.string} [gray]({result.vector.id})[/gray]"
            for result in results[:10]
        ))
        event.stop()

    def on_key(self, event: events.Key) -> None:
        """When a key is pressed on the keyboard"""
        if event.key == "escape":
            self.app.pop_screen()
        elif event.key == "enter":
            lang = self.current_language
            self.app.pop_screen()
            if lang and self.on_selection:
                self.on_selection(lang)

    def on_option_list_option_selected(self, msg: OptionList.OptionSelected):
        self.app.pop_screen()
        if self.on_selection:
            self.on_selection(self.current_language)

    @property
    def current_language(self) -> Language:
        """The selected language"""
        inp = self.query_one("#language-input", Input).value
        return Language(inp, threhsold=-1)
