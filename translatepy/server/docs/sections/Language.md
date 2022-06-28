
# Language Section API Reference

This file lists and explains the different endpoints available in the Language section.

# Language Details

Retrieving details about the given language

```http
GET /language/details
```

> [translatepy/server/language.py](../../translatepy/server/language.py#L113)

### Authentication

Login is **not** required

### Parameters

| Name         | Description                      | Required         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `lang` | The language to lookup  | Yes            | str            |
| `threshold` | The similarity threshold to use when searching for similar languages  | No            | float            |
| `foreign` | Whether to include the language in foreign languages  | No            | Bool            |

### Example

<!-- tabs:start -->


<details>
    <summary>cURL Example</summary>

#### **cURL**

```bash
curl -X GET \
    --data-urlencode "lang=<The language to lookup>" \
    "/language/details"
```

</details>


<details>
    <summary>JavaScript Example</summary>

#### **JavaScript**

```javascript
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

</details>


<details>
    <summary>Python Example</summary>

#### **Python**

```python
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
        "id": "eng",
        "alpha2": "en",
        "alpha3b": "eng",
        "alpha3t": "eng",
        "alpha3": "eng",
        "name": "English",
        "inForeignLanguages": {},
        "extra": {
            "scope": "Individual",
            "type": "Living"
        }
    }
}

```

#### Returns

| Field        | Description                      | Type   | Nullable  |
| ----------   | -------------------------------- | ------ | --------- |
| `id` | The language id  | str      | No      |
| `alpha2` | The language alpha2 code  | str      | No      |
| `alpha3b` | The language alpha3b code  | str      | No      |
| `alpha3t` | The language alpha3t code  | str      | No      |
| `alpha3` | The language alpha3 code  | str      | No      |
| `name` | The language name  | str      | No      |
| `inForeignLanguages` | The language in foreign languages  | object      | No      |
| `extra` | The language extra data  | object      | No      |

#### Possible Errors

| Exception         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy. This is the base class for the other exceptions raised by translatepy.  | 500  |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
[Return to the Index](../Getting%20Started.md#index)

# Language Search

Searching for a language

```http
GET /language/search
```

> [translatepy/server/language.py](../../translatepy/server/language.py#L135)

### Authentication

Login is **not** required

### Parameters

| Name         | Description                      | Required         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `lang` | The language to lookup  | Yes            | str            |
| `limit` | The limit of languages to return. (max: 100, default: 10)  | No            | int            |
| `foreign` | Whether to include the language in foreign languages  | No            | Bool            |

### Example

<!-- tabs:start -->


<details>
    <summary>cURL Example</summary>

#### **cURL**

```bash
curl -X GET \
    --data-urlencode "lang=<The language to lookup>" \
    "/language/search"
```

</details>


<details>
    <summary>JavaScript Example</summary>

#### **JavaScript**

```javascript
fetch(`/language/search?lang=${encodeURIComponent("lang")}`, {
    method: "GET"
})
.then((response) => {response.json()})
.then((response) => {
    if (response.success) {
        console.info("Successfully requested for /language/search")
        console.log(response.data)
    } else {
        console.error("An error occured while requesting for /language/search, error: " + response.error)
    }
})
```

</details>


<details>
    <summary>Python Example</summary>

#### **Python**

```python
import requests
r = requests.request("GET", "/language/search",
        params = {
            "lang": "The language to lookup"
        })
if r.status_code >= 400 or not r.json()["success"]:
    raise ValueError("An error occured while requesting for /language/search, error: " + r.json()["error"])
print("Successfully requested for /language/search")
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
        "languages": [
            {
                "string": "English",
                "similarity": 100,
                "language": {
                    "id": "eng",
                    "similarity": 100,
                    "alpha2": "en",
                    "alpha3b": "eng",
                    "alpha3t": "eng",
                    "alpha3": "eng",
                    "name": "English",
                    "inForeignLanguages": {
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
                        "scope": "Individual"
                    }
                }
            }
        ]
    }
}

```

#### Returns

| Field        | Description                      | Type   | Nullable  |
| ----------   | -------------------------------- | ------ | --------- |
| `languages` | The languages found  | array      | No      |

#### Possible Errors

| Exception         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy. This is the base class for the other exceptions raised by translatepy.  | 500  |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
[Return to the Index](../Getting%20Started.md#index)

# Language Details (dynamic)

Retrieving details about the given language

```http
GET /language/details/<language>
```

> [translatepy/server/language.py](../../translatepy/server/language.py#L184)

### Authentication

Login is **not** required

### Parameters

| Name         | Description                      | Required         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `threshold` | The similarity threshold to use when searching for similar languages  | No            | float            |
| `foreign` | Whether to include the language in foreign languages  | No            | Bool            |

### Dynamic URL

| Name         | Description                      | Required         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `language` | The language to lookup  | Yes            | str            |

### Example

<!-- tabs:start -->


<details>
    <summary>cURL Example</summary>

#### **cURL**

```bash
curl -X GET "/language/details/<language>"
```

</details>


<details>
    <summary>JavaScript Example</summary>

#### **JavaScript**

```javascript
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

</details>


<details>
    <summary>Python Example</summary>

#### **Python**

```python
import requests
r = requests.request("GET", "/language/details/<language>")
if r.status_code >= 400 or not r.json()["success"]:
    raise ValueError("An error occured while requesting for /language/details/<language>, error: " + r.json()["error"])
print("Successfully requested for /language/details/<language>")
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
        "id": "eng",
        "alpha2": "en",
        "alpha3b": "eng",
        "alpha3t": "eng",
        "alpha3": "eng",
        "name": "English",
        "inForeignLanguages": {},
        "extra": {
            "scope": "Individual",
            "type": "Living"
        }
    }
}

```

#### Returns

| Field        | Description                      | Type   | Nullable  |
| ----------   | -------------------------------- | ------ | --------- |
| `id` | The language id  | str      | No      |
| `alpha2` | The language alpha2 code  | str      | No      |
| `alpha3b` | The language alpha3b code  | str      | No      |
| `alpha3t` | The language alpha3t code  | str      | No      |
| `alpha3` | The language alpha3 code  | str      | No      |
| `name` | The language name  | str      | No      |
| `inForeignLanguages` | The language in foreign languages  | object      | No      |
| `extra` | The language extra data  | object      | No      |

#### Possible Errors

| Exception         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy. This is the base class for the other exceptions raised by translatepy.  | 500  |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
[Return to the Index](../Getting%20Started.md#index)