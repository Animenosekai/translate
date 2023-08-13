
# Stars Section API Reference

This file lists and explains the different endpoints available in the Stars section.

# Stars

Get all starred translations

```http
GET /stars
```

> [server/endpoints/stars.py](../../server/endpoints/stars.py#L49)

### Authentication

Login is **not** required

### Example

<!-- tabs:start -->


<details>
    <summary>cURL Example</summary>

#### **cURL**

```bash
curl -X GET "/stars"
```

</details>


<details>
    <summary>JavaScript Example</summary>

#### **JavaScript**

```javascript
fetch("/stars", {
    method: "GET"
})
.then((response) => {response.json()})
.then((response) => {
    if (response.success) {
        console.info("Successfully requested for /stars")
        console.log(response.data)
    } else {
        console.error("An error occured while requesting for /stars, error: " + response.error)
    }
})
```

</details>


<details>
    <summary>Python Example</summary>

#### **Python**

```python
import requests
r = requests.request("GET", "/stars")
if r.status_code >= 400 or not r.json()["success"]:
    raise ValueError("An error occured while requesting for /stars, error: " + r.json()["error"])
print("Successfully requested for /stars")
print(r.json()["data"])
```

</details>
<!-- tabs:end -->

#### Possible Errors

| Exception         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `DATABASE_DISABLED` | When the server disabled any database interaction  | 501  |
[Return to the Index](../Getting%20Started.md#index)

# Translation Star

 - ### Using GET

Get the stars for a translation

```http
GET /stars/<translation_id>
```

> [server/endpoints/stars.py](../../server/endpoints/stars.py#L82)

#### Authentication

Login is **not** required

#### Dynamic URL

| Name         | Description                      | Required         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `translation_id` | The ID of the translation to get  | Yes            | str            |

#### Example

<!-- tabs:start -->


<details>
    <summary>cURL Example</summary>

##### **cURL**

```bash
curl -X GET "/stars/<translation_id>"
```

</details>


<details>
    <summary>JavaScript Example</summary>

##### **JavaScript**

```javascript
fetch("/stars/<translation_id>", {
    method: "GET"
})
.then((response) => {response.json()})
.then((response) => {
    if (response.success) {
        console.info("Successfully requested for /stars/<translation_id>")
        console.log(response.data)
    } else {
        console.error("An error occured while requesting for /stars/<translation_id>, error: " + response.error)
    }
})
```

</details>


<details>
    <summary>Python Example</summary>

##### **Python**

```python
import requests
r = requests.request("GET", "/stars/<translation_id>")
if r.status_code >= 400 or not r.json()["success"]:
    raise ValueError("An error occured while requesting for /stars/<translation_id>, error: " + r.json()["error"])
print("Successfully requested for /stars/<translation_id>")
print(r.json()["data"])
```

</details>
<!-- tabs:end -->

#### Response

##### Example response

```json
{
    "success": true,
    "message": "Successfully processed your request",
    "error": null,
    "data": {
        "source": "no example",
        "result": "no example",
        "language": "no example",
        "users": "no example"
    }
}

```

##### Returns

| Field        | Description                      | Type   | Nullable  |
| ----------   | -------------------------------- | ------ | --------- |
| `source` | The source text  | string      | No      |
| `result` | The result text  | string      | No      |
| `language` | The translation languages  | string      | No      |
| `users` | The number of users who starred the translation  | <class 'int'>      | No      |

##### Possible Errors

| Exception         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `FORBIDDEN` | You are not allowed to star this translation  | 403  |
| `NOT_FOUND` | The translation could not be found  | 404  |
| `DATABASE_DISABLED` | When the server disabled any database interaction  | 501  |
[Return to the Index](../Getting%20Started.md#index)

 - ### Using POST

Star a translation

```http
POST /stars/<translation_id>
```

> [server/endpoints/stars.py](../../server/endpoints/stars.py#L82)

#### Authentication

Login is **not** required

#### Parameters

| Name         | Description                      | Required         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `token` | The token to authenticate the translation  | Yes            | TranslationToken            |

#### Dynamic URL

| Name         | Description                      | Required         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `translation_id` | The ID of the translation to star  | Yes            | str            |

#### Example

<!-- tabs:start -->


<details>
    <summary>cURL Example</summary>

##### **cURL**

```bash
curl -X POST \
    --data-urlencode "token=<The token to authenticate the translation>" \
    "/stars/<translation_id>"
```

</details>


<details>
    <summary>JavaScript Example</summary>

##### **JavaScript**

```javascript
fetch(`/stars/<translation_id>?token=${encodeURIComponent("token")}`, {
    method: "POST"
})
.then((response) => {response.json()})
.then((response) => {
    if (response.success) {
        console.info("Successfully requested for /stars/<translation_id>")
        console.log(response.data)
    } else {
        console.error("An error occured while requesting for /stars/<translation_id>, error: " + response.error)
    }
})
```

</details>


<details>
    <summary>Python Example</summary>

##### **Python**

```python
import requests
r = requests.request("POST", "/stars/<translation_id>",
        params = {
            "token": "The token to authenticate the translation"
        })
if r.status_code >= 400 or not r.json()["success"]:
    raise ValueError("An error occured while requesting for /stars/<translation_id>, error: " + r.json()["error"])
print("Successfully requested for /stars/<translation_id>")
print(r.json()["data"])
```

</details>
<!-- tabs:end -->

#### Response

##### Example response

```json
{
    "success": true,
    "message": "Successfully processed your request",
    "error": null,
    "data": {
        "source": "no example",
        "result": "no example",
        "language": "no example",
        "users": "no example"
    }
}

```

##### Returns

| Field        | Description                      | Type   | Nullable  |
| ----------   | -------------------------------- | ------ | --------- |
| `source` | The source text  | string      | No      |
| `result` | The result text  | string      | No      |
| `language` | The translation languages  | string      | No      |
| `users` | The number of users who starred the translation  | <class 'int'>      | No      |

##### Possible Errors

| Exception         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `FORBIDDEN` | You are not allowed to star this translation  | 403  |
| `NOT_FOUND` | The translation could not be found  | 404  |
| `DATABASE_DISABLED` | When the server disabled any database interaction  | 501  |
[Return to the Index](../Getting%20Started.md#index)

 - ### Using DELETE

Unstar a translation

```http
DELETE /stars/<translation_id>
```

> [server/endpoints/stars.py](../../server/endpoints/stars.py#L82)

#### Authentication

Login is **not** required

#### Dynamic URL

| Name         | Description                      | Required         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `translation_id` | The ID of the translation to unstar  | Yes            | str            |

#### Example

<!-- tabs:start -->


<details>
    <summary>cURL Example</summary>

##### **cURL**

```bash
curl -X DELETE "/stars/<translation_id>"
```

</details>


<details>
    <summary>JavaScript Example</summary>

##### **JavaScript**

```javascript
fetch("/stars/<translation_id>", {
    method: "DELETE"
})
.then((response) => {response.json()})
.then((response) => {
    if (response.success) {
        console.info("Successfully requested for /stars/<translation_id>")
        console.log(response.data)
    } else {
        console.error("An error occured while requesting for /stars/<translation_id>, error: " + response.error)
    }
})
```

</details>


<details>
    <summary>Python Example</summary>

##### **Python**

```python
import requests
r = requests.request("DELETE", "/stars/<translation_id>")
if r.status_code >= 400 or not r.json()["success"]:
    raise ValueError("An error occured while requesting for /stars/<translation_id>, error: " + r.json()["error"])
print("Successfully requested for /stars/<translation_id>")
print(r.json()["data"])
```

</details>
<!-- tabs:end -->

##### Possible Errors

| Exception         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `FORBIDDEN` | You are not allowed to star this translation  | 403  |
| `NOT_FOUND` | The translation could not be found  | 404  |
| `DATABASE_DISABLED` | When the server disabled any database interaction  | 501  |
[Return to the Index](../Getting%20Started.md#index)
