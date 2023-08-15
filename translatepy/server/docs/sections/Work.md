
# Work Section API Reference

This file lists and explains the different endpoints available in the Work section.

# translate

Translates the text in the given language

```http
GET /translate
```

> [../../endpoints/_.py](../../endpoints/_.py#L105)

### Authentication

Login is **not** required

### Parameters

| Name         | Description                      | Required         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `text` | The text to translate  | Yes            | str            |
| `translators` | A comma-separated list of translators to use  | No            | TranslatorList            |
| `source_lang` | The language `text` is in. If "auto", the translator will try to infer the language from `text`  | No            | Language            |
| `dest_lang` | The language to translate to  | Yes            | Language            |

### Example

<!-- tabs:start -->


<details>
    <summary>cURL Example</summary>

#### **cURL**

```bash
curl -X GET \
    --data-urlencode "text=<The text to translate>"\
    --data-urlencode "translators=<A comma-separated list of translators to use>"\
    --data-urlencode "source_lang=<The language `text` is in. If \"auto\", the translator will try to infer the language from `text`>"\
    --data-urlencode "dest_lang=<The language to translate to>" \
    "/translate"
```

</details>


<details>
    <summary>JavaScript Example</summary>

#### **JavaScript**

```javascript
fetch(`/translate?text=${encodeURIComponent("text")}&dest_lang=${encodeURIComponent("dest_lang")}`, {
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

</details>


<details>
    <summary>Python Example</summary>

#### **Python**

```python
import requests
r = requests.request("GET", "/translate",
        params = {
            "text": "The text to translate",
            "dest_lang": "The language to translate to"
        })
if r.status_code >= 400 or not r.json()["success"]:
    raise ValueError("An error occured while requesting for /translate, error: " + r.json()["error"])
print("Successfully requested for /translate")
print(r.json()["data"])
```

</details>
<!-- tabs:end -->

### Response

#### Example response

```json
{
    "success": true,
    "message": "Successfully processed your request",
    "error": null,
    "data": {
        "dest_lang": "no example",
        "source_lang": "no example",
        "translation": "no example",
        "source": "no example",
        "service": "no example"
    }
}

```

#### Returns

| Field        | Description                      | Type   | Nullable  |
| ----------   | -------------------------------- | ------ | --------- |
| `dest_lang` | The result's language  | Language      | No      |
| `source_lang` | The source text's language  | Language      | No      |
| `translation` | The translation result  | string      | No      |
| `source` | The source text  | string      | No      |
| `service` | The service which returned the result  | Translator      | No      |

#### Possible Errors

| Exception         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy  | 500  |
[Return to the Index](../Getting%20Started.md#index)

# transliterate

Transliterates the text in the given language

```http
GET /transliterate
```

> [../../endpoints/_.py](../../endpoints/_.py#L117)

### Authentication

Login is **not** required

### Parameters

| Name         | Description                      | Required         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `translators` | A comma-separated list of translators to use  | No            | TranslatorList            |
| `dest_lang` | The language to translate to  | Yes            | Language            |
| `source_lang` | The language `text` is in. If "auto", the translator will try to infer the language from `text`  | No            | Language            |
| `text` | The text to transliterate  | Yes            | str            |

### Example

<!-- tabs:start -->


<details>
    <summary>cURL Example</summary>

#### **cURL**

```bash
curl -X GET \
    --data-urlencode "translators=<A comma-separated list of translators to use>"\
    --data-urlencode "dest_lang=<The language to translate to>"\
    --data-urlencode "source_lang=<The language `text` is in. If \"auto\", the translator will try to infer the language from `text`>"\
    --data-urlencode "text=<The text to transliterate>" \
    "/transliterate"
```

</details>


<details>
    <summary>JavaScript Example</summary>

#### **JavaScript**

```javascript
fetch(`/transliterate?dest_lang=${encodeURIComponent("dest_lang")}&text=${encodeURIComponent("text")}`, {
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

</details>


<details>
    <summary>Python Example</summary>

#### **Python**

```python
import requests
r = requests.request("GET", "/transliterate",
        params = {
            "dest_lang": "The language to translate to",
            "text": "The text to transliterate"
        })
if r.status_code >= 400 or not r.json()["success"]:
    raise ValueError("An error occured while requesting for /transliterate, error: " + r.json()["error"])
print("Successfully requested for /transliterate")
print(r.json()["data"])
```

</details>
<!-- tabs:end -->

### Response

#### Example response

```json
{
    "success": true,
    "message": "Successfully processed your request",
    "error": null,
    "data": {
        "dest_lang": "no example",
        "source_lang": "no example",
        "source": "no example",
        "service": "no example",
        "transliteration": "no example"
    }
}

```

#### Returns

| Field        | Description                      | Type   | Nullable  |
| ----------   | -------------------------------- | ------ | --------- |
| `dest_lang` | The result's language  | Language      | No      |
| `source_lang` | The source text's language  | Language      | No      |
| `source` | The source text  | string      | No      |
| `service` | The service which returned the result  | Translator      | No      |
| `transliteration` | The transliteration result  | string      | No      |

#### Possible Errors

| Exception         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy  | 500  |
[Return to the Index](../Getting%20Started.md#index)

# spellcheck

Spellchecks the given text

```http
GET /spellcheck
```

> [../../endpoints/_.py](../../endpoints/_.py#L125)

### Authentication

Login is **not** required

### Parameters

| Name         | Description                      | Required         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `translators` | A comma-separated list of translators to use  | No            | TranslatorList            |
| `text` | The text to check for spelling mistakes  | Yes            | str            |
| `source_lang` | The language `text` is in. If "auto", the translator will try to infer the language from `text`  | No            | Language            |

### Example

<!-- tabs:start -->


<details>
    <summary>cURL Example</summary>

#### **cURL**

```bash
curl -X GET \
    --data-urlencode "translators=<A comma-separated list of translators to use>"\
    --data-urlencode "text=<The text to check for spelling mistakes>"\
    --data-urlencode "source_lang=<The language `text` is in. If \"auto\", the translator will try to infer the language from `text`>" \
    "/spellcheck"
```

</details>


<details>
    <summary>JavaScript Example</summary>

#### **JavaScript**

```javascript
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

</details>


<details>
    <summary>Python Example</summary>

#### **Python**

```python
import requests
r = requests.request("GET", "/spellcheck",
        params = {
            "text": "The text to check for spelling mistakes"
        })
if r.status_code >= 400 or not r.json()["success"]:
    raise ValueError("An error occured while requesting for /spellcheck, error: " + r.json()["error"])
print("Successfully requested for /spellcheck")
print(r.json()["data"])
```

</details>
<!-- tabs:end -->

### Response

#### Example response

```json
{
    "success": true,
    "message": "Successfully processed your request",
    "error": null,
    "data": {
        "source": "no example",
        "service": "no example",
        "source_lang": "no example",
        "corrected": "no example"
    }
}

```

#### Returns

| Field        | Description                      | Type   | Nullable  |
| ----------   | -------------------------------- | ------ | --------- |
| `source` | The source text  | string      | No      |
| `service` | The service which returned the result  | Translator      | No      |
| `source_lang` | The source text's language  | Language      | No      |
| `corrected` | The corrected text  | string      | No      |

#### Possible Errors

| Exception         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy  | 500  |
[Return to the Index](../Getting%20Started.md#index)

# language

Retrieves the language of the given text

```http
GET /language
```

> [../../endpoints/_.py](../../endpoints/_.py#L133)

### Authentication

Login is **not** required

### Parameters

| Name         | Description                      | Required         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `source_lang` | No description  | No            | Language            |
| `translators` | A comma-separated list of translators to use  | No            | TranslatorList            |
| `text` | The text to get the language for  | Yes            | str            |

### Example

<!-- tabs:start -->


<details>
    <summary>cURL Example</summary>

#### **cURL**

```bash
curl -X GET \
    --data-urlencode "source_lang=<>"\
    --data-urlencode "translators=<A comma-separated list of translators to use>"\
    --data-urlencode "text=<The text to get the language for>" \
    "/language"
```

</details>


<details>
    <summary>JavaScript Example</summary>

#### **JavaScript**

```javascript
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

</details>


<details>
    <summary>Python Example</summary>

#### **Python**

```python
import requests
r = requests.request("GET", "/language",
        params = {
            "text": "The text to get the language for"
        })
if r.status_code >= 400 or not r.json()["success"]:
    raise ValueError("An error occured while requesting for /language, error: " + r.json()["error"])
print("Successfully requested for /language")
print(r.json()["data"])
```

</details>
<!-- tabs:end -->

### Response

#### Example response

```json
{
    "success": true,
    "message": "Successfully processed your request",
    "error": null,
    "data": {
        "source": "no example",
        "service": "no example",
        "language": "no example"
    }
}

```

#### Returns

| Field        | Description                      | Type   | Nullable  |
| ----------   | -------------------------------- | ------ | --------- |
| `source` | The source text  | string      | No      |
| `service` | The service which returned the result  | Translator      | No      |
| `language` | The detected language  | Language      | No      |

#### Possible Errors

| Exception         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy  | 500  |
[Return to the Index](../Getting%20Started.md#index)

# example

Finds examples for the given text

```http
GET /example
```

> [../../endpoints/_.py](../../endpoints/_.py#L141)

### Authentication

Login is **not** required

### Parameters

| Name         | Description                      | Required         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `text` | The text to get the example for  | Yes            | str            |
| `translators` | A comma-separated list of translators to use  | No            | TranslatorList            |
| `source_lang` | The language `text` is in. If "auto", the translator will try to infer the language from `text`  | No            | Language            |

### Example

<!-- tabs:start -->


<details>
    <summary>cURL Example</summary>

#### **cURL**

```bash
curl -X GET \
    --data-urlencode "text=<The text to get the example for>"\
    --data-urlencode "translators=<A comma-separated list of translators to use>"\
    --data-urlencode "source_lang=<The language `text` is in. If \"auto\", the translator will try to infer the language from `text`>" \
    "/example"
```

</details>


<details>
    <summary>JavaScript Example</summary>

#### **JavaScript**

```javascript
fetch(`/example?text=${encodeURIComponent("text")}`, {
    method: "GET"
})
.then((response) => {response.json()})
.then((response) => {
    if (response.success) {
        console.info("Successfully requested for /example")
        console.log(response.data)
    } else {
        console.error("An error occured while requesting for /example, error: " + response.error)
    }
})
```

</details>


<details>
    <summary>Python Example</summary>

#### **Python**

```python
import requests
r = requests.request("GET", "/example",
        params = {
            "text": "The text to get the example for"
        })
if r.status_code >= 400 or not r.json()["success"]:
    raise ValueError("An error occured while requesting for /example, error: " + r.json()["error"])
print("Successfully requested for /example")
print(r.json()["data"])
```

</details>
<!-- tabs:end -->

### Response

#### Example response

```json
{
    "success": true,
    "message": "Successfully processed your request",
    "error": null,
    "data": {
        "example": "no example",
        "source_lang": "no example",
        "reference": "no example",
        "source": "no example",
        "service": "no example"
    }
}

```

#### Returns

| Field        | Description                      | Type   | Nullable  |
| ----------   | -------------------------------- | ------ | --------- |
| `example` | The example  | string      | No      |
| `source_lang` | The source text's language  | Language      | No      |
| `reference` | Where the example comes from (i.e a book or a the person who said it if it's a quote)  | string      | No      |
| `source` | The source text  | string      | No      |
| `service` | The service which returned the result  | Translator      | No      |

#### Possible Errors

| Exception         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy  | 500  |
[Return to the Index](../Getting%20Started.md#index)

# dictionary

Retrieves meanings for the given text

```http
GET /dictionary
```

> [../../endpoints/_.py](../../endpoints/_.py#L149)

### Authentication

Login is **not** required

### Parameters

| Name         | Description                      | Required         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `translators` | A comma-separated list of translators to use  | No            | TranslatorList            |
| `text` | The text to get the meaning for  | Yes            | str            |
| `source_lang` | The language `text` is in. If "auto", the translator will try to infer the language from `text`  | No            | Language            |

### Example

<!-- tabs:start -->


<details>
    <summary>cURL Example</summary>

#### **cURL**

```bash
curl -X GET \
    --data-urlencode "translators=<A comma-separated list of translators to use>"\
    --data-urlencode "text=<The text to get the meaning for>"\
    --data-urlencode "source_lang=<The language `text` is in. If \"auto\", the translator will try to infer the language from `text`>" \
    "/dictionary"
```

</details>


<details>
    <summary>JavaScript Example</summary>

#### **JavaScript**

```javascript
fetch(`/dictionary?text=${encodeURIComponent("text")}`, {
    method: "GET"
})
.then((response) => {response.json()})
.then((response) => {
    if (response.success) {
        console.info("Successfully requested for /dictionary")
        console.log(response.data)
    } else {
        console.error("An error occured while requesting for /dictionary, error: " + response.error)
    }
})
```

</details>


<details>
    <summary>Python Example</summary>

#### **Python**

```python
import requests
r = requests.request("GET", "/dictionary",
        params = {
            "text": "The text to get the meaning for"
        })
if r.status_code >= 400 or not r.json()["success"]:
    raise ValueError("An error occured while requesting for /dictionary, error: " + r.json()["error"])
print("Successfully requested for /dictionary")
print(r.json()["data"])
```

</details>
<!-- tabs:end -->

### Response

#### Example response

```json
{
    "success": true,
    "message": "Successfully processed your request",
    "error": null,
    "data": {
        "source": "no example",
        "service": "no example",
        "source_lang": "no example",
        "meaning": "no example"
    }
}

```

#### Returns

| Field        | Description                      | Type   | Nullable  |
| ----------   | -------------------------------- | ------ | --------- |
| `source` | The source text  | string      | No      |
| `service` | The service which returned the result  | Translator      | No      |
| `source_lang` | The source text's language  | Language      | No      |
| `meaning` | The meaning of the text  | string      | No      |

#### Possible Errors

| Exception         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy  | 500  |
[Return to the Index](../Getting%20Started.md#index)

# tts

Returns the speech version of the given text

```http
GET /tts
```

> [../../endpoints/_.py](../../endpoints/_.py#L157)

### Authentication

Login is **not** required

### Parameters

| Name         | Description                      | Required         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `text` | The text to get the speech for  | Yes            | str            |
| `translators` | A comma-separated list of translators to use  | No            | TranslatorList            |
| `raw` | No description  | No            | to_bool            |
| `source_lang` | The language `text` is in. If "auto", the translator will try to infer the language from `text`  | No            | Language            |

### Example

<!-- tabs:start -->


<details>
    <summary>cURL Example</summary>

#### **cURL**

```bash
curl -X GET \
    --data-urlencode "text=<The text to get the speech for>"\
    --data-urlencode "translators=<A comma-separated list of translators to use>"\
    --data-urlencode "raw=<>"\
    --data-urlencode "source_lang=<The language `text` is in. If \"auto\", the translator will try to infer the language from `text`>" \
    "/tts"
```

</details>


<details>
    <summary>JavaScript Example</summary>

#### **JavaScript**

```javascript
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

</details>


<details>
    <summary>Python Example</summary>

#### **Python**

```python
import requests
r = requests.request("GET", "/tts",
        params = {
            "text": "The text to get the speech for"
        })
if r.status_code >= 400 or not r.json()["success"]:
    raise ValueError("An error occured while requesting for /tts, error: " + r.json()["error"])
print("Successfully requested for /tts")
print(r.json()["data"])
```

</details>
<!-- tabs:end -->

### Response

#### Example response

```json
{
    "success": true,
    "message": "Successfully processed your request",
    "error": null,
    "data": {
        "result": "no example",
        "source_lang": "no example",
        "speed": 4,
        "source": "no example",
        "service": "no example",
        "gender": "no example"
    }
}

```

#### Returns

| Field        | Description                      | Type   | Nullable  |
| ----------   | -------------------------------- | ------ | --------- |
| `result` | Text to speech result  | bytes      | No      |
| `source_lang` | The source text's language  | Language      | No      |
| `speed` | Speed of the text to speech result  | int      | No      |
| `source` | The source text  | string      | No      |
| `service` | The service which returned the result  | Translator      | No      |
| `gender` | Gender of the 'person' saying the text  | Gender      | No      |

#### Possible Errors

| Exception         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy  | 500  |
[Return to the Index](../Getting%20Started.md#index)