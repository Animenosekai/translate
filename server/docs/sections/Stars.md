
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

##### Possible Errors

| Exception         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `FORBIDDEN` | You are not allowed to star this translation  | 403  |
| `NOT_FOUND` | The translation could not be found  | 404  |
| `DATABASE_DISABLED` | When the server disabled any database interaction  | 501  |
[Return to the Index](../Getting%20Started.md#index)
