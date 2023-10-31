
# Référence de la section Work

Ce fichier liste et explique les différents *endpoints* disponible sous la section Work

# translate

Translates the text in the given language

```http
GET /api/translate
```

> [../../../../endpoints/api/_.py](../../../../endpoints/api/_.py#L113)

### Authentification

Il n'est **pas** nécessaire d'être authentifié

### Paramètres

| Nom         | Description                      | Obligatoire         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `translators` | A comma-separated list of translators to use  | Non            | TranslatorList            |

### Exemple

<!-- tabs:start -->


<details>
    <summary>cURL Exemple</summary>

#### **cURL**

```bash
curl -X GET \
    --data-urlencode "translators=<A comma-separated list of translators to use>" \
    "/api/translate"
```

</details>


<details>
    <summary>JavaScript Exemple</summary>

#### **JavaScript**

```javascript
fetch("/api/translate", {
    method: "GET"
})
.then((response) => {response.json()})
.then((response) => {
    if (response.success) {
        console.info("Successfully requested for /api/translate")
        console.log(response.data)
    } else {
        console.error("An error occured while requesting for /api/translate, error: " + response.error)
    }
})
```

</details>


<details>
    <summary>Python Exemple</summary>

#### **Python**

```python
import requests
r = requests.request("GET", "/api/translate")
if r.status_code >= 400 or not r.json()["success"]:
    raise ValueError("An error occured while requesting for /api/translate, error: " + r.json()["error"])
print("Successfully requested for /api/translate")
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
        "service": "no example",
        "translation": "no example",
        "dest_lang": "no example",
        "source": "no example",
        "source_lang": "no example"
    }
}

```

#### Retourne

| Champ        | Description                      | Type   | Peut être `null`  |
| ----------   | -------------------------------- | ------ | --------- |
| `service` | The service which returned the result  | Translator      | Non      |
| `translation` | The translation result  | string      | Non      |
| `dest_lang` | The result's language  | Language      | Non      |
| `source` | The source text  | string      | Non      |
| `source_lang` | The source text's language  | Language      | Non      |

#### Erreurs possibles

| Erreur         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy  | 500  |
[Retourner à l'Index](../Pour%20commencer.md#index)

# translate_html

Translates the HTML in the given language

```http
GET /api/translate/html
```

> [../../../../endpoints/api/_.py](../../../../endpoints/api/_.py#L121)

### Authentification

Il n'est **pas** nécessaire d'être authentifié

### Paramètres

| Nom         | Description                      | Obligatoire         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `translators` | A comma-separated list of translators to use  | Non            | TranslatorList            |

### Exemple

<!-- tabs:start -->


<details>
    <summary>cURL Exemple</summary>

#### **cURL**

```bash
curl -X GET \
    --data-urlencode "translators=<A comma-separated list of translators to use>" \
    "/api/translate/html"
```

</details>


<details>
    <summary>JavaScript Exemple</summary>

#### **JavaScript**

```javascript
fetch("/api/translate/html", {
    method: "GET"
})
.then((response) => {response.json()})
.then((response) => {
    if (response.success) {
        console.info("Successfully requested for /api/translate/html")
        console.log(response.data)
    } else {
        console.error("An error occured while requesting for /api/translate/html, error: " + response.error)
    }
})
```

</details>


<details>
    <summary>Python Exemple</summary>

#### **Python**

```python
import requests
r = requests.request("GET", "/api/translate/html")
if r.status_code >= 400 or not r.json()["success"]:
    raise ValueError("An error occured while requesting for /api/translate/html, error: " + r.json()["error"])
print("Successfully requested for /api/translate/html")
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
        "service": "no example",
        "source_lang": "no example",
        "source": "no example"
    }
}

```

#### Retourne

| Champ        | Description                      | Type   | Peut être `null`  |
| ----------   | -------------------------------- | ------ | --------- |
| `service` | The service which returned the result  | Translator      | Non      |
| `source_lang` | The source text's language  | Language      | Non      |
| `source` | The source text  | string      | Non      |

#### Erreurs possibles

| Erreur         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy  | 500  |
[Retourner à l'Index](../Pour%20commencer.md#index)

# stream

Streams all translations available using the different translators

```http
* /api/stream
```

> [../../../../endpoints/api/_.py](../../../../endpoints/api/_.py#L133)

### Authentification

Il n'est **pas** nécessaire d'être authentifié

### Exemple

<!-- tabs:start -->


<details>
    <summary>cURL Exemple</summary>

#### **cURL**

```bash
curl -X * "/api/stream"
```

</details>


<details>
    <summary>JavaScript Exemple</summary>

#### **JavaScript**

```javascript
fetch("/api/stream", {
    method: "*"
})
.then((response) => {response.json()})
.then((response) => {
    if (response.success) {
        console.info("Successfully requested for /api/stream")
        console.log(response.data)
    } else {
        console.error("An error occured while requesting for /api/stream, error: " + response.error)
    }
})
```

</details>


<details>
    <summary>Python Exemple</summary>

#### **Python**

```python
import requests
r = requests.request("*", "/api/stream")
if r.status_code >= 400 or not r.json()["success"]:
    raise ValueError("An error occured while requesting for /api/stream, error: " + r.json()["error"])
print("Successfully requested for /api/stream")
print(r.json()["data"])
```

</details>
<!-- tabs:end -->

#### Erreurs possibles

| Erreur         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy  | 500  |
[Retourner à l'Index](../Pour%20commencer.md#index)

# transliterate

Transliterates the text in the given language

```http
GET /api/transliterate
```

> [../../../../endpoints/api/_.py](../../../../endpoints/api/_.py#L186)

### Authentification

Il n'est **pas** nécessaire d'être authentifié

### Paramètres

| Nom         | Description                      | Obligatoire         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `translators` | A comma-separated list of translators to use  | Non            | TranslatorList            |

### Exemple

<!-- tabs:start -->


<details>
    <summary>cURL Exemple</summary>

#### **cURL**

```bash
curl -X GET \
    --data-urlencode "translators=<A comma-separated list of translators to use>" \
    "/api/transliterate"
```

</details>


<details>
    <summary>JavaScript Exemple</summary>

#### **JavaScript**

```javascript
fetch("/api/transliterate", {
    method: "GET"
})
.then((response) => {response.json()})
.then((response) => {
    if (response.success) {
        console.info("Successfully requested for /api/transliterate")
        console.log(response.data)
    } else {
        console.error("An error occured while requesting for /api/transliterate, error: " + response.error)
    }
})
```

</details>


<details>
    <summary>Python Exemple</summary>

#### **Python**

```python
import requests
r = requests.request("GET", "/api/transliterate")
if r.status_code >= 400 or not r.json()["success"]:
    raise ValueError("An error occured while requesting for /api/transliterate, error: " + r.json()["error"])
print("Successfully requested for /api/transliterate")
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
        "service": "no example",
        "transliteration": "no example",
        "dest_lang": "no example",
        "source": "no example",
        "source_lang": "no example"
    }
}

```

#### Retourne

| Champ        | Description                      | Type   | Peut être `null`  |
| ----------   | -------------------------------- | ------ | --------- |
| `service` | The service which returned the result  | Translator      | Non      |
| `transliteration` | The transliteration result  | string      | Non      |
| `dest_lang` | The result's language  | Language      | Non      |
| `source` | The source text  | string      | Non      |
| `source_lang` | The source text's language  | Language      | Non      |

#### Erreurs possibles

| Erreur         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy  | 500  |
[Retourner à l'Index](../Pour%20commencer.md#index)

# spellcheck

Spellchecks the given text

```http
GET /api/spellcheck
```

> [../../../../endpoints/api/_.py](../../../../endpoints/api/_.py#L194)

### Authentification

Il n'est **pas** nécessaire d'être authentifié

### Paramètres

| Nom         | Description                      | Obligatoire         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `translators` | A comma-separated list of translators to use  | Non            | TranslatorList            |

### Exemple

<!-- tabs:start -->


<details>
    <summary>cURL Exemple</summary>

#### **cURL**

```bash
curl -X GET \
    --data-urlencode "translators=<A comma-separated list of translators to use>" \
    "/api/spellcheck"
```

</details>


<details>
    <summary>JavaScript Exemple</summary>

#### **JavaScript**

```javascript
fetch("/api/spellcheck", {
    method: "GET"
})
.then((response) => {response.json()})
.then((response) => {
    if (response.success) {
        console.info("Successfully requested for /api/spellcheck")
        console.log(response.data)
    } else {
        console.error("An error occured while requesting for /api/spellcheck, error: " + response.error)
    }
})
```

</details>


<details>
    <summary>Python Exemple</summary>

#### **Python**

```python
import requests
r = requests.request("GET", "/api/spellcheck")
if r.status_code >= 400 or not r.json()["success"]:
    raise ValueError("An error occured while requesting for /api/spellcheck, error: " + r.json()["error"])
print("Successfully requested for /api/spellcheck")
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
        "service": "no example",
        "source": "no example",
        "source_lang": "no example",
        "corrected": "no example",
        "rich": true
    }
}

```

#### Retourne

| Champ        | Description                      | Type   | Peut être `null`  |
| ----------   | -------------------------------- | ------ | --------- |
| `service` | The service which returned the result  | Translator      | Non      |
| `source` | The source text  | string      | Non      |
| `source_lang` | The source text's language  | Language      | Non      |
| `corrected` | The corrected text  | string      | Non      |
| `rich` | Whether the given result features the full range of information  | bool      | Non      |

#### Erreurs possibles

| Erreur         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy  | 500  |
[Retourner à l'Index](../Pour%20commencer.md#index)

# language

Retrieves the language of the given text

```http
GET /api/language
```

> [../../../../endpoints/api/_.py](../../../../endpoints/api/_.py#L202)

### Authentification

Il n'est **pas** nécessaire d'être authentifié

### Paramètres

| Nom         | Description                      | Obligatoire         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `translators` | A comma-separated list of translators to use  | Non            | TranslatorList            |

### Exemple

<!-- tabs:start -->


<details>
    <summary>cURL Exemple</summary>

#### **cURL**

```bash
curl -X GET \
    --data-urlencode "translators=<A comma-separated list of translators to use>" \
    "/api/language"
```

</details>


<details>
    <summary>JavaScript Exemple</summary>

#### **JavaScript**

```javascript
fetch("/api/language", {
    method: "GET"
})
.then((response) => {response.json()})
.then((response) => {
    if (response.success) {
        console.info("Successfully requested for /api/language")
        console.log(response.data)
    } else {
        console.error("An error occured while requesting for /api/language, error: " + response.error)
    }
})
```

</details>


<details>
    <summary>Python Exemple</summary>

#### **Python**

```python
import requests
r = requests.request("GET", "/api/language")
if r.status_code >= 400 or not r.json()["success"]:
    raise ValueError("An error occured while requesting for /api/language, error: " + r.json()["error"])
print("Successfully requested for /api/language")
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
        "service": "no example",
        "source_lang": "no example",
        "source": "no example"
    }
}

```

#### Retourne

| Champ        | Description                      | Type   | Peut être `null`  |
| ----------   | -------------------------------- | ------ | --------- |
| `service` | The service which returned the result  | Translator      | Non      |
| `source_lang` | The source text's language  | Language      | Non      |
| `source` | The source text  | string      | Non      |

#### Erreurs possibles

| Erreur         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy  | 500  |
[Retourner à l'Index](../Pour%20commencer.md#index)

# example

Finds examples for the given text

```http
GET /api/example
```

> [../../../../endpoints/api/_.py](../../../../endpoints/api/_.py#L210)

### Authentification

Il n'est **pas** nécessaire d'être authentifié

### Paramètres

| Nom         | Description                      | Obligatoire         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `translators` | A comma-separated list of translators to use  | Non            | TranslatorList            |

### Exemple

<!-- tabs:start -->


<details>
    <summary>cURL Exemple</summary>

#### **cURL**

```bash
curl -X GET \
    --data-urlencode "translators=<A comma-separated list of translators to use>" \
    "/api/example"
```

</details>


<details>
    <summary>JavaScript Exemple</summary>

#### **JavaScript**

```javascript
fetch("/api/example", {
    method: "GET"
})
.then((response) => {response.json()})
.then((response) => {
    if (response.success) {
        console.info("Successfully requested for /api/example")
        console.log(response.data)
    } else {
        console.error("An error occured while requesting for /api/example, error: " + response.error)
    }
})
```

</details>


<details>
    <summary>Python Exemple</summary>

#### **Python**

```python
import requests
r = requests.request("GET", "/api/example")
if r.status_code >= 400 or not r.json()["success"]:
    raise ValueError("An error occured while requesting for /api/example, error: " + r.json()["error"])
print("Successfully requested for /api/example")
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
        "service": "no example",
        "reference": "no example",
        "source": "no example",
        "source_lang": "no example",
        "example": "no example",
        "positions": "no example"
    }
}

```

#### Retourne

| Champ        | Description                      | Type   | Peut être `null`  |
| ----------   | -------------------------------- | ------ | --------- |
| `service` | The service which returned the result  | Translator      | Non      |
| `reference` | Where the example comes from (i.e a book or a the person who said it if it's a quote)  | string      | Non      |
| `source` | The source text  | string      | Non      |
| `source_lang` | The source text's language  | Language      | Non      |
| `example` | The example  | string      | Non      |
| `positions` | The positions of the word in the example  | list[int]      | Non      |

#### Erreurs possibles

| Erreur         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy  | 500  |
[Retourner à l'Index](../Pour%20commencer.md#index)

# dictionary

Retrieves meanings for the given text

```http
GET /api/dictionary
```

> [../../../../endpoints/api/_.py](../../../../endpoints/api/_.py#L218)

### Authentification

Il n'est **pas** nécessaire d'être authentifié

### Paramètres

| Nom         | Description                      | Obligatoire         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `translators` | A comma-separated list of translators to use  | Non            | TranslatorList            |

### Exemple

<!-- tabs:start -->


<details>
    <summary>cURL Exemple</summary>

#### **cURL**

```bash
curl -X GET \
    --data-urlencode "translators=<A comma-separated list of translators to use>" \
    "/api/dictionary"
```

</details>


<details>
    <summary>JavaScript Exemple</summary>

#### **JavaScript**

```javascript
fetch("/api/dictionary", {
    method: "GET"
})
.then((response) => {response.json()})
.then((response) => {
    if (response.success) {
        console.info("Successfully requested for /api/dictionary")
        console.log(response.data)
    } else {
        console.error("An error occured while requesting for /api/dictionary, error: " + response.error)
    }
})
```

</details>


<details>
    <summary>Python Exemple</summary>

#### **Python**

```python
import requests
r = requests.request("GET", "/api/dictionary")
if r.status_code >= 400 or not r.json()["success"]:
    raise ValueError("An error occured while requesting for /api/dictionary, error: " + r.json()["error"])
print("Successfully requested for /api/dictionary")
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
        "service": "no example",
        "source_lang": "no example",
        "source": "no example",
        "meaning": "no example",
        "rich": true
    }
}

```

#### Retourne

| Champ        | Description                      | Type   | Peut être `null`  |
| ----------   | -------------------------------- | ------ | --------- |
| `service` | The service which returned the result  | Translator      | Non      |
| `source_lang` | The source text's language  | Language      | Non      |
| `source` | The source text  | string      | Non      |
| `meaning` | The meaning of the text  | string      | Non      |
| `rich` | Whether the given result features the full range of information  | bool      | Non      |

#### Erreurs possibles

| Erreur         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy  | 500  |
[Retourner à l'Index](../Pour%20commencer.md#index)

# tts

Returns the speech version of the given text

```http
GET /api/tts
```

> [../../../../endpoints/api/_.py](../../../../endpoints/api/_.py#L226)

### Authentification

Il n'est **pas** nécessaire d'être authentifié

### Paramètres

| Nom         | Description                      | Obligatoire         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `translators` | A comma-separated list of translators to use  | Non            | TranslatorList            |

### Exemple

<!-- tabs:start -->


<details>
    <summary>cURL Exemple</summary>

#### **cURL**

```bash
curl -X GET \
    --data-urlencode "translators=<A comma-separated list of translators to use>" \
    "/api/tts"
```

</details>


<details>
    <summary>JavaScript Exemple</summary>

#### **JavaScript**

```javascript
fetch("/api/tts", {
    method: "GET"
})
.then((response) => {response.json()})
.then((response) => {
    if (response.success) {
        console.info("Successfully requested for /api/tts")
        console.log(response.data)
    } else {
        console.error("An error occured while requesting for /api/tts, error: " + response.error)
    }
})
```

</details>


<details>
    <summary>Python Exemple</summary>

#### **Python**

```python
import requests
r = requests.request("GET", "/api/tts")
if r.status_code >= 400 or not r.json()["success"]:
    raise ValueError("An error occured while requesting for /api/tts, error: " + r.json()["error"])
print("Successfully requested for /api/tts")
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
        "extension": "no example",
        "result": "no example",
        "source": "no example",
        "speed": 4,
        "gender": "no example",
        "service": "no example",
        "mime_type": "no example",
        "source_lang": "no example"
    }
}

```

#### Retourne

| Champ        | Description                      | Type   | Peut être `null`  |
| ----------   | -------------------------------- | ------ | --------- |
| `extension` | Returns the audio file extension  | Optional[str]      | Non      |
| `result` | Text to speech result  | bytes      | Non      |
| `source` | The source text  | string      | Non      |
| `speed` | Speed of the text to speech result  | int      | Non      |
| `gender` | Gender of the 'person' saying the text  | Gender      | Non      |
| `service` | The service which returned the result  | Translator      | Non      |
| `mime_type` | Returns the MIME type of the audio file  | Optional[str]      | Non      |
| `source_lang` | The source text's language  | Language      | Non      |

#### Erreurs possibles

| Erreur         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy  | 500  |
[Retourner à l'Index](../Pour%20commencer.md#index)