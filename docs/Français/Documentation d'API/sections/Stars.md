
# Référence de la section Stars

Ce fichier liste et explique les différents *endpoints* disponible sous la section Stars

# Stars

Get all starred translations

```http
GET /stars
```

> [server/endpoints/stars.py](../../server/endpoints/stars.py#L49)

### Authentification

Il n'est **pas** nécessaire d'être authentifié

### Exemple

<!-- tabs:start -->


<details>
    <summary>cURL Exemple</summary>

#### **cURL**

```bash
curl -X GET "/stars"
```

</details>


<details>
    <summary>JavaScript Exemple</summary>

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
    <summary>Python Exemple</summary>

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

#### Erreurs possibles

| Erreur         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `DATABASE_DISABLED` | When the server disabled any database interaction  | 501  |
[Retourner à l'Index](../Pour%20commencer.md#index)

# Translation Star

 - ### En utilisant GET

Get the stars for a translation

```http
GET /stars/<translation_id>
```

> [server/endpoints/stars.py](../../server/endpoints/stars.py#L82)

#### Authentification

Il n'est **pas** nécessaire d'être authentifié

#### URL Dynamique

| Nom         | Description                      | Obligatoire         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `translation_id` | The ID of the translation to get  | Oui            | str            |

#### Exemple

<!-- tabs:start -->


<details>
    <summary>cURL Exemple</summary>

##### **cURL**

```bash
curl -X GET "/stars/<translation_id>"
```

</details>


<details>
    <summary>JavaScript Exemple</summary>

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
    <summary>Python Exemple</summary>

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

#### Réponse

##### Exemple de réponse

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

##### Retourne

| Champ        | Description                      | Type   | Peut être `null`  |
| ----------   | -------------------------------- | ------ | --------- |
| `source` | The source text  | string      | Non      |
| `result` | The result text  | string      | Non      |
| `language` | The translation languages  | string      | Non      |
| `users` | The number of users who starred the translation  | <class 'int'>      | Non      |

##### Erreurs possibles

| Erreur         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `FORBIDDEN` | You are not allowed to star this translation  | 403  |
| `NOT_FOUND` | The translation could not be found  | 404  |
| `DATABASE_DISABLED` | When the server disabled any database interaction  | 501  |
[Retourner à l'Index](../Pour%20commencer.md#index)

 - ### En utilisant POST

Star a translation

```http
POST /stars/<translation_id>
```

> [server/endpoints/stars.py](../../server/endpoints/stars.py#L82)

#### Authentification

Il n'est **pas** nécessaire d'être authentifié

#### Paramètres

| Nom         | Description                      | Obligatoire         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `token` | The token to authenticate the translation  | Oui            | TranslationToken            |

#### URL Dynamique

| Nom         | Description                      | Obligatoire         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `translation_id` | The ID of the translation to star  | Oui            | str            |

#### Exemple

<!-- tabs:start -->


<details>
    <summary>cURL Exemple</summary>

##### **cURL**

```bash
curl -X POST \
    --data-urlencode "token=<The token to authenticate the translation>" \
    "/stars/<translation_id>"
```

</details>


<details>
    <summary>JavaScript Exemple</summary>

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
    <summary>Python Exemple</summary>

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

#### Réponse

##### Exemple de réponse

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

##### Retourne

| Champ        | Description                      | Type   | Peut être `null`  |
| ----------   | -------------------------------- | ------ | --------- |
| `source` | The source text  | string      | Non      |
| `result` | The result text  | string      | Non      |
| `language` | The translation languages  | string      | Non      |
| `users` | The number of users who starred the translation  | <class 'int'>      | Non      |

##### Erreurs possibles

| Erreur         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `FORBIDDEN` | You are not allowed to star this translation  | 403  |
| `NOT_FOUND` | The translation could not be found  | 404  |
| `DATABASE_DISABLED` | When the server disabled any database interaction  | 501  |
[Retourner à l'Index](../Pour%20commencer.md#index)

 - ### En utilisant DELETE

Unstar a translation

```http
DELETE /stars/<translation_id>
```

> [server/endpoints/stars.py](../../server/endpoints/stars.py#L82)

#### Authentification

Il n'est **pas** nécessaire d'être authentifié

#### URL Dynamique

| Nom         | Description                      | Obligatoire         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `translation_id` | The ID of the translation to unstar  | Oui            | str            |

#### Exemple

<!-- tabs:start -->


<details>
    <summary>cURL Exemple</summary>

##### **cURL**

```bash
curl -X DELETE "/stars/<translation_id>"
```

</details>


<details>
    <summary>JavaScript Exemple</summary>

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
    <summary>Python Exemple</summary>

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

##### Erreurs possibles

| Erreur         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `FORBIDDEN` | You are not allowed to star this translation  | 403  |
| `NOT_FOUND` | The translation could not be found  | 404  |
| `DATABASE_DISABLED` | When the server disabled any database interaction  | 501  |
[Retourner à l'Index](../Pour%20commencer.md#index)
