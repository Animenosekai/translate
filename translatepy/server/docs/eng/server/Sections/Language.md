
# Language Section API Reference

This file lists and explains the different endpoints available in the Language section.

# __language__

This represents a non implemented endpoint

```http
* /api/language/<string:language>
```

> [../../../../endpoints/api/language.py](../../../../endpoints/api/language.py#L17)

### Authentication

Login is **not** required

### Dynamic URL

| Name         | Description                      | Required         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `language` | No description  | Yes            | str            |

### Example

<!-- tabs:start -->


<details>
    <summary>cURL Example</summary>

#### **cURL**

```bash
curl -X * "/api/language/<string:language>"
```

</details>


<details>
    <summary>JavaScript Example</summary>

#### **JavaScript**

```javascript
fetch("/api/language/<string:language>", {
    method: "*"
})
.then((response) => {response.json()})
.then((response) => {
    if (response.success) {
        console.info("Successfully requested for /api/language/<string:language>")
        console.log(response.data)
    } else {
        console.error("An error occured while requesting for /api/language/<string:language>, error: " + response.error)
    }
})
```

</details>


<details>
    <summary>Python Example</summary>

#### **Python**

```python
import requests
r = requests.request("*", "/api/language/<string:language>")
if r.status_code >= 400 or not r.json()["success"]:
    raise ValueError("An error occured while requesting for /api/language/<string:language>, error: " + r.json()["error"])
print("Successfully requested for /api/language/<string:language>")
print(r.json()["data"])
```

</details>
<!-- tabs:end -->

#### Possible Errors

| Exception         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy  | 500  |
[Return to the Index](../Getting%20Started.md#index)

# search

This represents a non implemented endpoint

```http
* /api/language/search
```

> [../../../../endpoints/api/language.py](../../../../endpoints/api/language.py#L22)

### Authentication

Login is **not** required

### Example

<!-- tabs:start -->


<details>
    <summary>cURL Example</summary>

#### **cURL**

```bash
curl -X * "/api/language/search"
```

</details>


<details>
    <summary>JavaScript Example</summary>

#### **JavaScript**

```javascript
fetch("/api/language/search", {
    method: "*"
})
.then((response) => {response.json()})
.then((response) => {
    if (response.success) {
        console.info("Successfully requested for /api/language/search")
        console.log(response.data)
    } else {
        console.error("An error occured while requesting for /api/language/search, error: " + response.error)
    }
})
```

</details>


<details>
    <summary>Python Example</summary>

#### **Python**

```python
import requests
r = requests.request("*", "/api/language/search")
if r.status_code >= 400 or not r.json()["success"]:
    raise ValueError("An error occured while requesting for /api/language/search, error: " + r.json()["error"])
print("Successfully requested for /api/language/search")
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
        "languages": "no example"
    }
}

```

#### Returns

| Field        | Description                      | Type   | Nullable  |
| ----------   | -------------------------------- | ------ | --------- |
| `languages` | The language search results  | <class 'list'>      | No      |

#### Possible Errors

| Exception         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy  | 500  |
[Return to the Index](../Getting%20Started.md#index)