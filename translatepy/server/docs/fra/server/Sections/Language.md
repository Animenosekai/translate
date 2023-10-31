
# Référence de la section Language

Ce fichier liste et explique les différents *endpoints* disponible sous la section Language

# __language__

This represents a non implemented endpoint

```http
* /api/language/<string:language>
```

> [../../../../endpoints/api/language.py](../../../../endpoints/api/language.py#L17)

### Authentification

Il n'est **pas** nécessaire d'être authentifié

### URL Dynamique

| Nom         | Description                      | Obligatoire         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `language` | Il n'y a pas de description  | Oui            | str            |

### Exemple

<!-- tabs:start -->


<details>
    <summary>cURL Exemple</summary>

#### **cURL**

```bash
curl -X * "/api/language/<string:language>"
```

</details>


<details>
    <summary>JavaScript Exemple</summary>

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
    <summary>Python Exemple</summary>

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

#### Erreurs possibles

| Erreur         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy  | 500  |
[Retourner à l'Index](../Pour%20commencer.md#index)

# search

This represents a non implemented endpoint

```http
* /api/language/search
```

> [../../../../endpoints/api/language.py](../../../../endpoints/api/language.py#L22)

### Authentification

Il n'est **pas** nécessaire d'être authentifié

### Exemple

<!-- tabs:start -->


<details>
    <summary>cURL Exemple</summary>

#### **cURL**

```bash
curl -X * "/api/language/search"
```

</details>


<details>
    <summary>JavaScript Exemple</summary>

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
    <summary>Python Exemple</summary>

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

### Réponse

#### Exemple de réponse

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

#### Retourne

| Champ        | Description                      | Type   | Peut être `null`  |
| ----------   | -------------------------------- | ------ | --------- |
| `languages` | The language search results  | <class 'list'>      | Non      |

#### Erreurs possibles

| Erreur         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy  | 500  |
[Retourner à l'Index](../Pour%20commencer.md#index)