
# Référence de la section Stats

Ce fichier liste et explique les différents *endpoints* disponible sous la section Stats

# Timings Stats

Get all timings

```http
GET /stats/timings
```

> [server/endpoints/stats.py](../../server/endpoints/stats.py#L17)

### Authentification

Il n'est **pas** nécessaire d'être authentifié

### Paramètres

| Nom         | Description                      | Obligatoire         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `granularity` | The granularity of the stats  | Non            | Granularity            |

### Exemple

<!-- tabs:start -->


<details>
    <summary>cURL Exemple</summary>

#### **cURL**

```bash
curl -X GET "/stats/timings"
```

</details>


<details>
    <summary>JavaScript Exemple</summary>

#### **JavaScript**

```javascript
fetch("/stats/timings", {
    method: "GET"
})
.then((response) => {response.json()})
.then((response) => {
    if (response.success) {
        console.info("Successfully requested for /stats/timings")
        console.log(response.data)
    } else {
        console.error("An error occured while requesting for /stats/timings, error: " + response.error)
    }
})
```

</details>


<details>
    <summary>Python Exemple</summary>

#### **Python**

```python
import requests
r = requests.request("GET", "/stats/timings")
if r.status_code >= 400 or not r.json()["success"]:
    raise ValueError("An error occured while requesting for /stats/timings, error: " + r.json()["error"])
print("Successfully requested for /stats/timings")
print(r.json()["data"])
```

</details>
<!-- tabs:end -->

#### Erreurs possibles

| Erreur         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `DATABASE_DISABLED` | When the server disabled any database interaction  | 501  |
[Retourner à l'Index](../Pour%20commencer.md#index)

# Erros Stats

Get all errors count for each service

```http
GET /stats/errors
```

> [server/endpoints/stats.py](../../server/endpoints/stats.py#L28)

### Authentification

Il n'est **pas** nécessaire d'être authentifié

### Paramètres

| Nom         | Description                      | Obligatoire         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `granularity` | The granularity of the stats  | Non            | Granularity            |

### Exemple

<!-- tabs:start -->


<details>
    <summary>cURL Exemple</summary>

#### **cURL**

```bash
curl -X GET "/stats/errors"
```

</details>


<details>
    <summary>JavaScript Exemple</summary>

#### **JavaScript**

```javascript
fetch("/stats/errors", {
    method: "GET"
})
.then((response) => {response.json()})
.then((response) => {
    if (response.success) {
        console.info("Successfully requested for /stats/errors")
        console.log(response.data)
    } else {
        console.error("An error occured while requesting for /stats/errors, error: " + response.error)
    }
})
```

</details>


<details>
    <summary>Python Exemple</summary>

#### **Python**

```python
import requests
r = requests.request("GET", "/stats/errors")
if r.status_code >= 400 or not r.json()["success"]:
    raise ValueError("An error occured while requesting for /stats/errors, error: " + r.json()["error"])
print("Successfully requested for /stats/errors")
print(r.json()["data"])
```

</details>
<!-- tabs:end -->

#### Erreurs possibles

| Erreur         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `DATABASE_DISABLED` | When the server disabled any database interaction  | 501  |
[Retourner à l'Index](../Pour%20commencer.md#index)