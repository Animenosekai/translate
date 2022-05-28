
# Translation Section API Reference

This file lists and explains the different endpoints available in the Translation section.

## Translate



```http
GET /translate
```

> [translatepy/server/translation.py](../../translatepy/server/translation.py#L29)

### Authentication

Login is **optional**

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
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatpy. Extra information like the string similarity and the most similar string are provided in `data`.  | 500  |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatpy. Extra information like the string similarity and the most similar string are provided in `data`.  | 500  |
[Return to the Index](../Getting%20Started.md#index)