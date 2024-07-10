"""
The base strings
"""
import pathlib
import inspect


# We are using a special `classproperty` because
# the chaining of `@property` and `@classmethod`
# got deprecated in 3.11
class classproperty(property):
    """A class property"""

    def __get__(self, owner_self, owner_cls):
        if self.fget:
            return self.fget(owner_cls)


class Localization:
    """
    translatepy localization
    """
    __native__ = "Base"
    """The native name for the localization language"""

    @classproperty
    def __id__(cls):  # pylint: disable=no-self-argument
        return pathlib.Path(inspect.getfile(cls)).stem

    @classproperty
    def __english__(cls):  # pylint: disable=no-self-argument
        # Might change this later to support MultipleCaseNames
        # pylint: disable=no-member
        return cls.__name__.lower().removesuffix("localization").title()

    input = "Input"
    result = "Result"
    service = "by {service}"
    language = "Language"
    language_notice = "You need to restart the app to apply the changes"
    options = "Options"
    quit = "Quit"
    theme = "Theme"

    name = "Name"
    value = "Value"

    min = "Min"
    average = "Avg"
    max = "Max"

    cancel = "Cancel"
    quit_confirmation = "Are you sure you want to quit?"

    filter = "Filter"

    action_translate = "Translate"
    action_transliterate = "Transliterate"
    action_spellcheck = "Spellcheck"
    action_language = "Language"
    action_example = "Example"
    action_dictionary = "Dictionary"
    action_text_to_speech = "Text to Speech"
