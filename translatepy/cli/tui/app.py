"""
The Terminal UI for translatepy

        ╭────────────────────────────────────────────────────────────────╮
        │  Translate   Transliterate   Spellcheck    Language    Example │
        ├─╺━━━━━━━━━╸────────────────────────────────────────────────────┤
        │                                                                │
        │ Input                                                          │
        │ ╭────────────────────────────────────────────────────────────╮ │
        │ │ Bonjour, comment allez-vous                                │ │
        │ ╰────────────────────────────────────────────────────────────╯ │
        │                                                                │
        │ Result                                                         │
        │ ╭────────────────────────────────────────────────────────────╮ │
        │ │ Hello, how are you                                         │ │
        │ ╰────────────────────────────────────────────────────────────╯ │
        │                                                                │
        │                                                                │
        ╰────────────────────────────────────────────────────────────────╯                                                                                                                                                     
"""
import dataclasses
import typing

from textual import work, events
from textual.binding import Binding
from textual.containers import Container, Horizontal, VerticalScroll
from textual.widgets import (Footer, Header, Label, Select, Static,
                             TabbedContent, TabPane, _header)
from textual.worker import get_current_worker

from translatepy import AUTOMATIC, Translate, __info__, models
from translatepy.cli.tui.components.buttons import LanguageButton
from translatepy.cli.tui.components.inputs import Input
from translatepy.cli.tui.components.texts import SectionTitle
from translatepy.cli.tui.localization import (EnglishLocalization,
                                              FrenchLocalization,
                                              JapaneseLocalization,
                                              Localization)
from translatepy.cli.tui.redefine import App
from translatepy.cli.tui.screens import OptionsScreen, QuitScreen

ACTIONS = (
    "translate",
    "transliterate",
    "spellcheck",
    "language",
    "example",
    "dictionary",
    # "text_to_speech"
)
"""The different actions"""

# pylint: disable=pointless-string-statement
"""
╭─────────────────────────────── Dataclasses ────────────────────────────────╮
│ TranslatepyOptions                                                         │
╰────────────────────────────────────────────────────────────────────────────╯
"""


def language_to_localization(lang: str = "eng"):
    """Returns the correct localization from the given language string"""
    if lang == JapaneseLocalization.__id__:
        return JapaneseLocalization
    elif lang == FrenchLocalization.__id__:
        return FrenchLocalization
    return EnglishLocalization


@dataclasses.dataclass
class TranslatepyOptions:
    """App options"""
    language: str = "eng"


# pylint: disable=pointless-string-statement
"""
╭─────────────────────────────── Widgets/Views/Screens ────────────────────────────────╮
│ TranslatepyOptionsScreen                                                             │
╰──────────────────────────────────────────────────────────────────────────────────────╯
"""


class TranslatepyOptionsScreen(OptionsScreen[TranslatepyOptions]):
    """The TranslatepyTUI app options screen"""

    def __init__(self,
                 localization: typing.Type[Localization] = EnglishLocalization,
                 **kwargs) -> None:
        self.localization = localization
        super().__init__(**kwargs)

    def compose_options(self):
        """Composes the inner options view"""
        with VerticalScroll(id="options-inner-container"):
            yield SectionTitle(self.localization.language)
            yield Select([(local.__native__, local.__id__) for local in (EnglishLocalization, FrenchLocalization, JapaneseLocalization)],
                         prompt=self.localization.language,
                         allow_blank=False,
                         value=self.localization.__id__,
                         id="options-language")
            yield Label(self.localization.language_notice, id="options-language-notice")

            # yield UserSentForm(self.localization.proxies, id="options-proxies", initial_values=[(UserSent(name=key), value) for key, value in self.options.proxies.items()], localization=self.localization)

    def collect_values(self) -> typing.Dict[str, typing.Any]:
        """Collect the different options value"""
        return {
            "language": self.query_one("#options-language", Select).value
        }


# pylint: disable=pointless-string-statement
"""
╭─────────────────────────────── App ────────────────────────────────╮
│ TranslatepyTUI                                                     │
╰────────────────────────────────────────────────────────────────────╯
"""


def define_bindings(localization: typing.Type[Localization] = EnglishLocalization):
    """Defines the different bindings for the app"""
    return [("o", "open_options", localization.options),
            ("d", "toggle_dark", localization.theme),
            ("q", "request_quit", localization.quit),
            Binding("ctrl+c", "request_quit", localization.quit, show=False)]


class TranslatepyTUI(App):
    """Lets you use translatepy comfortably"""

    # Default values
    CSS_PATH = "app.css"
    BINDINGS = define_bindings()

    def __init__(self,
                 options: typing.Optional[TranslatepyOptions] = None,  # Options for the app
                 **kwargs):
        self.__class__.__name__ = "translatepy"
        super().__init__(**kwargs)

        self.options = options or TranslatepyOptionsScreen.loads("tui", TranslatepyOptions)
        self.localization = language_to_localization(self.options.language)

        self.set_bindings(define_bindings(self.localization))
        self.translator = Translate()

    # pylint: disable=pointless-string-statement
    """
    ╭─────────────────────────────── Composers ────────────────────────────────╮
    │ compose                                                                  │
    ╰──────────────────────────────────────────────────────────────────────────╯
    """

    def compose(self):
        """
        Draws the screen

        Area
        ----
        ╭────────────────────────────────────────────────╮
        │▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
        │▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
        │▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
        │▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
        │▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
        │▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
        │▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
        │▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
        │▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒│
        ╰────────────────────────────────────────────────╯
        """
        # The header icon will be changed inside the `on_mount` event of this class
        yield Header(show_clock=True)

        # Coverage: Screen
        with Horizontal(id="screen"):
            # with Container(id="history"):
            #     # History
            #     # Coverage: Left sidebar
            #     yield StickyHeader(self.localization.history)
            #     with VerticalScroll(id="history-requests"):
            #         # Requests History
            #         # This displays a list of already made
            #         # requests, whether it be successful or
            #         # erroneous ones, in chronological orders.
            #         for response in self.history:
            #             yield HistoryResponse(response)
            with Container(id="main"):
                # Main Page
                # Coverage: Center of the screen
                with TabbedContent(id="tabbed-content"):
                    for element in ACTIONS:
                        name = getattr(self.localization, f"action_{element}")
                        with TabPane(name, id=element, classes="pane"):
                            yield from getattr(self, f"{element}_view")()
        # Add a footer, which automatically displays the different available bindings
        yield Footer()

    def additional_on_blur(self, event: events.Blur, input: Input):
        """When something is blurred"""
        if not input.id:
            return
        action, _, _ = input.id.partition("-")
        getattr(self, f"request_{action}")()

    def translate_view(self):
        """Draws the `translate` method view"""
        yield SectionTitle(self.localization.input)
        yield Container(LanguageButton(id="translate-input-language", on_language_change=self.request_translate),
                        # Input("", classes="input", id="translate-input-text", on_key=self.request_translate),
                        Input("", classes="input", id="translate-input-text", on_blur=self.additional_on_blur),
                        classes="text-container")
        yield SectionTitle(self.localization.result)
        yield Container(LanguageButton("English", id="translate-result-language", on_language_change=self.request_translate),
                        Static("", classes="result result-static", id="translate-result-text"),
                        Static("", classes="service", id="translate-result-service"), classes="text-container")

    def update_translate_view(self, result: models.TranslationResult):
        """Updates the `translate` method view"""
        try:
            tabbed_content = self.app.query_one("#tabbed-content", TabbedContent)
        except Exception:
            return
        if not tabbed_content.active == "translate":
            return
        input_lang_btn = self.query_one("#translate-input-language", LanguageButton)
        if input_lang_btn.language == AUTOMATIC:
            input_lang_btn.set_extra_language(result.source_lang)
        else:
            input_lang_btn.set_language(result.source_lang)

        self.query_one("#translate-input-text", Input).value = result.source
        self.query_one("#translate-result-language", LanguageButton).language = result.dest_lang
        self.query_one("#translate-result-text", Static).update(result.translation)
        self.query_one("#translate-result-service", Static).update(self.localization.service.format(service=str(result.service)))

    def request_translate(self, *args, **kwargs):
        """Request a work from `translator`"""
        try:
            tabbed_content = self.app.query_one("#tabbed-content", TabbedContent)
        except Exception:
            return
        if not tabbed_content.active == "translate":
            return
        self.translation_worker("translate",
                                text=self.query_one("#translate-input-text", Input).value,
                                dest_lang=self.query_one("#translate-result-language", LanguageButton).language,
                                source_lang=self.query_one("#translate-input-language", LanguageButton).language)

    def transliterate_view(self):
        """Draws the `transliterate` method view"""
        yield SectionTitle(self.localization.input)
        yield Container(LanguageButton(id="transliterate-input-language", on_language_change=self.request_transliterate),
                        Input("", classes="input", id="transliterate-input-text", on_blur=self.additional_on_blur),
                        classes="text-container")
        yield SectionTitle(self.localization.result)
        yield Container(LanguageButton("English", id="transliterate-result-language", on_language_change=self.request_transliterate),
                        Static("", classes="result result-static", id="transliterate-result-text"),
                        Static("", classes="service", id="transliterate-result-service"), classes="text-container")

    def update_transliterate_view(self, result: models.TransliterationResult):
        """Updates the `transliterate` method view"""
        try:
            tabbed_content = self.app.query_one("#tabbed-content", TabbedContent)
        except Exception:
            return
        if not tabbed_content.active == "transliterate":
            return
        input_lang_btn = self.query_one("#transliterate-input-language", LanguageButton)
        if input_lang_btn.language == AUTOMATIC:
            input_lang_btn.set_extra_language(result.source_lang)
        else:
            input_lang_btn.set_language(result.source_lang)

        self.query_one("#transliterate-input-text", Input).value = result.source
        self.query_one("#transliterate-result-language", LanguageButton).language = result.dest_lang
        self.query_one("#transliterate-result-text", Static).update(result.transliteration)
        self.query_one("#transliterate-result-service", Static).update(self.localization.service.format(service=str(result.service)))

    def request_transliterate(self, *args, **kwargs):
        """Request a work from `translator`"""
        try:
            tabbed_content = self.app.query_one("#tabbed-content", TabbedContent)
        except Exception:
            return
        if not tabbed_content.active == "transliterate":
            return
        self.translation_worker("transliterate",
                                text=self.query_one("#transliterate-input-text", Input).value,
                                dest_lang=self.query_one("#transliterate-result-language", LanguageButton).language,
                                source_lang=self.query_one("#transliterate-input-language", LanguageButton).language)

    def spellcheck_view(self):
        """Draws the `spellcheck` method view"""
        yield SectionTitle(self.localization.input)
        yield Container(LanguageButton(id="spellcheck-input-language", on_language_change=self.request_spellcheck),
                        Input("", classes="input", id="spellcheck-input-text", on_blur=self.additional_on_blur),
                        classes="text-container")
        yield SectionTitle(self.localization.result)
        yield Container(Static("", classes="result result-static", id="spellcheck-result-text"),
                        Static("", classes="service", id="spellcheck-result-service"), classes="text-container")

    def update_spellcheck_view(self, result: typing.Union[models.SpellcheckResult, models.RichSpellcheckResult]):
        """Updates the `spellcheck` method view"""
        try:
            tabbed_content = self.app.query_one("#tabbed-content", TabbedContent)
        except Exception:
            return
        if not tabbed_content.active == "spellcheck":
            return
        input_lang_btn = self.query_one("#spellcheck-input-language", LanguageButton)
        if input_lang_btn.language == AUTOMATIC:
            input_lang_btn.set_extra_language(result.source_lang)
        else:
            input_lang_btn.set_language(result.source_lang)

        if isinstance(result, models.RichSpellcheckResult):
            result_text = result.__pretty__()
        else:
            result_text = result.corrected
        self.query_one("#spellcheck-input-text", Input).value = result.source
        self.query_one("#spellcheck-result-text", Static).update(result_text)
        self.query_one("#spellcheck-result-service", Static).update(self.localization.service.format(service=str(result.service)))

    def request_spellcheck(self, *args, **kwargs):
        """Request a work from `translator`"""
        try:
            tabbed_content = self.app.query_one("#tabbed-content", TabbedContent)
        except Exception:
            return
        if not tabbed_content.active == "spellcheck":
            return
        self.translation_worker("spellcheck",
                                text=self.query_one("#spellcheck-input-text", Input).value,
                                source_lang=self.query_one("#spellcheck-input-language", LanguageButton).language)

    def language_view(self):
        """Draws the `language` method view"""
        yield SectionTitle(self.localization.input)
        yield Container(Input("", classes="input", id="language-input-text", on_blur=self.additional_on_blur),
                        classes="text-container")
        yield SectionTitle(self.localization.result)
        yield Container(Static("", classes="result result-static", id="language-result-text"),
                        Static("", classes="service", id="language-result-service"), classes="text-container")

    def update_language_view(self, result: models.LanguageResult):
        """Updates the `language` method view"""
        try:
            tabbed_content = self.app.query_one("#tabbed-content", TabbedContent)
        except Exception:
            return
        if not tabbed_content.active == "language":
            return
        native = result.language.native
        if native == result.language.name:
            result_text = native
        else:
            result_text = f"{native} ({result.language.name})"

        self.query_one("#language-input-text", Input).value = result.source
        self.query_one("#language-result-text", Static).update(result_text)
        self.query_one("#language-result-service", Static).update(self.localization.service.format(service=str(result.service)))

    def request_language(self, *args, **kwargs):
        """Request a work from `translator`"""
        try:
            tabbed_content = self.app.query_one("#tabbed-content", TabbedContent)
        except Exception:
            return
        if not tabbed_content.active == "language":
            return
        self.translation_worker("language",
                                text=self.query_one("#language-input-text", Input).value)

    def example_view(self):
        """Draws the `example` method view"""
        yield SectionTitle(self.localization.input)
        yield Container(LanguageButton(id="example-input-language", on_language_change=self.request_example),
                        Input("", classes="input", id="example-input-text", on_blur=self.additional_on_blur),
                        classes="text-container")
        yield SectionTitle(self.localization.result)
        yield Container(Static("", classes="result result-static", id="example-result-text"),
                        Static("", classes="service", id="example-result-service"), classes="text-container")

    def update_example_view(self, results: typing.List[models.ExampleResult]):
        """Updates the `example` method view"""
        try:
            tabbed_content = self.app.query_one("#tabbed-content", TabbedContent)
        except Exception:
            return
        if not tabbed_content.active == "example":
            return
        result = results[0] if results else None
        input_lang_btn = self.query_one("#example-input-language", LanguageButton)
        if not result:
            result = models.ExampleResult(
                service="translatepy",
                source=self.query_one("#example-input-text", Input).value,
                source_lang=input_lang_btn.language,
                example="(no example available)"
            )
        if input_lang_btn.language == AUTOMATIC:
            input_lang_btn.set_extra_language(result.source_lang)
        else:
            input_lang_btn.set_language(result.source_lang)

        self.query_one("#example-input-text", Input).value = result.source
        self.query_one("#example-result-text", Static).update(result.__pretty__())
        self.query_one("#example-result-service", Static).update(self.localization.service.format(service=str(result.service)))

    def request_example(self, *args, **kwargs):
        """Request a work from `translator`"""
        try:
            tabbed_content = self.app.query_one("#tabbed-content", TabbedContent)
        except Exception:
            return
        if not tabbed_content.active == "example":
            return
        self.translation_worker("example",
                                text=self.query_one("#example-input-text", Input).value,
                                source_lang=self.query_one("#example-input-language", LanguageButton).language)

    def dictionary_view(self):
        """Draws the `dictionary` method view"""
        yield SectionTitle(self.localization.input)
        yield Container(LanguageButton(id="dictionary-input-language", on_language_change=self.request_dictionary),
                        Input("", classes="input", id="dictionary-input-text", on_blur=self.additional_on_blur),
                        classes="text-container")
        yield SectionTitle(self.localization.result)
        yield Container(Static("", classes="result result-static", id="dictionary-result-text"),
                        Static("", classes="service", id="dictionary-result-service"), classes="text-container")

    def update_dictionary_view(self, results: typing.List[typing.Union[models.DictionaryResult, models.RichDictionaryResult]]):
        """Updates the `dictionary` method view"""
        try:
            tabbed_content = self.app.query_one("#tabbed-content", TabbedContent)
        except Exception:
            return
        if not tabbed_content.active == "dictionary":
            return
        result = results[0] if results else None
        input_lang_btn = self.query_one("#dictionary-input-language", LanguageButton)
        if not result:
            result = models.DictionaryResult(
                service="translatepy",
                source=self.query_one("#dictionary-input-text", Input).value,
                source_lang=input_lang_btn.language,
                meaning="(no meaning available)"
            )
        if input_lang_btn.language == AUTOMATIC:
            input_lang_btn.set_extra_language(result.source_lang)
        else:
            input_lang_btn.set_language(result.source_lang)

        self.query_one("#dictionary-input-text", Input).value = result.source
        self.query_one("#dictionary-result-text", Static).update(result.__pretty__())
        self.query_one("#dictionary-result-service", Static).update(self.localization.service.format(service=str(result.service)))

    def request_dictionary(self, *args, **kwargs):
        """Request a work from `translator`"""
        try:
            tabbed_content = self.app.query_one("#tabbed-content", TabbedContent)
        except Exception:
            return
        if not tabbed_content.active == "dictionary":
            return
        self.translation_worker("dictionary",
                                text=self.query_one("#dictionary-input-text", Input).value,
                                source_lang=self.query_one("#dictionary-input-language", LanguageButton).language)

    # def text_to_speech_view(self):
    #     """Draws the `text_to_speech` method view"""
    #     yield Static("Hello world text to speech")

    # pylint: disable=pointless-string-statement
    """
    ╭────────────────────────── Event Handlers ────────────────────────────────╮
    │ on_mount                                                                 │
    ╰──────────────────────────────────────────────────────────────────────────╯
    """

    def on_mount(self):
        """When mounted"""
        # Yea it's a pain to change the Header Icon
        self.query_one(Header).query_one(_header.HeaderIcon).icon = "🌐"

    # pylint: disable=pointless-string-statement
    """
    ╭────────────────────────── Binding actions ───────────────────────────────╮
    │ action_toggle_dark                                                       │
    │ action_open_options                                                      │
    │ replace_options                                                          │
    │ action_request_quit                                                      │
    │ translation_worker                                                       │
    ╰──────────────────────────────────────────────────────────────────────────╯
    """

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark

    def action_open_options(self):
        """When the user wants to see the options screen"""
        self.push_screen(TranslatepyOptionsScreen(options=self.options,
                                                  id="options-screen",
                                                  localization=self.localization),
                         self.replace_options)

    def replace_options(self, options: TranslatepyOptions):
        """To replace the current options"""
        self.options = options
        TranslatepyOptionsScreen.dumps("tui", options)
        self.localization = language_to_localization(self.options.language)

    def action_request_quit(self) -> None:
        """Action to display the quit dialog."""
        self.push_screen(QuitScreen(localization=self.localization))

    @work(exclusive=True)
    def translation_worker(self, action: str, **kwargs):
        """The worker thread which actually makes the request"""
        worker = get_current_worker()
        if worker.is_cancelled:
            return
        result = getattr(self.translator, action)(**kwargs)
        if worker.is_cancelled:
            return
        getattr(self, f"update_{action}_view")(result)

    # pylint: disable=pointless-string-statement
    """
    ╭──────────────────────── Reactive handlers ────────────────────────────╮
    │ watch_localization                                                    │
    ╰───────────────────────────────────────────────────────────────────────╯
    """

    def watch_localization(self, localization: typing.Type[Localization]) -> None:
        """Called when `localization` is modified"""
        # self.refresh(repaint=True, layout=True)
        self.app.exit()
        self.app.run()


if __name__ == "__main__":
    TranslatepyTUI().run()
