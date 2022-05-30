
# Language Section API Reference

This file lists and explains the different endpoints available in the Language section.

## Language Details

Retrieving details about the given language

```http
GET /language/details
```

> [translatepy/server/language.py](../../translatepy/server/language.py#L48)

### Authentication

Login is **not** required

### Parameters

| Name         | Description                      | Required         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `lang` | The language to lookup  | True            | str            |
| `threshold` | The similarity threshold to use when searching for similar languages  | False            | float            |
| `foreign` | Whether to include the language in foreign languages  | False            | Bool            |

### Example

<!-- tabs:start -->

#### **cURL**

```bash
curl -X GET \
    --data-urlencode "lang=<The language to lookup>" \
    "/language/details"
```

#### **JavaScript**

```bash
fetch(`/language/details?lang=${encodeURIComponent("lang")}`, {
    method: "GET"
})
.then((response) => {response.json()})
.then((response) => {
    if (response.success) {
        console.info("Successfully requested for /language/details")
        console.log(response.data)
    } else {
        console.error("An error occured while requesting for /language/details, error: " + response.error)
    }
})
```

#### **Python**

```bash
import requests
r = requests.request("GET", "/language/details",
        params = {
            "lang": "The language to lookup"
        })
if r.status_code >= 400 or not r.json()["success"]:
    raise ValueError("An error occured while requesting for /language/details, error: " + r.json()["error"])
print("Successfully requested for /language/details")
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
        "id": "eng",
        "alpha2": "en",
        "alpha3b": "eng",
        "alpha3t": "eng",
        "alpha3": "eng",
        "name": "English",
        "foreign": {
            "af": "Engels",
            "sq": "Anglisht",
            "am": "እንግሊዝኛ",
            "ar": "الإنجليزية",
            "hy": "Անգլերեն",
            "...": "...",
            "zh": "英语",
            "he": "אנגלית",
            "jv": "Inggris",
            "en": "English"
        },
        "extra": {
            "type": "Living",
            "scope": null
        },
        "type": "Living",
        "scope": "Individual"
    }
}

```

#### Returns

| Field        | Description                      | Type   | Nullable  |
| ----------   | -------------------------------- | ------ | --------- |
| `id` | The language id  | str      | False      |
| `alpha2` | The language alpha2 code  | str      | False      |
| `alpha3b` | The language alpha3b code  | str      | False      |
| `alpha3t` | The language alpha3t code  | str      | False      |
| `alpha3` | The language alpha3 code  | str      | False      |
| `name` | The language name  | str      | False      |
| `foreign` | The language in foreign languages  | <class 'dict'>      | False      |
| `extra` | The language extra data  | <class 'dict'>      | False      |
| `type` | The language type  | str      | False      |
| `scope` | The language scope  | str      | False      |

#### Possible Errors

| Exception         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy. This is the base class for the other exceptions raised by translatepy.  | 500  |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
[Return to the Index](../Getting%20Started.md#index)

## Language Details (dynamic)

Retrieving details about the given language

```http
GET /language/details/<language>
```

> [translatepy/server/language.py](../../translatepy/server/language.py#L81)

### Authentication

Login is **not** required

### Parameters

| Name         | Description                      | Required         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `threshold` | The similarity threshold to use when searching for similar languages  | False            | float            |
| `foreign` | Whether to include the language in foreign languages  | False            | Bool            |

### Dynamic URL

| Name         | Description                      | Required         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `language` | The language to lookup  | True            | str            |

### Example

<!-- tabs:start -->

#### **cURL**

```bash
curl -X GET "/language/details/<language>"
```

#### **JavaScript**

```bash
fetch("/language/details/<language>", {
    method: "GET"
})
.then((response) => {response.json()})
.then((response) => {
    if (response.success) {
        console.info("Successfully requested for /language/details/<language>")
        console.log(response.data)
    } else {
        console.error("An error occured while requesting for /language/details/<language>, error: " + response.error)
    }
})
```

#### **Python**

```bash
import requests
r = requests.request("GET", "/language/details/<language>")
if r.status_code >= 400 or not r.json()["success"]:
    raise ValueError("An error occured while requesting for /language/details/<language>, error: " + r.json()["error"])
print("Successfully requested for /language/details/<language>")
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
        "id": "eng",
        "alpha2": "en",
        "alpha3b": "eng",
        "alpha3t": "eng",
        "alpha3": "eng",
        "name": "English",
        "foreign": {
            "af": "Engels",
            "sq": "Anglisht",
            "am": "እንግሊዝኛ",
            "ar": "الإنجليزية",
            "hy": "Անգլերեն",
            "...": "...",
            "zh": "英语",
            "he": "אנגלית",
            "jv": "Inggris",
            "en": "English"
        },
        "extra": {
            "type": "Living",
            "scope": null
        },
        "type": "Living",
        "scope": "Individual"
    }
}

```

#### Returns

| Field        | Description                      | Type   | Nullable  |
| ----------   | -------------------------------- | ------ | --------- |
| `id` | The language id  | str      | False      |
| `alpha2` | The language alpha2 code  | str      | False      |
| `alpha3b` | The language alpha3b code  | str      | False      |
| `alpha3t` | The language alpha3t code  | str      | False      |
| `alpha3` | The language alpha3 code  | str      | False      |
| `name` | The language name  | str      | False      |
| `foreign` | The language in foreign languages  | <class 'dict'>      | False      |
| `extra` | The language extra data  | <class 'dict'>      | False      |
| `type` | The language type  | str      | False      |
| `scope` | The language scope  | str      | False      |

#### Possible Errors

| Exception         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy. This is the base class for the other exceptions raised by translatepy.  | 500  |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
[Return to the Index](../Getting%20Started.md#index)