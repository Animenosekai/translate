"""Defines the options view"""
import dataclasses
import json
import pathlib
import typing

from textual import events
from textual.containers import Container, Horizontal
from textual.screen import ModalScreen
from textual.widgets import Button

from nasse.tui.components.headers import StickyHeader

T = typing.TypeVar("T")


class OptionsScreen(ModalScreen[T]):
    """The options managing screen"""

    DEFAULT_CSS = """
    OptionsScreen {
        align: center middle;
        background: rgba(30, 30, 30, 0.75);
        height: auto;
        width: 80vw;
    }

    Input {
        margin-bottom: 1;
    }

    .options-switch-title {
        content-align: center middle;
        height: 3;
        content-align: center middle;
        width: 20;
    }

    .options-switch-container {
        align-vertical: middle;
        margin-bottom: 1;
        height: auto;
        width: auto;
    }

    #options-container {
        /* height: auto; */
        min-height: 50vh;
        max-height: 75vh;
        width: 80vw;
        height: auto;
        padding: 1 5;
        content-align: center middle;
        align: center middle;
        border: round gray;
    }

    #options-confirmation-container {
        width: auto;
        height: auto;
        dock: bottom;
        align-horizontal: right;
    }
    """

    def __init__(self,
                 options: T,
                 name: typing.Optional[str] = None,
                 id: typing.Optional[str] = None,
                 classes: typing.Optional[str] = None) -> None:
        super().__init__(name, id, classes)
        self.options: T = options

    def compose(self):
        yield StickyHeader("Options")
        with Container(id="options-container"):
            yield from self.compose_options()
        with Horizontal(id="options-confirmation-container"):
            yield Button("Ok", id="options-confirmation-button")

    def compose_options(self):
        """The inner options view renderer"""
        raise NotImplementedError("The options view couldn't be rendered because it is not implemented yet.")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """When a button is pressed"""
        if event.button.id == "options-confirmation-button":
            options = dataclasses.asdict(self.options)
            options.update(self.collect_values())
            return self.dismiss(self.options.__class__(**options))

    def collect_values(self) -> typing.Dict[str, typing.Any]:
        """Collect the different options value"""
        return {}

    def on_key(self, event: events.Key) -> None:
        """When a key is pressed on the keyboard"""
        if event.key == "escape":
            return self.dismiss(self.options)

    @staticmethod
    def loads(key: str, cast: typing.Type[T]) -> T:
        """Loads the configs"""
        config_path = pathlib.Path() / ".translatepy" / "config" / str(key)
        try:
            return cast(**json.loads(config_path.read_text()))
        except Exception:
            return cast()

    @staticmethod
    def dumps(key: str, options: T) -> None:
        """Exports the configs"""
        config_path = pathlib.Path() / ".translatepy" / "config" / str(key)
        config_path.parent.mkdir(parents=True, exist_ok=True)
        config_path.write_text(json.dumps(dataclasses.asdict(options), ensure_ascii=False, separators=(",", ":")))
