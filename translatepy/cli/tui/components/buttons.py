"""Buttons"""
import typing
import functools

from textual.widgets import Static, Button
from textual.binding import Binding
from textual.message import Message
from textual import events

from translatepy import AUTOMATIC, Language
from translatepy.cli.tui.screens import LanguageSelection


class LanguageButton(Static, can_focus=True):
    """The language selection button"""
    DEFAULT_CSS = """
    LanguageButton {
        background: black 0%;
        margin-top: 0;
        text-style: bold;
        width: auto;
    }

    LanguageButton:focus {
        text-style: 
    }
    """

    BINDINGS = [Binding("enter", "press", "Press Button", show=False)]

    def __init__(self, language: typing.Union[str, Language] = AUTOMATIC,
                 extra_language: typing.Optional[typing.Union[str, Language]] = None,
                 on_language_change: typing.Optional[typing.Callable[[Language], typing.Any]] = None,
                 *args, **kwargs):
        self.language = Language(language)
        self.extra_language = Language(extra_language) if extra_language else None
        self.on_language_change = on_language_change
        super().__init__(*args, **kwargs)

    def on_mount(self, event):
        """When the button is mounted"""
        self.update(self.render_label())

    async def _on_click(self, event: events.Click) -> None:
        event.stop()
        self.press()

    class Pressed(Message, bubble=True):
        """Event sent when a `Button` is pressed.

        Can be handled using `on_button_pressed` in a subclass of
        [`Button`][textual.widgets.Button] or in a parent widget in the DOM.
        """

        def __init__(self, button: "LanguageButton") -> None:
            self.button: LanguageButton = button
            """The button that was pressed."""
            super().__init__()

    def press(self):
        """Respond to a button press.

        Returns:
            The button instance."""
        if self.disabled or not self.display:
            return self
        # ...and let other components know that we've just been clicked:
        self.post_message(LanguageButton.Pressed(self))
        return self

    def action_press(self) -> None:
        """Activate a press of the button."""
        self.press()

    def on_language_button_pressed(self, event: Button.Pressed):
        """When the button is pressed"""
        try:
            self.app.push_screen(LanguageSelection(on_selection=functools.partial(self.set_language, trigger=True)))
        except Exception:
            pass

    def render_label(self):
        """Renders the button label"""
        if self.extra_language:
            return f"{self.language.native} [gray]({self.extra_language.native})[/gray] ✍️"
        return f"{self.language.native} ✍️"

    def set_language(self, language: Language, trigger: bool = False):
        """Updates the language"""
        self.language = language
        self.extra_language = None
        self.update(self.render_label())
        if trigger and self.on_language_change:
            self.on_language_change(language)

    def set_extra_language(self, language: typing.Optional[typing.Union[str, Language]] = None):
        """Sets the extra language and updates the button"""
        self.extra_language = Language(language) if language else None
        self.update(self.render_label())
