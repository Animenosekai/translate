"""Redefines base classes from textual"""
import typing

from textual.app import App as TextualApp
from textual.app import Widget as TextualWidget
from textual.binding import Binding, _Bindings

Bindings = typing.Optional[typing.List[typing.Union[Binding, typing.Tuple[str, str, str]]]]


class App(TextualApp):
    """Controlling Textual apps general behaviors"""

    def set_bindings(self, bindings: Bindings = None) -> None:
        """Sets the current bindings"""
        bindings = bindings or []
        self._bindings = _Bindings(bindings)


class Widget(TextualWidget):
    """Controlling Textual widgets general behaviors"""
    _id = None
    _name = ""
