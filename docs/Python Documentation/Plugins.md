# Plugins

You can easily create your own translator by inheriting the "BaseTranslator" class (`translatepy.translators.base.BaseTranslator`)

## Table of Content

- [Usage](#usage)
- [Template](#template)
- [Best Practices](#best-practices)

## Usage

You can use plugins by importing them and using as normal translatepy translators.

You can also import them and add them to the `services_list` parameter in the `Translate`/`Translator` class.

To dynamic import them (using the CLI, the API or any other interface using a text-based translator definition/the dynamic translator importer), you need to give the *dot path* of the translator.

> Example : translatepy.translators.google.GoogleTranslate

## Template

If you want to create your own translator, you can use the following template :

```python
from translatepy.language import Language
from translatepy.utils.request import Request
from translatepy.translators.base import BaseTranslator, BaseTranslateException
from translatepy.utils.annotations import Tuple, List

class TranslatorNameException(BaseTranslateException):
    error_codes = {
        429: "Too many requests" # add your own status codes and error
    }

    # you can use it like so in your endpoint:
    # raise TranslateNameException(request.status_code)

class TranslatorName(BaseTranslator):
    """
    translatepy's implementation of <TranslatorName>
    """

    _supported_languages = {"set", "of", "supported", "language", "code"}

    def __init__(self, request: Request = Request()):
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

    def _example(self, text: str, destination_language: str, source_language: str) -> Tuple[str, List]:
        """
        This is the examples endpoint

        Must return a tuple with (detected_language, result)
        """
        # You could use `self.session` to make a request to the endpoint, with all of the parameters
        # Then extract the detected language (or use the "source_language" parameter but what if the user pass in "auto")
        # the result should be a list of use examples
        return detected_language, result

    def _dictionary(self, text: str, destination_language: str, source_language: str) -> Tuple[str, List]:
        """
        This is the dictionary endpoint

        Must return a tuple with (detected_language, result)
        """
        # You could use `self.session` to make a request to the endpoint, with all of the parameters
        # Then extract the detected language (or use the "source_language" parameter but what if the user pass in "auto")
        # the result should be
        return detected_language, result

    def _language_normalize(self, language: Language) -> str:
        """
        This is the language validation function
        It receives a "translatepy.language.Language" object and returns the correct language code

        Must return a string with the correct language code
        """
        return result


    def _language_denormalize(self, language_code: str) -> Language:
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

## Best Practices

### Requests

Using the object passed in "request" is highly suggested because it is the one passed in by the user (which is in most of the cases our translatepy's version of requests' `Request` object).

### Caching

Responses will be cached in the Base class if successful

### Supported Languages

The `_supported_languages` set is optional but highly recommended : it avoids making unneeded requests.

### Recursion

Avoid making big loops and recursions to wait for a valid result, if the user is using the `Translator` class, you might tremendously slow down the execution of the user's program.

### Unsupported Methods/Endpoints

Your source might not support some of the available features, in which case you need to raise the `translatepy.exceptions.UnsupportedMethod`exception to let `Translator` know that this is an unsupported feature.

### Non "_" prefixed functions

You should not use the normal functions/methods for the naming of the features you implement. They are used by the `BaseTranslator` class to make verifications, cache and shape your responses before giving it back to the user.

### Usage

The user will be able to use your plugin by importing it and using it normally or adding it to the `services_list` parameter in the `Translator` class.
