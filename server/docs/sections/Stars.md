
# Stars Section API Reference

This file lists and explains the different endpoints available in the Stars section.

##  > Nasse > Models > Hello

Get all starred translations

```http
GET /stars
```

> [server/endpoints/stars.py](../../server/endpoints/stars.py#L47)

### Authentication

Login is **not** required

### Example

<!-- tabs:start -->

#### **cURL**

```bash
curl -X GET "/stars"
```

#### **JavaScript**

```bash
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

#### **Python**

```bash
import requests
r = requests.request("GET", "/stars")
if r.status_code >= 400 or not r.json()["success"]:
    raise ValueError("An error occured while requesting for /stars, error: " + r.json()["error"])
print("Successfully requested for /stars")
print(r.json()["data"])
```
<!-- tabs:end -->

#### Possible Errors

| Exception         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `DATABASE_DISABLED` | When the server disabled any database interaction  | 501  |
[Return to the Index](../Getting%20Started.md#index)

## Translation Star

- ### Using GET

Get the stars for a translation

```http
GET /stars/<translation_id>
```

> [server/endpoints/stars.py](../../server/endpoints/stars.py#L79)

#### Authentication

Login is **not** required

#### Dynamic URL

| Name         | Description                      | Required         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `translation_id` | The ID of the translation to get  | True            | str            |

#### Response

##### Example Response

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
| `source` | The source text  | string      | False      |
| `result` | The result text  | string      | False      |
| `language` | The translation languages  | string      | False      |
| `users` | The number of users who starred the translation  | <class 'int'>      | False      |

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

> [server/endpoints/stars.py](../../server/endpoints/stars.py#L79)

#### Authentication

Login is **not** required

#### Parameters

| Name         | Description                      | Required         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `token` | The token to authenticate the translation  | True            | TranslationToken            |

#### Dynamic URL

| Name         | Description                      | Required         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `translation_id` | The ID of the translation to star  | True            | str            |

#### Response

##### Example Response

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
| `source` | The source text  | string      | False      |
| `result` | The result text  | string      | False      |
| `language` | The translation languages  | string      | False      |
| `users` | The number of users who starred the translation  | <class 'int'>      | False      |

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

> [server/endpoints/stars.py](../../server/endpoints/stars.py#L79)

#### Authentication

Login is **not** required

#### Dynamic URL

| Name         | Description                      | Required         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `translation_id` | The ID of the translation to unstar  | True            | str            |

##### Possible Errors

| Exception         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `FORBIDDEN` | You are not allowed to star this translation  | 403  |
| `NOT_FOUND` | The translation could not be found  | 404  |
| `DATABASE_DISABLED` | When the server disabled any database interaction  | 501  |
[Return to the Index](../Getting%20Started.md#index)
