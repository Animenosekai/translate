# Plugins

You can easily create your own translator by adding inheriting the "BaseTranslator" class (`translatepy.translators.base.BaseTranslator`)

This is how your class should look like:

```python
from translatepy.language import Language
from translatepy.utils.request import Request
from translatepy.translators.base import BaseTranslator

class TranslatorName(BaseTranslator):
    """
    translatepy's implementation of <TranslatorName>
    """

    def __init__(self, request: Request):
        self.session = request

    def _translate(self, text: str, destination_language: str, source_language: str) -> str:
        """
        This is the translating endpoint

        Must return a tuple with (detected_language, result)
        """
        # You could use `self.session` to make a request to the endpoint, with all of the parameters
        # Then extract the detected language (or use the "source_language" parameter but what if the user pass in "auto")
        return detected_language, result

    def _transliterate(self, text: str, destination_language, source_language: str) -> str:
        """
        This is the transliterating endpoint

        Must return a tuple with (detected_language, result)
        """
        # You could use `self.session` to make a request to the endpoint, with all of the parameters
        # Then extract the detected language (or use the "source_language" parameter but what if the user pass in "auto")
        return detected_language, result


    def _spellcheck(self, text: str, source_language: str) -> str:
        """
        This is the spellcheking endpoint

        Must return a tuple with (detected_language, result)
        """
        # You could use `self.session` to make a request to the endpoint, with all of the parameters
        # Then extract the detected language (or use the "source_language" parameter but what if the user pass in "auto")
        # result should be the original text if no correction is made or the corrected text if found
        return detected_language, result

    def _language(self, text: str) -> str:
        """
        This is the language detection endpoint

        Must return a string with the language code
        """
        # You could use `self.session` to make a request to the endpoint, with all of the parameters
        return result

    def _example(self, text: str, destination_language: str, source_language: str) -> List:
        """
        This is the examples endpoint

        Must return a tuple with (detected_language, result)
        """
        # You could use `self.session` to make a request to the endpoint, with all of the parameters
        # Then extract the detected language (or use the "source_language" parameter but what if the user pass in "auto")
        # the result should be a list of use examples
        return detected_language, result

    def _dictionary(self, text: str, destination_language: str, source_language: str) -> List:
        """
        This is the dictionary endpoint

        Must return a tuple with (detected_language, result)
        """
        # You could use `self.session` to make a request to the endpoint, with all of the parameters
        # Then extract the detected language (or use the "source_language" parameter but what if the user pass in "auto")
        # the result should be
        return detected_language, result

    def _language_normalize(self, language) -> str:
        """
        This is the language validation function
        It receives a "translatepy.language.Language" object and returns the correct language code

        Must return a string with the correct language code
        """
        return result


    def _language_denormalize(self, language_code) -> str:
        """
        This is the language denormalization function
        It receives a string with the translator language code and returns a "translatepy.language.Language" object

        Must return a string with the correct language code
        """
        return result

    def __str__(self) -> str:
        """
        This is optional but you can use it if you want to change the way the class is represented as a string.

        It defaults (if not defined) to:
        ... class_name = self.__class__.__name__.split("Translate")[0]
        ... return "Unknown" if class_name == "" else class_name
        """
        return name

```
