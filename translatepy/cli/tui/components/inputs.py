import typing
from rich.highlighter import Highlighter
from textual import events, keys
from textual.suggester import Suggester
from textual.validation import Validator
from textual.widgets import Input as DefaultInput


class Input(DefaultInput):
    """A (custom) text input widget."""

    def __init__(self, value: typing.Optional[str] = None,
                 placeholder: str = "",
                 highlighter: typing.Optional[Highlighter] = None,
                 password: bool = False, *,
                 suggester: typing.Optional[Suggester] = None,
                 validators: typing.Optional[typing.Union[Validator, typing.Iterable[Validator]]] = None,
                 name: typing.Optional[str] = None,
                 id: typing.Optional[str] = None,
                 classes: typing.Optional[str] = None,
                 disabled: bool = False,
                 on_key: typing.Optional[typing.Callable[[events.Key, "Input"], typing.Any]] = None,
                 on_blur: typing.Optional[typing.Callable[[events.Blur, "Input"], typing.Any]] = None) -> None:
        super().__init__(value, placeholder, highlighter, password, suggester=suggester, validators=validators, name=name, id=id, classes=classes, disabled=disabled)
        self.additional_on_key = on_key
        self.additional_on_blur = on_blur

    def on_key(self, event: events.Key) -> None:
        """Checks for `enter` or `esc` to blur the input"""
        if event.key in (keys.Keys.Enter, keys.Keys.Escape):
            try:
                self.screen.set_focus(None)
            except Exception:
                self.blur()
        else:
            if self.additional_on_key:
                return self.additional_on_key(event, self)

    def on_blur(self, event: events.Blur) -> None:
        """Checks for blurs"""
        if self.additional_on_blur:
            self.additional_on_blur(event, self)