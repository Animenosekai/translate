"""Form components"""
import typing

from textual.containers import Horizontal, Container
from textual.reactive import reactive
from textual.widgets import Label, Select
from nasse.tui.components.inputs import Input
from textual.css.query import NoMatches

from nasse.models import UserSent
from nasse.tui.widget import Widget
from nasse.tui.components.texts import SectionTitle
from nasse.localization import Localization, EnglishLocalization


class UserSentInput(Widget):
    """The input component for a user sent value"""
    value: reactive[typing.Optional[UserSent]] = reactive(None)

    DEFAULT_CSS = """
    UserSentInput {
        height: auto;
        margin: 1 0 1 0;
    }

    .form-input-container {
        height: auto;
    }

    .form-input-name {
        width: 15%;
        height: auto;
    }

    .form-input-value {
        width: 80%;
        height: auto;
    }

    .form-input-description {
        text-opacity: 0.5;
        margin-left: 1;
    }
    """
    input_name: reactive[typing.Optional[str]] = reactive(None)
    input_value: reactive[typing.Optional[str]] = reactive(None)

    def __init__(self,
                 user_sent: typing.Optional[UserSent] = None,
                 inputs: typing.Optional[typing.Set[UserSent]] = None,
                 on_change: typing.Optional[typing.Callable[["UserSentInput", typing.Optional[str], typing.Optional[str]], typing.Any]] = None,
                 initial_value: typing.Optional[str] = None,
                 localization: typing.Type[Localization] = EnglishLocalization,
                 **kwargs) -> None:

        super().__init__(**kwargs)
        self.user_sent = user_sent
        self.inputs = inputs or set()
        self.on_change = on_change
        self.localization = localization

        self.initial_value = initial_value
        if self.user_sent:
            self.input_name = self.user_sent.name

    def compose(self):
        if not self.inputs:
            with Horizontal(classes="form-input-container"):
                yield Input(value=self.user_sent.name if self.user_sent else None, placeholder=self.localization.name, classes="form-input-name", name="input-name")
                yield Input(value=self.initial_value, placeholder=self.localization.value, classes="form-input-value", name="input-value")
            return

        with Horizontal(classes="form-input-container"):
            if not self.user_sent:
                yield Select([(element.name, element) for element in self.inputs], classes="form-input-name", value=None, name="input-name")
                yield Input(disabled=False, classes="form-input-value", value=self.initial_value, name="input-value")
                return
            yield Select([(element.name, element) for element in self.inputs],
                         value=self.user_sent,
                         disabled=self.user_sent.required,
                         classes="form-input-name",
                         name="input-name")
            yield Input(placeholder=self.user_sent.type.__name__
                        if hasattr(self.user_sent.type, "__name__") else str(self.user_sent.type),
                        classes="form-input-value",
                        name="input-value")
        yield Label(self.user_sent.description or "" if self.user_sent else "", classes="form-input-description")

    def on_input_changed(self, event: Input.Changed) -> None:
        """When an input changed"""
        if event.input.name == "input-name":
            self.input_name = event.input.value
        elif event.input.name == "input-value":
            self.input_value = event.input.value

        if self.on_change:
            self.on_change(self, self.input_name, self.input_value)

    def on_select_changed(self, event: Select.Changed) -> None:
        """When a Select object changed"""
        if event.select.name == "input-name":
            val: typing.Optional[UserSent] = event.select.value
            self.input_name = val.name if val else None
            for inp in self.inputs:
                if inp.name == self.input_name:
                    try:
                        self.query_one(".form-input-description", Label).update(inp.description)
                    except NoMatches:
                        self.mount(Label(inp.description or "", classes="form-input-description"))
                    break

        if self.on_change:
            self.on_change(self, self.input_name, self.input_value)


class UserSentForm(Widget):
    """A form for user sent inputs"""

    DEFAULT_CSS = """
    UserSentForm {
        height: auto;
        margin-top: 1;
        margin-bottom: 1;
    }

    .form-inputs-container {
        height: auto;
    }

    .form-buttons {
        height: auto;
        align-horizontal: right;
    }

    .form-buttons-add {
        background: rgb(0, 162, 255);
        color: white;
    }

    .form-buttons-remove {
        opacity: 0.75;
    }
    """

    def __init__(self,
                 title: str,
                 inputs: typing.Optional[typing.Set[UserSent]] = None,
                 multiple: bool = False,
                 initial_values: typing.Optional[typing.List[typing.Tuple[UserSent, str]]] = None,
                 localization: typing.Type[Localization] = EnglishLocalization,
                 **kwargs) -> None:
        super().__init__(**kwargs)
        self.title = title
        self.inputs = inputs or set()
        self.multiple = multiple
        self.localization = localization

        self.initial_values = initial_values or []

    def compose(self):
        yield SectionTitle(self.title)

        initial_values = self.initial_values.copy()

        for element in self.inputs:
            if element.required:
                for user_sent, value in initial_values.copy():
                    if user_sent == element:
                        yield UserSentInput(element, inputs=self.inputs, initial_value=value, localization=self.localization)
                        initial_values.remove((user_sent, value))
                        break
                else:
                    yield UserSentInput(element, inputs=self.inputs, localization=self.localization)

        for user_sent, value in initial_values:
            yield UserSentInput(user_sent, inputs=self.inputs, initial_value=value, localization=self.localization)

        with Container(classes="form-inputs-container"):
            yield UserSentInput(None, self.inputs, self.on_change, localization=self.localization)

    #     with Horizontal(classes="form-buttons"):
    #         yield Button("Add", name="add", classes="form-buttons-add")
    #         yield Button("Remove", name="remove", classes="form-buttons-remove")

    def on_change(self, user_input: UserSentInput, name: typing.Optional[str] = None, value: typing.Optional[str] = None):
        """When something changed in any user input"""
        last_element: UserSentInput = self.query_one(".form-inputs-container", Container).query(UserSentInput).last()

        for element in self.query_one(".form-inputs-container", Container).query(UserSentInput)[:-1]:
            if not element.input_name and not element.input_value:
                element.remove()

        if last_element.input_name or last_element.input_value:
            self.query_one(".form-inputs-container", Container).mount(UserSentInput(None, self.inputs, self.on_change, localization=self.localization))

    @property
    def values(self):
        """Returns the rendered values"""
        results = {}
        # pylint: disable=not-an-iterable
        for element in self.query(UserSentInput):
            # if element.input_name and element.input_value:
            if element.input_name:
                if self.multiple:
                    try:
                        results[element.input_name].append(element.input_value)
                    except KeyError:
                        results[element.input_name] = [element.input_value]
                else:
                    results[element.input_name] = element.input_value
        return results

    # def on_button_pressed(self, event: Button.Pressed) -> None:
    #     """When a button is pressed"""
    #     if event.button.name == "add":
    #         self.query_one(".form-inputs-container", Container).mount(UserSentInput(None, self.inputs))
    #     elif event.button.name == "remove":
    #         self.query_one(".form-inputs-container", Container).query(UserSentInput).last().remove()
