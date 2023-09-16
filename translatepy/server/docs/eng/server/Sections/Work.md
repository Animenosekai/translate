
# Work Section API Reference

This file lists and explains the different endpoints available in the Work section.

# translate

Translates the text in the given language

```http
GET /api/translate
```

> [../../../../translatepy/server/endpoints/api/_.py](../../../../translatepy/server/endpoints/api/_.py#L113)

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
    "/api/translate"
```

</details>


<details>
    <summary>JavaScript Example</summary>

#### **JavaScript**

```javascript
fetch(`/api/translate?text=${encodeURIComponent("text")}&dest_lang=${encodeURIComponent("dest_lang")}`, {
    method: "GET"
})
.then((response) => {response.json()})
.then((response) => {
    if (response.success) {
        console.info("Successfully requested for /api/translate")
        console.log(response.data)
    } else {
        console.error("An error occured while requesting for /api/translate, error: " + response.error)
    }
})
```

</details>


<details>
    <summary>Python Example</summary>

#### **Python**

```python
import requests
r = requests.request("GET", "/api/translate",
        params = {
            "text": "The text to translate",
            "dest_lang": "The language to translate to"
        })
if r.status_code >= 400 or not r.json()["success"]:
    raise ValueError("An error occured while requesting for /api/translate, error: " + r.json()["error"])
print("Successfully requested for /api/translate")
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
        "translation": "no example",
        "source_lang": "no example",
        "dest_lang": "no example"
    }
}

```

#### Returns

| Field        | Description                      | Type   | Nullable  |
| ----------   | -------------------------------- | ------ | --------- |
| `source` | The source text  | string      | No      |
| `service` | The service which returned the result  | Translator      | No      |
| `translation` | The translation result  | string      | No      |
| `source_lang` | The source text's language  | Language      | No      |
| `dest_lang` | The result's language  | Language      | No      |

#### Possible Errors

| Exception         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy  | 500  |
[Return to the Index](../Getting%20Started.md#index)

# translate_html

Translates the HTML in the given language

```http
GET /api/translate/html
```

> [../../../../translatepy/server/endpoints/api/_.py](../../../../translatepy/server/endpoints/api/_.py#L121)

### Authentication

Login is **not** required

### Parameters

| Name         | Description                      | Required         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `parser` | The BeautifulSoup parser to use to parse the HTML  | No            | str            |
| `source_lang` | The language `text` is in. If "auto", the translator will try to infer the language from each node in `html`  | No            | Language            |
| `html` | The HTML you want to translate  | Yes            | str            |
| `strict` | If the function should raise something is one of the nodes couldn't be translated.
If `False`, the node will be left as is and the `result` part will be `None`  | No            | to_bool            |
| `dest_lang` | The language to translate to  | Yes            | Language            |
| `threads_limit` | The maximum number of threads to spawn at a time to translate  | No            | int            |
| `translators` | A comma-separated list of translators to use  | No            | TranslatorList            |

### Example

<!-- tabs:start -->


<details>
    <summary>cURL Example</summary>

#### **cURL**

```bash
curl -X GET \
    --data-urlencode "parser=<The BeautifulSoup parser to use to parse the HTML>"\
    --data-urlencode "source_lang=<The language `text` is in. If \"auto\", the translator will try to infer the language from each node in `html`>"\
    --data-urlencode "html=<The HTML you want to translate>"\
    --data-urlencode "strict=<If the function should raise something is one of the nodes couldn't be translated.
If `False`, the node will be left as is and the `result` part will be `None`>"\
    --data-urlencode "dest_lang=<The language to translate to>"\
    --data-urlencode "threads_limit=<The maximum number of threads to spawn at a time to translate>"\
    --data-urlencode "translators=<A comma-separated list of translators to use>" \
    "/api/translate/html"
```

</details>


<details>
    <summary>JavaScript Example</summary>

#### **JavaScript**

```javascript
fetch(`/api/translate/html?html=${encodeURIComponent("html")}&dest_lang=${encodeURIComponent("dest_lang")}`, {
    method: "GET"
})
.then((response) => {response.json()})
.then((response) => {
    if (response.success) {
        console.info("Successfully requested for /api/translate/html")
        console.log(response.data)
    } else {
        console.error("An error occured while requesting for /api/translate/html, error: " + response.error)
    }
})
```

</details>


<details>
    <summary>Python Example</summary>

#### **Python**

```python
import requests
r = requests.request("GET", "/api/translate/html",
        params = {
            "html": "The HTML you want to translate",
            "dest_lang": "The language to translate to"
        })
if r.status_code >= 400 or not r.json()["success"]:
    raise ValueError("An error occured while requesting for /api/translate/html, error: " + r.json()["error"])
print("Successfully requested for /api/translate/html")
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
        "service": "no example",
        "source_lang": "no example",
        "source": "no example"
    }
}

```

#### Returns

| Field        | Description                      | Type   | Nullable  |
| ----------   | -------------------------------- | ------ | --------- |
| `service` | The service which returned the result  | Translator      | No      |
| `source_lang` | The source text's language  | Language      | No      |
| `source` | The source text  | string      | No      |

#### Possible Errors

| Exception         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy  | 500  |
[Return to the Index](../Getting%20Started.md#index)

# stream

Streams all translations available using the different translators

```http
* /api/stream
```

> [../../../../translatepy/server/endpoints/api/_.py](../../../../translatepy/server/endpoints/api/_.py#L133)

### Authentication

Login is **not** required

### Parameters

| Name         | Description                      | Required         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `source_lang` | No description  | No            | Language            |
| `dest_lang` | No description  | Yes            | Language            |
| `translators` | No description  | No            | TranslatorList            |
| `text` | No description  | Yes            | str            |
| `timeout` | No description  | No            | int            |

### Example

<!-- tabs:start -->


<details>
    <summary>cURL Example</summary>

#### **cURL**

```bash
curl -X * \
    --data-urlencode "source_lang=<>"\
    --data-urlencode "dest_lang=<>"\
    --data-urlencode "translators=<>"\
    --data-urlencode "text=<>"\
    --data-urlencode "timeout=<>" \
    "/api/stream"
```

</details>


<details>
    <summary>JavaScript Example</summary>

#### **JavaScript**

```javascript
fetch(`/api/stream?dest_lang=${encodeURIComponent("dest_lang")}&text=${encodeURIComponent("text")}`, {
    method: "*"
})
.then((response) => {response.json()})
.then((response) => {
    if (response.success) {
        console.info("Successfully requested for /api/stream")
        console.log(response.data)
    } else {
        console.error("An error occured while requesting for /api/stream, error: " + response.error)
    }
})
```

</details>


<details>
    <summary>Python Example</summary>

#### **Python**

```python
import requests
r = requests.request("*", "/api/stream",
        params = {
            "dest_lang": "dest_lang",
            "text": "text"
        })
if r.status_code >= 400 or not r.json()["success"]:
    raise ValueError("An error occured while requesting for /api/stream, error: " + r.json()["error"])
print("Successfully requested for /api/stream")
print(r.json()["data"])
```

</details>
<!-- tabs:end -->

#### Possible Errors

| Exception         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy  | 500  |
[Return to the Index](../Getting%20Started.md#index)

# transliterate

Transliterates the text in the given language

```http
GET /api/transliterate
```

> [../../../../translatepy/server/endpoints/api/_.py](../../../../translatepy/server/endpoints/api/_.py#L186)

### Authentication

Login is **not** required

### Parameters

| Name         | Description                      | Required         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `dest_lang` | The language to translate to  | Yes            | Language            |
| `translators` | A comma-separated list of translators to use  | No            | TranslatorList            |
| `text` | The text to transliterate  | Yes            | str            |
| `source_lang` | The language `text` is in. If "auto", the translator will try to infer the language from `text`  | No            | Language            |

### Example

<!-- tabs:start -->


<details>
    <summary>cURL Example</summary>

#### **cURL**

```bash
curl -X GET \
    --data-urlencode "dest_lang=<The language to translate to>"\
    --data-urlencode "translators=<A comma-separated list of translators to use>"\
    --data-urlencode "text=<The text to transliterate>"\
    --data-urlencode "source_lang=<The language `text` is in. If \"auto\", the translator will try to infer the language from `text`>" \
    "/api/transliterate"
```

</details>


<details>
    <summary>JavaScript Example</summary>

#### **JavaScript**

```javascript
fetch(`/api/transliterate?dest_lang=${encodeURIComponent("dest_lang")}&text=${encodeURIComponent("text")}`, {
    method: "GET"
})
.then((response) => {response.json()})
.then((response) => {
    if (response.success) {
        console.info("Successfully requested for /api/transliterate")
        console.log(response.data)
    } else {
        console.error("An error occured while requesting for /api/transliterate, error: " + response.error)
    }
})
```

</details>


<details>
    <summary>Python Example</summary>

#### **Python**

```python
import requests
r = requests.request("GET", "/api/transliterate",
        params = {
            "dest_lang": "The language to translate to",
            "text": "The text to transliterate"
        })
if r.status_code >= 400 or not r.json()["success"]:
    raise ValueError("An error occured while requesting for /api/transliterate, error: " + r.json()["error"])
print("Successfully requested for /api/transliterate")
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
        "transliteration": "no example",
        "source_lang": "no example",
        "dest_lang": "no example"
    }
}

```

#### Returns

| Field        | Description                      | Type   | Nullable  |
| ----------   | -------------------------------- | ------ | --------- |
| `source` | The source text  | string      | No      |
| `service` | The service which returned the result  | Translator      | No      |
| `transliteration` | The transliteration result  | string      | No      |
| `source_lang` | The source text's language  | Language      | No      |
| `dest_lang` | The result's language  | Language      | No      |

#### Possible Errors

| Exception         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy  | 500  |
[Return to the Index](../Getting%20Started.md#index)

# spellcheck

Spellchecks the given text

```http
GET /api/spellcheck
```

> [../../../../translatepy/server/endpoints/api/_.py](../../../../translatepy/server/endpoints/api/_.py#L194)

### Authentication

Login is **not** required

### Parameters

| Name         | Description                      | Required         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `text` | The text to check for spelling mistakes  | Yes            | str            |
| `translators` | A comma-separated list of translators to use  | No            | TranslatorList            |
| `source_lang` | The language `text` is in. If "auto", the translator will try to infer the language from `text`  | No            | Language            |

### Example

<!-- tabs:start -->


<details>
    <summary>cURL Example</summary>

#### **cURL**

```bash
curl -X GET \
    --data-urlencode "text=<The text to check for spelling mistakes>"\
    --data-urlencode "translators=<A comma-separated list of translators to use>"\
    --data-urlencode "source_lang=<The language `text` is in. If \"auto\", the translator will try to infer the language from `text`>" \
    "/api/spellcheck"
```

</details>


<details>
    <summary>JavaScript Example</summary>

#### **JavaScript**

```javascript
fetch(`/api/spellcheck?text=${encodeURIComponent("text")}`, {
    method: "GET"
})
.then((response) => {response.json()})
.then((response) => {
    if (response.success) {
        console.info("Successfully requested for /api/spellcheck")
        console.log(response.data)
    } else {
        console.error("An error occured while requesting for /api/spellcheck, error: " + response.error)
    }
})
```

</details>


<details>
    <summary>Python Example</summary>

#### **Python**

```python
import requests
r = requests.request("GET", "/api/spellcheck",
        params = {
            "text": "The text to check for spelling mistakes"
        })
if r.status_code >= 400 or not r.json()["success"]:
    raise ValueError("An error occured while requesting for /api/spellcheck, error: " + r.json()["error"])
print("Successfully requested for /api/spellcheck")
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
        "rich": true,
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
| `rich` | Whether the given result features the full range of information  | bool      | No      |
| `source_lang` | The source text's language  | Language      | No      |
| `corrected` | The corrected text  | string      | No      |

#### Possible Errors

| Exception         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy  | 500  |
[Return to the Index](../Getting%20Started.md#index)

# language

Retrieves the language of the given text

```http
GET /api/language
```

> [../../../../translatepy/server/endpoints/api/_.py](../../../../translatepy/server/endpoints/api/_.py#L202)

### Authentication

Login is **not** required

### Parameters

| Name         | Description                      | Required         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `text` | The text to get the language for  | Yes            | str            |
| `translators` | A comma-separated list of translators to use  | No            | TranslatorList            |
| `source_lang` | No description  | No            | Language            |

### Example

<!-- tabs:start -->


<details>
    <summary>cURL Example</summary>

#### **cURL**

```bash
curl -X GET \
    --data-urlencode "text=<The text to get the language for>"\
    --data-urlencode "translators=<A comma-separated list of translators to use>"\
    --data-urlencode "source_lang=<>" \
    "/api/language"
```

</details>


<details>
    <summary>JavaScript Example</summary>

#### **JavaScript**

```javascript
fetch(`/api/language?text=${encodeURIComponent("text")}`, {
    method: "GET"
})
.then((response) => {response.json()})
.then((response) => {
    if (response.success) {
        console.info("Successfully requested for /api/language")
        console.log(response.data)
    } else {
        console.error("An error occured while requesting for /api/language, error: " + response.error)
    }
})
```

</details>


<details>
    <summary>Python Example</summary>

#### **Python**

```python
import requests
r = requests.request("GET", "/api/language",
        params = {
            "text": "The text to get the language for"
        })
if r.status_code >= 400 or not r.json()["success"]:
    raise ValueError("An error occured while requesting for /api/language, error: " + r.json()["error"])
print("Successfully requested for /api/language")
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
        "service": "no example",
        "source_lang": "no example",
        "source": "no example"
    }
}

```

#### Returns

| Field        | Description                      | Type   | Nullable  |
| ----------   | -------------------------------- | ------ | --------- |
| `service` | The service which returned the result  | Translator      | No      |
| `source_lang` | The source text's language  | Language      | No      |
| `source` | The source text  | string      | No      |

#### Possible Errors

| Exception         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy  | 500  |
[Return to the Index](../Getting%20Started.md#index)

# example

Finds examples for the given text

```http
GET /api/example
```

> [../../../../translatepy/server/endpoints/api/_.py](../../../../translatepy/server/endpoints/api/_.py#L210)

### Authentication

Login is **not** required

### Parameters

| Name         | Description                      | Required         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `translators` | A comma-separated list of translators to use  | No            | TranslatorList            |
| `source_lang` | The language `text` is in. If "auto", the translator will try to infer the language from `text`  | No            | Language            |
| `text` | The text to get the example for  | Yes            | str            |

### Example

<!-- tabs:start -->


<details>
    <summary>cURL Example</summary>

#### **cURL**

```bash
curl -X GET \
    --data-urlencode "translators=<A comma-separated list of translators to use>"\
    --data-urlencode "source_lang=<The language `text` is in. If \"auto\", the translator will try to infer the language from `text`>"\
    --data-urlencode "text=<The text to get the example for>" \
    "/api/example"
```

</details>


<details>
    <summary>JavaScript Example</summary>

#### **JavaScript**

```javascript
fetch(`/api/example?text=${encodeURIComponent("text")}`, {
    method: "GET"
})
.then((response) => {response.json()})
.then((response) => {
    if (response.success) {
        console.info("Successfully requested for /api/example")
        console.log(response.data)
    } else {
        console.error("An error occured while requesting for /api/example, error: " + response.error)
    }
})
```

</details>


<details>
    <summary>Python Example</summary>

#### **Python**

```python
import requests
r = requests.request("GET", "/api/example",
        params = {
            "text": "The text to get the example for"
        })
if r.status_code >= 400 or not r.json()["success"]:
    raise ValueError("An error occured while requesting for /api/example, error: " + r.json()["error"])
print("Successfully requested for /api/example")
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
        "reference": "no example",
        "service": "no example",
        "example": "no example",
        "positions": "no example",
        "source_lang": "no example",
        "source": "no example"
    }
}

```

#### Returns

| Field        | Description                      | Type   | Nullable  |
| ----------   | -------------------------------- | ------ | --------- |
| `reference` | Where the example comes from (i.e a book or a the person who said it if it's a quote)  | string      | No      |
| `service` | The service which returned the result  | Translator      | No      |
| `example` | The example  | string      | No      |
| `positions` | The positions of the word in the example  | list[int]      | No      |
| `source_lang` | The source text's language  | Language      | No      |
| `source` | The source text  | string      | No      |

#### Possible Errors

| Exception         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy  | 500  |
[Return to the Index](../Getting%20Started.md#index)

# dictionary

Retrieves meanings for the given text

```http
GET /api/dictionary
```

> [../../../../translatepy/server/endpoints/api/_.py](../../../../translatepy/server/endpoints/api/_.py#L218)

### Authentication

Login is **not** required

### Parameters

| Name         | Description                      | Required         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `translators` | A comma-separated list of translators to use  | No            | TranslatorList            |
| `source_lang` | The language `text` is in. If "auto", the translator will try to infer the language from `text`  | No            | Language            |
| `text` | The text to get the meaning for  | Yes            | str            |

### Example

<!-- tabs:start -->


<details>
    <summary>cURL Example</summary>

#### **cURL**

```bash
curl -X GET \
    --data-urlencode "translators=<A comma-separated list of translators to use>"\
    --data-urlencode "source_lang=<The language `text` is in. If \"auto\", the translator will try to infer the language from `text`>"\
    --data-urlencode "text=<The text to get the meaning for>" \
    "/api/dictionary"
```

</details>


<details>
    <summary>JavaScript Example</summary>

#### **JavaScript**

```javascript
fetch(`/api/dictionary?text=${encodeURIComponent("text")}`, {
    method: "GET"
})
.then((response) => {response.json()})
.then((response) => {
    if (response.success) {
        console.info("Successfully requested for /api/dictionary")
        console.log(response.data)
    } else {
        console.error("An error occured while requesting for /api/dictionary, error: " + response.error)
    }
})
```

</details>


<details>
    <summary>Python Example</summary>

#### **Python**

```python
import requests
r = requests.request("GET", "/api/dictionary",
        params = {
            "text": "The text to get the meaning for"
        })
if r.status_code >= 400 or not r.json()["success"]:
    raise ValueError("An error occured while requesting for /api/dictionary, error: " + r.json()["error"])
print("Successfully requested for /api/dictionary")
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
        "service": "no example",
        "rich": true,
        "source_lang": "no example",
        "source": "no example",
        "meaning": "no example"
    }
}

```

#### Returns

| Field        | Description                      | Type   | Nullable  |
| ----------   | -------------------------------- | ------ | --------- |
| `service` | The service which returned the result  | Translator      | No      |
| `rich` | Whether the given result features the full range of information  | bool      | No      |
| `source_lang` | The source text's language  | Language      | No      |
| `source` | The source text  | string      | No      |
| `meaning` | The meaning of the text  | string      | No      |

#### Possible Errors

| Exception         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy  | 500  |
[Return to the Index](../Getting%20Started.md#index)

# tts

Returns the speech version of the given text

```http
GET /api/tts
```

> [../../../../translatepy/server/endpoints/api/_.py](../../../../translatepy/server/endpoints/api/_.py#L226)

### Authentication

Login is **not** required

### Parameters

| Name         | Description                      | Required         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `text` | The text to get the speech for  | Yes            | str            |
| `raw` | No description  | No            | to_bool            |
| `translators` | A comma-separated list of translators to use  | No            | TranslatorList            |
| `source_lang` | The language `text` is in. If "auto", the translator will try to infer the language from `text`  | No            | Language            |

### Example

<!-- tabs:start -->


<details>
    <summary>cURL Example</summary>

#### **cURL**

```bash
curl -X GET \
    --data-urlencode "text=<The text to get the speech for>"\
    --data-urlencode "raw=<>"\
    --data-urlencode "translators=<A comma-separated list of translators to use>"\
    --data-urlencode "source_lang=<The language `text` is in. If \"auto\", the translator will try to infer the language from `text`>" \
    "/api/tts"
```

</details>


<details>
    <summary>JavaScript Example</summary>

#### **JavaScript**

```javascript
fetch(`/api/tts?text=${encodeURIComponent("text")}`, {
    method: "GET"
})
.then((response) => {response.json()})
.then((response) => {
    if (response.success) {
        console.info("Successfully requested for /api/tts")
        console.log(response.data)
    } else {
        console.error("An error occured while requesting for /api/tts, error: " + response.error)
    }
})
```

</details>


<details>
    <summary>Python Example</summary>

#### **Python**

```python
import requests
r = requests.request("GET", "/api/tts",
        params = {
            "text": "The text to get the speech for"
        })
if r.status_code >= 400 or not r.json()["success"]:
    raise ValueError("An error occured while requesting for /api/tts, error: " + r.json()["error"])
print("Successfully requested for /api/tts")
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
        "service": "no example",
        "result": "no example",
        "gender": "no example",
        "speed": 4,
        "extension": "no example",
        "mime_type": "no example",
        "source_lang": "no example",
        "source": "no example"
    }
}

```

#### Returns

| Field        | Description                      | Type   | Nullable  |
| ----------   | -------------------------------- | ------ | --------- |
| `service` | The service which returned the result  | Translator      | No      |
| `result` | Text to speech result  | bytes      | No      |
| `gender` | Gender of the 'person' saying the text  | Gender      | No      |
| `speed` | Speed of the text to speech result  | int      | No      |
| `extension` | Returns the audio file extension  | Optional[str]      | No      |
| `mime_type` | Returns the MIME type of the audio file  | Optional[str]      | No      |
| `source_lang` | The source text's language  | Language      | No      |
| `source` | The source text  | string      | No      |

#### Possible Errors

| Exception         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy  | 500  |
[Return to the Index](../Getting%20Started.md#index)