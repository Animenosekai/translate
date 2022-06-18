
# Translation Section API Reference

This file lists and explains the different endpoints available in the Translation section.

## Translate


        Translates the given text to the given language

        i.e Good morning (en) --> おはようございます (ja)
        

```http
GET /translate
```

> [/opt/homebrew/lib/python3.9/site-packages/translatepy/server/translation.py](../..//opt/homebrew/lib/python3.9/site-packages/translatepy/server/translation.py#L45)

### Authentication

Login is **not** required

### Parameters

| Name         | Description                      | Required         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `text` | The text to translate  | True            | str            |
| `dest` | The destination language  | True            | str            |
| `source` | The source language  | False            | str            |
| `translators` | The translator(s) to use. When providing multiple translators, the names should be comma-separated.  | False            | TranslatorList            |
| `foreign` | Whether to include the language in foreign languages  | False            | Bool            |

### Example

<!-- tabs:start -->

#### **cURL**

```bash
curl -X GET \
    --data-urlencode "text=<The text to translate>"\
    --data-urlencode "dest=<The destination language>" \
    "/translate"
```

#### **JavaScript**

```bash
fetch(`/translate?text=${encodeURIComponent("text")}&dest=${encodeURIComponent("dest")}`, {
    method: "GET"
})
.then((response) => {response.json()})
.then((response) => {
    if (response.success) {
        console.info("Successfully requested for /translate")
        console.log(response.data)
    } else {
        console.error("An error occured while requesting for /translate, error: " + response.error)
    }
})
```

#### **Python**

```bash
import requests
r = requests.request("GET", "/translate",
        params = {
            "text": "The text to translate",
            "dest": "The destination language"
        })
if r.status_code >= 400 or not r.json()["success"]:
    raise ValueError("An error occured while requesting for /translate, error: " + r.json()["error"])
print("Successfully requested for /translate")
print(r.json()["data"])
```
<!-- tabs:end -->

### Response

#### Example Response

```json
{
    "success": true,
    "message": "Successfully processed your request",
    "error": null,
    "data": {
        "service": "Google",
        "source": "Hello world",
        "sourceLanguage": {
            "alpha3b": "eng",
            "extra": {
                "type": "Living",
                "scope": "Individual"
            },
            "alpha2": "en",
            "inForeignLanguages": {},
            "id": "eng",
            "alpha3t": "eng",
            "name": "English",
            "alpha3": "eng"
        },
        "destinationLanguage": {
            "alpha3b": "eng",
            "extra": {
                "type": "Living",
                "scope": "Individual"
            },
            "alpha2": "en",
            "inForeignLanguages": {},
            "id": "eng",
            "alpha3t": "eng",
            "name": "English",
            "alpha3": "eng"
        },
        "result": "こんにちは世界"
    }
}

```

#### Returns

| Field        | Description                      | Type   | Nullable  |
| ----------   | -------------------------------- | ------ | --------- |
| `service` | The translator used  | str      | False      |
| `source` | The source text  | str      | False      |
| `sourceLanguage` | The source language  | object      | False      |
| `destinationLanguage` | The destination language  | object      | False      |
| `result` | The translated text  | str      | False      |

#### Possible Errors

| Exception         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy. This is the base class for the other exceptions raised by translatepy.  | 500  |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `PARAMETER_ERROR` | When a parameter is missing or invalid  | 500  |
| `PARAMETER_TYPE_ERROR` | When a parameter is of the wrong type  | 500  |
| `PARAMETER_VALUE_ERROR` | When a parameter is of the wrong value  | 500  |
| `TRANSLATION_ERROR` | When a translation error occurs  | 500  |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
[Return to the Index](../Getting%20Started.md#index)

## Translation Stream


        Translates the given text to the given language

        i.e Good morning (en) --> おはようございます (ja)
         This endpoint returns a stream of results.

```http
GET /stream
```

> [server/endpoints/translation.py](../../server/endpoints/translation.py#L44)

### Authentication

Login is **not** required

### Parameters

| Name         | Description                      | Required         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `text` | The text to translate  | True            | str            |
| `dest` | The destination language  | True            | str            |
| `source` | The source language  | False            | str            |
| `translators` | The translator(s) to use. When providing multiple translators, the names should be comma-separated.  | False            | TranslatorList            |
| `foreign` | Whether to include the language in foreign languages  | False            | Bool            |

### Example

<!-- tabs:start -->

#### **cURL**

```bash
curl -X GET \
    --data-urlencode "text=<The text to translate>"\
    --data-urlencode "dest=<The destination language>" \
    "/stream"
```

#### **JavaScript**

```bash
fetch(`/stream?text=${encodeURIComponent("text")}&dest=${encodeURIComponent("dest")}`, {
    method: "GET"
})
.then((response) => {response.json()})
.then((response) => {
    if (response.success) {
        console.info("Successfully requested for /stream")
        console.log(response.data)
    } else {
        console.error("An error occured while requesting for /stream, error: " + response.error)
    }
})
```

#### **Python**

```bash
import requests
r = requests.request("GET", "/stream",
        params = {
            "text": "The text to translate",
            "dest": "The destination language"
        })
if r.status_code >= 400 or not r.json()["success"]:
    raise ValueError("An error occured while requesting for /stream, error: " + r.json()["error"])
print("Successfully requested for /stream")
print(r.json()["data"])
```
<!-- tabs:end -->

### Response

#### Example Response

```json
{
    "success": true,
    "message": "Successfully processed your request",
    "error": null,
    "data": {
        "service": "Google",
        "source": "Hello world",
        "sourceLanguage": {
            "alpha3b": "eng",
            "extra": {
                "type": "Living",
                "scope": "Individual"
            },
            "alpha2": "en",
            "inForeignLanguages": {},
            "id": "eng",
            "alpha3t": "eng",
            "name": "English",
            "alpha3": "eng"
        },
        "destinationLanguage": {
            "alpha3b": "eng",
            "extra": {
                "type": "Living",
                "scope": "Individual"
            },
            "alpha2": "en",
            "inForeignLanguages": {},
            "id": "eng",
            "alpha3t": "eng",
            "name": "English",
            "alpha3": "eng"
        },
        "result": "こんにちは世界"
    }
}

```

#### Returns

| Field        | Description                      | Type   | Nullable  |
| ----------   | -------------------------------- | ------ | --------- |
| `service` | The translator used  | str      | False      |
| `source` | The source text  | str      | False      |
| `sourceLanguage` | The source language  | object      | False      |
| `destinationLanguage` | The destination language  | object      | False      |
| `result` | The translated text  | str      | False      |

#### Possible Errors

| Exception         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy. This is the base class for the other exceptions raised by translatepy.  | 500  |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `PARAMETER_ERROR` | When a parameter is missing or invalid  | 500  |
| `PARAMETER_TYPE_ERROR` | When a parameter is of the wrong type  | 500  |
| `PARAMETER_VALUE_ERROR` | When a parameter is of the wrong value  | 500  |
| `TRANSLATION_ERROR` | When a translation error occurs  | 500  |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
[Return to the Index](../Getting%20Started.md#index)

## Translate HTML


        Translates the given HTML string or BeautifulSoup object to the given language

        i.e
         English: `<div class="hello"><h1>Hello</h1> everyone and <a href="/welcome">welcome</a> to <span class="w-full">my website</span></div>`
         French: `<div class="hello"><h1>Bonjour</h1>tout le monde et<a href="/welcome">Bienvenue</a>à<span class="w-full">Mon site internet</span></div>`

        Note: This method is not perfect since it is not tag/context aware. Example: `<span>Hello <strong>everyone</strong></span>` will not be understood as
        "Hello everyone" with "everyone" in bold but rather "Hello" and "everyone" separately.

        Warning: If you give a `bs4.BeautifulSoup`, `bs4.element.PageElement` or `bs4.element.Tag` input (which are mutable), they will be modified.
        If you don't want this behavior, please make sure to pass the string version of the element:
        >>> result = Translate().translate_html(str(page_element), "French")

        Parameters:
        ----------
            html : str | bs4.element.PageElement | bs4.element.Tag | bs4.BeautifulSoup
                The HTML string to be translated. This can also be an instance of BeautifulSoup's `BeautifulSoup` element, `PageElement` or `Tag` element.
            destination_language : str
                The language the HTML string needs to be translated in.
            source_language : str, default = "auto"
                The language of the HTML string.
            parser : str, default = "html.parser"
                The parser that BeautifulSoup will use to parse the HTML string.
            threads_limit : int, default = 100
                The maximum number of threads that will be spawned by translate_html
            __internal_replacement_function__ : function, default = None
                This is used internally, especially by the translatepy HTTP server to modify the translation step.

        Returns:
        --------
            BeautifulSoup:
                The result will be the same element as the input `html` parameter with the values modified if the given
                input is of bs4.BeautifulSoup, bs4.element.PageElement or bs4.element.Tag instance.
            str:
                The result will be a string in any other case.

        

```http
GET /html
```

> [/opt/homebrew/lib/python3.9/site-packages/translatepy/server/translation.py](../..//opt/homebrew/lib/python3.9/site-packages/translatepy/server/translation.py#L206)

### Authentication

Login is **not** required

### Parameters

| Name         | Description                      | Required         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `code` | The HTML snippet to translate  | True            | str            |
| `dest` | The destination language  | True            | str            |
| `source` | The source language  | False            | str            |
| `parser` | The HTML parser to use  | False            | str            |
| `translators` | The translator(s) to use. When providing multiple translators, the names should be comma-separated.  | False            | TranslatorList            |
| `foreign` | Whether to include the language in foreign languages  | False            | Bool            |

### Example

<!-- tabs:start -->

#### **cURL**

```bash
curl -X GET \
    --data-urlencode "code=<The HTML snippet to translate>"\
    --data-urlencode "dest=<The destination language>" \
    "/html"
```

#### **JavaScript**

```bash
fetch(`/html?code=${encodeURIComponent("code")}&dest=${encodeURIComponent("dest")}`, {
    method: "GET"
})
.then((response) => {response.json()})
.then((response) => {
    if (response.success) {
        console.info("Successfully requested for /html")
        console.log(response.data)
    } else {
        console.error("An error occured while requesting for /html, error: " + response.error)
    }
})
```

#### **Python**

```bash
import requests
r = requests.request("GET", "/html",
        params = {
            "code": "The HTML snippet to translate",
            "dest": "The destination language"
        })
if r.status_code >= 400 or not r.json()["success"]:
    raise ValueError("An error occured while requesting for /html, error: " + r.json()["error"])
print("Successfully requested for /html")
print(r.json()["data"])
```
<!-- tabs:end -->

### Response

#### Example Response

```json
{
    "success": true,
    "message": "Successfully processed your request",
    "error": null,
    "data": {
        "services": [
            "Google",
            "Bing"
        ],
        "source": "<div><p>Hello, how are you today</p><p>Comment allez-vous</p></div>",
        "sourceLanguage": [
            "fra",
            "eng"
        ],
        "destinationLanguage": {
            "alpha3b": "eng",
            "extra": {
                "type": "Living",
                "scope": "Individual"
            },
            "alpha2": "en",
            "inForeignLanguages": {},
            "id": "eng",
            "alpha3t": "eng",
            "name": "English",
            "alpha3": "eng"
        },
        "result": "<div><p>こんにちは、今日はお元気ですか</p><p>大丈夫</p></div>"
    }
}

```

#### Returns

| Field        | Description                      | Type   | Nullable  |
| ----------   | -------------------------------- | ------ | --------- |
| `services` | The translators used  | array      | False      |
| `source` | The source text  | str      | False      |
| `sourceLanguage` | The source languages  | array      | False      |
| `destinationLanguage` | The destination language  | object      | False      |
| `result` | The translated text  | str      | False      |

#### Possible Errors

| Exception         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy. This is the base class for the other exceptions raised by translatepy.  | 500  |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `PARAMETER_ERROR` | When a parameter is missing or invalid  | 500  |
| `PARAMETER_TYPE_ERROR` | When a parameter is of the wrong type  | 500  |
| `PARAMETER_VALUE_ERROR` | When a parameter is of the wrong value  | 500  |
| `TRANSLATION_ERROR` | When a translation error occurs  | 500  |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
[Return to the Index](../Getting%20Started.md#index)

## Transliterate


        Transliterates the given text, get its pronunciation

        i.e おはよう --> Ohayou
        

```http
GET /transliterate
```

> [/opt/homebrew/lib/python3.9/site-packages/translatepy/server/translation.py](../..//opt/homebrew/lib/python3.9/site-packages/translatepy/server/translation.py#L284)

### Authentication

Login is **not** required

### Parameters

| Name         | Description                      | Required         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `text` | The text to transliterate  | True            | str            |
| `dest` | The destination language  | False            | str            |
| `source` | The source language  | False            | str            |
| `translators` | The translator(s) to use. When providing multiple translators, the names should be comma-separated.  | False            | TranslatorList            |
| `foreign` | Whether to include the language in foreign languages  | False            | Bool            |

### Example

<!-- tabs:start -->

#### **cURL**

```bash
curl -X GET \
    --data-urlencode "text=<The text to transliterate>" \
    "/transliterate"
```

#### **JavaScript**

```bash
fetch(`/transliterate?text=${encodeURIComponent("text")}`, {
    method: "GET"
})
.then((response) => {response.json()})
.then((response) => {
    if (response.success) {
        console.info("Successfully requested for /transliterate")
        console.log(response.data)
    } else {
        console.error("An error occured while requesting for /transliterate, error: " + response.error)
    }
})
```

#### **Python**

```bash
import requests
r = requests.request("GET", "/transliterate",
        params = {
            "text": "The text to transliterate"
        })
if r.status_code >= 400 or not r.json()["success"]:
    raise ValueError("An error occured while requesting for /transliterate, error: " + r.json()["error"])
print("Successfully requested for /transliterate")
print(r.json()["data"])
```
<!-- tabs:end -->

### Response

#### Example Response

```json
{
    "success": true,
    "message": "Successfully processed your request",
    "error": null,
    "data": {
        "service": "Google",
        "source": "おはよう",
        "sourceLanguage": {
            "alpha3b": "eng",
            "extra": {
                "type": "Living",
                "scope": "Individual"
            },
            "alpha2": "en",
            "inForeignLanguages": {},
            "id": "eng",
            "alpha3t": "eng",
            "name": "English",
            "alpha3": "eng"
        },
        "destinationLanguage": {
            "alpha3b": "eng",
            "extra": {
                "type": "Living",
                "scope": "Individual"
            },
            "alpha2": "en",
            "inForeignLanguages": {},
            "id": "eng",
            "alpha3t": "eng",
            "name": "English",
            "alpha3": "eng"
        },
        "result": "Ohayou"
    }
}

```

#### Returns

| Field        | Description                      | Type   | Nullable  |
| ----------   | -------------------------------- | ------ | --------- |
| `service` | The translator used  | str      | False      |
| `source` | The source text  | str      | False      |
| `sourceLanguage` | The source language  | object      | False      |
| `destinationLanguage` | The destination language  | object      | False      |
| `result` | The transliteration  | str      | False      |

#### Possible Errors

| Exception         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy. This is the base class for the other exceptions raised by translatepy.  | 500  |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `PARAMETER_ERROR` | When a parameter is missing or invalid  | 500  |
| `PARAMETER_TYPE_ERROR` | When a parameter is of the wrong type  | 500  |
| `PARAMETER_VALUE_ERROR` | When a parameter is of the wrong value  | 500  |
| `TRANSLATION_ERROR` | When a translation error occurs  | 500  |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
[Return to the Index](../Getting%20Started.md#index)

## Spellcheck


        Checks the spelling of a given text

        i.e God morning --> Good morning
        

```http
GET /spellcheck
```

> [/opt/homebrew/lib/python3.9/site-packages/translatepy/server/translation.py](../..//opt/homebrew/lib/python3.9/site-packages/translatepy/server/translation.py#L340)

### Authentication

Login is **not** required

### Parameters

| Name         | Description                      | Required         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `text` | The text to spellcheck  | True            | str            |
| `source` | The source language  | False            | str            |
| `translators` | The translator(s) to use. When providing multiple translators, the names should be comma-separated.  | False            | TranslatorList            |
| `foreign` | Whether to include the language in foreign languages  | False            | Bool            |

### Example

<!-- tabs:start -->

#### **cURL**

```bash
curl -X GET \
    --data-urlencode "text=<The text to spellcheck>" \
    "/spellcheck"
```

#### **JavaScript**

```bash
fetch(`/spellcheck?text=${encodeURIComponent("text")}`, {
    method: "GET"
})
.then((response) => {response.json()})
.then((response) => {
    if (response.success) {
        console.info("Successfully requested for /spellcheck")
        console.log(response.data)
    } else {
        console.error("An error occured while requesting for /spellcheck, error: " + response.error)
    }
})
```

#### **Python**

```bash
import requests
r = requests.request("GET", "/spellcheck",
        params = {
            "text": "The text to spellcheck"
        })
if r.status_code >= 400 or not r.json()["success"]:
    raise ValueError("An error occured while requesting for /spellcheck, error: " + r.json()["error"])
print("Successfully requested for /spellcheck")
print(r.json()["data"])
```
<!-- tabs:end -->

### Response

#### Example Response

```json
{
    "success": true,
    "message": "Successfully processed your request",
    "error": null,
    "data": {
        "service": "Google",
        "source": "God morning",
        "sourceLang": {
            "alpha3b": "eng",
            "extra": {
                "type": "Living",
                "scope": "Individual"
            },
            "alpha2": "en",
            "inForeignLanguages": {},
            "id": "eng",
            "alpha3t": "eng",
            "name": "English",
            "alpha3": "eng"
        },
        "result": "Good morning"
    }
}

```

#### Returns

| Field        | Description                      | Type   | Nullable  |
| ----------   | -------------------------------- | ------ | --------- |
| `service` | The translator used  | str      | False      |
| `source` | The source text  | str      | False      |
| `sourceLang` | The source language  | object      | False      |
| `result` | The spellchecked text  | str      | False      |

#### Possible Errors

| Exception         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy. This is the base class for the other exceptions raised by translatepy.  | 500  |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `PARAMETER_ERROR` | When a parameter is missing or invalid  | 500  |
| `PARAMETER_TYPE_ERROR` | When a parameter is of the wrong type  | 500  |
| `PARAMETER_VALUE_ERROR` | When a parameter is of the wrong value  | 500  |
| `TRANSLATION_ERROR` | When a translation error occurs  | 500  |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
[Return to the Index](../Getting%20Started.md#index)

## Language


        Returns the language of the given text

        i.e 皆さんおはようございます！ --> Japanese
        

```http
GET /language
```

> [/opt/homebrew/lib/python3.9/site-packages/translatepy/server/translation.py](../..//opt/homebrew/lib/python3.9/site-packages/translatepy/server/translation.py#L394)

### Authentication

Login is **not** required

### Parameters

| Name         | Description                      | Required         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `text` | The text to get the language of  | True            | str            |
| `translators` | The translator(s) to use. When providing multiple translators, the names should be comma-separated.  | False            | TranslatorList            |
| `foreign` | Whether to include the language in foreign languages  | False            | Bool            |

### Example

<!-- tabs:start -->

#### **cURL**

```bash
curl -X GET \
    --data-urlencode "text=<The text to get the language of>" \
    "/language"
```

#### **JavaScript**

```bash
fetch(`/language?text=${encodeURIComponent("text")}`, {
    method: "GET"
})
.then((response) => {response.json()})
.then((response) => {
    if (response.success) {
        console.info("Successfully requested for /language")
        console.log(response.data)
    } else {
        console.error("An error occured while requesting for /language, error: " + response.error)
    }
})
```

#### **Python**

```bash
import requests
r = requests.request("GET", "/language",
        params = {
            "text": "The text to get the language of"
        })
if r.status_code >= 400 or not r.json()["success"]:
    raise ValueError("An error occured while requesting for /language, error: " + r.json()["error"])
print("Successfully requested for /language")
print(r.json()["data"])
```
<!-- tabs:end -->

### Response

#### Example Response

```json
{
    "success": true,
    "message": "Successfully processed your request",
    "error": null,
    "data": {
        "service": "Google",
        "source": "Hello world",
        "result": {
            "alpha3b": "eng",
            "extra": {
                "type": "Living",
                "scope": "Individual"
            },
            "alpha2": "en",
            "inForeignLanguages": {},
            "id": "eng",
            "alpha3t": "eng",
            "name": "English",
            "alpha3": "eng"
        }
    }
}

```

#### Returns

| Field        | Description                      | Type   | Nullable  |
| ----------   | -------------------------------- | ------ | --------- |
| `service` | The translator used  | str      | False      |
| `source` | The source text  | str      | False      |
| `result` | The resulting language alpha-3 code  | object      | False      |

#### Possible Errors

| Exception         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy. This is the base class for the other exceptions raised by translatepy.  | 500  |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `PARAMETER_ERROR` | When a parameter is missing or invalid  | 500  |
| `PARAMETER_TYPE_ERROR` | When a parameter is of the wrong type  | 500  |
| `PARAMETER_VALUE_ERROR` | When a parameter is of the wrong value  | 500  |
| `TRANSLATION_ERROR` | When a translation error occurs  | 500  |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
[Return to the Index](../Getting%20Started.md#index)

## Text to Speech


        Gives back the text to speech result for the given text

        Args:
          text: the given text
          source_language: the source language

        Returns:
            the mp3 file as bytes

        Example:
            >>> from translatepy import Translator
            >>> t = Translator()
            >>> result = t.text_to_speech("Hello, how are you?")
            >>> with open("output.mp3", "wb") as output: # open a binary (b) file to write (w)
            ...     output.write(result.result)
                    # or:
                    result.write_to_file(output)
            # Or you can just use write_to_file method:
            >>> result.write_to_file("output.mp3")
            >>> print("Output of Text to Speech is available in output.mp3!")

            # the result is an MP3 file with the text to speech output
        

```http
GET /tts
```

> [/opt/homebrew/lib/python3.9/site-packages/translatepy/server/translation.py](../..//opt/homebrew/lib/python3.9/site-packages/translatepy/server/translation.py#L434)

### Authentication

Login is **not** required

### Parameters

| Name         | Description                      | Required         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `text` | The text to convert to speech  | True            | str            |
| `source` | The source language  | False            | str            |
| `speed` | The speed of the speech  | False            | int            |
| `gender` | The gender of the speech  | False            | str            |
| `translators` | The translator(s) to use. When providing multiple translators, the names should be comma-separated.  | False            | TranslatorList            |

### Example

<!-- tabs:start -->

#### **cURL**

```bash
curl -X GET \
    --data-urlencode "text=<The text to convert to speech>" \
    "/tts"
```

#### **JavaScript**

```bash
fetch(`/tts?text=${encodeURIComponent("text")}`, {
    method: "GET"
})
.then((response) => {response.json()})
.then((response) => {
    if (response.success) {
        console.info("Successfully requested for /tts")
        console.log(response.data)
    } else {
        console.error("An error occured while requesting for /tts, error: " + response.error)
    }
})
```

#### **Python**

```bash
import requests
r = requests.request("GET", "/tts",
        params = {
            "text": "The text to convert to speech"
        })
if r.status_code >= 400 or not r.json()["success"]:
    raise ValueError("An error occured while requesting for /tts, error: " + r.json()["error"])
print("Successfully requested for /tts")
print(r.json()["data"])
```
<!-- tabs:end -->

#### Possible Errors

| Exception         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy. This is the base class for the other exceptions raised by translatepy.  | 500  |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `PARAMETER_ERROR` | When a parameter is missing or invalid  | 500  |
| `PARAMETER_TYPE_ERROR` | When a parameter is of the wrong type  | 500  |
| `PARAMETER_VALUE_ERROR` | When a parameter is of the wrong value  | 500  |
| `TRANSLATION_ERROR` | When a translation error occurs  | 500  |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
[Return to the Index](../Getting%20Started.md#index)