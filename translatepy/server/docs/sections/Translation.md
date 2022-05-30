
# Translation Section API Reference

This file lists and explains the different endpoints available in the Translation section.

## Translate


        Translates the given text to the given language

        i.e Good morning (en) --> おはようございます (ja)
        

```http
GET /translate
```

> [translatepy/server/translation.py](../../translatepy/server/translation.py#L32)

### Authentication

Login is **not** required

### Parameters

| Name         | Description                      | Required         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `text` | The text to translate  | True            | str            |
| `dest` | The destination language  | True            | str            |
| `source` | The source language  | False            | str            |
| `translators` | The translator(s) to use. When providing multiple translators, the names should be comma-separated.  | False            | TranslatorList            |

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
        "sourceLang": "English",
        "destLang": "Japanese",
        "result": "こんにちは世界"
    }
}

```

#### Returns

| Field        | Description                      | Type   | Nullable  |
| ----------   | -------------------------------- | ------ | --------- |
| `service` | The translator used  | str      | False      |
| `source` | The source text  | str      | False      |
| `sourceLang` | The source language  | str      | False      |
| `destLang` | The destination language  | str      | False      |
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

> [translatepy/server/translation.py](../../translatepy/server/translation.py#L87)

### Authentication

Login is **not** required

### Parameters

| Name         | Description                      | Required         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `text` | The text to transliterate  | True            | str            |
| `dest` | The destination language  | False            | str            |
| `source` | The source language  | False            | str            |
| `translators` | The translator(s) to use. When providing multiple translators, the names should be comma-separated.  | False            | TranslatorList            |

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
        "sourceLang": "Japanese",
        "destLang": "English",
        "result": "Ohayou"
    }
}

```

#### Returns

| Field        | Description                      | Type   | Nullable  |
| ----------   | -------------------------------- | ------ | --------- |
| `service` | The translator used  | str      | False      |
| `source` | The source text  | str      | False      |
| `sourceLang` | The source language  | str      | False      |
| `destLang` | The destination language  | str      | False      |
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

> [translatepy/server/translation.py](../../translatepy/server/translation.py#L142)

### Authentication

Login is **not** required

### Parameters

| Name         | Description                      | Required         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `text` | The text to spellcheck  | True            | str            |
| `source` | The source language  | False            | str            |
| `translators` | The translator(s) to use. When providing multiple translators, the names should be comma-separated.  | False            | TranslatorList            |

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
        "sourceLang": "English",
        "result": "Good morning"
    }
}

```

#### Returns

| Field        | Description                      | Type   | Nullable  |
| ----------   | -------------------------------- | ------ | --------- |
| `service` | The translator used  | str      | False      |
| `source` | The source text  | str      | False      |
| `sourceLang` | The source language  | str      | False      |
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

> [translatepy/server/translation.py](../../translatepy/server/translation.py#L194)

### Authentication

Login is **not** required

### Parameters

| Name         | Description                      | Required         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `text` | The text to get the language of  | True            | str            |
| `translators` | The translator(s) to use. When providing multiple translators, the names should be comma-separated.  | False            | TranslatorList            |

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
        "result": "jpa"
    }
}

```

#### Returns

| Field        | Description                      | Type   | Nullable  |
| ----------   | -------------------------------- | ------ | --------- |
| `service` | The translator used  | str      | False      |
| `source` | The source text  | str      | False      |
| `result` | The resulting language alpha-3 code  | str      | False      |

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

> [translatepy/server/translation.py](../../translatepy/server/translation.py#L233)

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
        "sourceLang": "English",
        "destLang": "Japanese",
        "result": "こんにちは世界"
    }
}

```

#### Returns

| Field        | Description                      | Type   | Nullable  |
| ----------   | -------------------------------- | ------ | --------- |
| `service` | The translator used  | str      | False      |
| `source` | The source text  | str      | False      |
| `sourceLang` | The source language  | str      | False      |
| `destLang` | The destination language  | str      | False      |
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