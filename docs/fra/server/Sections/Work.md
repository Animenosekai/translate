
# Référence de la section Work

Ce fichier liste et explique les différents *endpoints* disponible sous la section Work

# translate

Translates the text in the given language

```http
GET /api/translate
```

> [../../../../translatepy/server/endpoints/api/_.py](../../../../translatepy/server/endpoints/api/_.py#L113)

### Authentification

Il n'est **pas** nécessaire d'être authentifié

### Paramètres

| Nom         | Description                      | Obligatoire         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `dest_lang` | The language to translate to  | Oui            | Language            |
| `translators` | A comma-separated list of translators to use  | Non            | TranslatorList            |
| `text` | The text to translate  | Oui            | str            |
| `source_lang` | The language `text` is in. If "auto", the translator will try to infer the language from `text`  | Non            | Language            |

### Exemple

<!-- tabs:start -->


<details>
    <summary>cURL Exemple</summary>

#### **cURL**

```bash
curl -X GET \
    --data-urlencode "dest_lang=<The language to translate to>"\
    --data-urlencode "translators=<A comma-separated list of translators to use>"\
    --data-urlencode "text=<The text to translate>"\
    --data-urlencode "source_lang=<The language `text` is in. If \"auto\", the translator will try to infer the language from `text`>" \
    "/api/translate"
```

</details>


<details>
    <summary>JavaScript Exemple</summary>

#### **JavaScript**

```javascript
fetch(`/api/translate?dest_lang=${encodeURIComponent("dest_lang")}&text=${encodeURIComponent("text")}`, {
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
r = requests.request("GET", "/api/translate",
        params = {
            "dest_lang": "The language to translate to",
            "text": "The text to translate"
        })
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
        "source_lang": "no example",
        "dest_lang": "no example",
        "service": "no example",
        "translation": "no example",
        "source": "no example"
    }
}

```

#### Retourne

| Champ        | Description                      | Type   | Peut être `null`  |
| ----------   | -------------------------------- | ------ | --------- |
| `source_lang` | The source text's language  | Language      | Non      |
| `dest_lang` | The result's language  | Language      | Non      |
| `service` | The service which returned the result  | Translator      | Non      |
| `translation` | The translation result  | string      | Non      |
| `source` | The source text  | string      | Non      |

#### Erreurs possibles

| Erreur         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy  | 500  |
[Retourner à l'Index](../Pour%20commencer.md#index)

# translate_html

Translates the HTML in the given language

```http
GET /api/translate/html
```

> [../../../../translatepy/server/endpoints/api/_.py](../../../../translatepy/server/endpoints/api/_.py#L121)

### Authentification

Il n'est **pas** nécessaire d'être authentifié

### Paramètres

| Nom         | Description                      | Obligatoire         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `threads_limit` | The maximum number of threads to spawn at a time to translate  | Non            | int            |
| `translators` | A comma-separated list of translators to use  | Non            | TranslatorList            |
| `dest_lang` | The language to translate to  | Oui            | Language            |
| `strict` | If the function should raise something is one of the nodes couldn't be translated.
If `False`, the node will be left as is and the `result` part will be `None`  | Non            | to_bool            |
| `source_lang` | The language `text` is in. If "auto", the translator will try to infer the language from each node in `html`  | Non            | Language            |
| `parser` | The BeautifulSoup parser to use to parse the HTML  | Non            | str            |
| `html` | The HTML you want to translate  | Oui            | str            |

### Exemple

<!-- tabs:start -->


<details>
    <summary>cURL Exemple</summary>

#### **cURL**

```bash
curl -X GET \
    --data-urlencode "threads_limit=<The maximum number of threads to spawn at a time to translate>"\
    --data-urlencode "translators=<A comma-separated list of translators to use>"\
    --data-urlencode "dest_lang=<The language to translate to>"\
    --data-urlencode "strict=<If the function should raise something is one of the nodes couldn't be translated.
If `False`, the node will be left as is and the `result` part will be `None`>"\
    --data-urlencode "source_lang=<The language `text` is in. If \"auto\", the translator will try to infer the language from each node in `html`>"\
    --data-urlencode "parser=<The BeautifulSoup parser to use to parse the HTML>"\
    --data-urlencode "html=<The HTML you want to translate>" \
    "/api/translate/html"
```

</details>


<details>
    <summary>JavaScript Exemple</summary>

#### **JavaScript**

```javascript
fetch(`/api/translate/html?dest_lang=${encodeURIComponent("dest_lang")}&html=${encodeURIComponent("html")}`, {
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
r = requests.request("GET", "/api/translate/html",
        params = {
            "dest_lang": "The language to translate to",
            "html": "The HTML you want to translate"
        })
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
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy  | 500  |
[Retourner à l'Index](../Pour%20commencer.md#index)

# stream

Streams all translations available using the different translators

```http
* /api/stream
```

> [../../../../translatepy/server/endpoints/api/_.py](../../../../translatepy/server/endpoints/api/_.py#L133)

### Authentification

Il n'est **pas** nécessaire d'être authentifié

### Paramètres

| Nom         | Description                      | Obligatoire         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `timeout` | Il n'y a pas de description  | Non            | int            |
| `translators` | Il n'y a pas de description  | Non            | TranslatorList            |
| `text` | Il n'y a pas de description  | Oui            | str            |
| `source_lang` | Il n'y a pas de description  | Non            | Language            |
| `dest_lang` | Il n'y a pas de description  | Oui            | Language            |

### Exemple

<!-- tabs:start -->


<details>
    <summary>cURL Exemple</summary>

#### **cURL**

```bash
curl -X * \
    --data-urlencode "timeout=<>"\
    --data-urlencode "translators=<>"\
    --data-urlencode "text=<>"\
    --data-urlencode "source_lang=<>"\
    --data-urlencode "dest_lang=<>" \
    "/api/stream"
```

</details>


<details>
    <summary>JavaScript Exemple</summary>

#### **JavaScript**

```javascript
fetch(`/api/stream?text=${encodeURIComponent("text")}&dest_lang=${encodeURIComponent("dest_lang")}`, {
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
r = requests.request("*", "/api/stream",
        params = {
            "text": "text",
            "dest_lang": "dest_lang"
        })
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
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy  | 500  |
[Retourner à l'Index](../Pour%20commencer.md#index)

# transliterate

Transliterates the text in the given language

```http
GET /api/transliterate
```

> [../../../../translatepy/server/endpoints/api/_.py](../../../../translatepy/server/endpoints/api/_.py#L186)

### Authentification

Il n'est **pas** nécessaire d'être authentifié

### Paramètres

| Nom         | Description                      | Obligatoire         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `dest_lang` | The language to translate to  | Oui            | Language            |
| `translators` | A comma-separated list of translators to use  | Non            | TranslatorList            |
| `text` | The text to transliterate  | Oui            | str            |
| `source_lang` | The language `text` is in. If "auto", the translator will try to infer the language from `text`  | Non            | Language            |

### Exemple

<!-- tabs:start -->


<details>
    <summary>cURL Exemple</summary>

#### **cURL**

```bash
curl -X GET \
    --data-urlencode "dest_lang=<The language to translate to>"\
    --data-urlencode "translators=<A comma-separated list of translators to use>"\
    --data-urlencode "text=<The text to transliterate>"\
    --data-urlencode "source_lang=<The language `text` is in. If \"auto\", the translator will try to infer the language from `text`>" \
    "/api/transliterate"
```

</details>


<details>
    <summary>JavaScript Exemple</summary>

#### **JavaScript**

```javascript
fetch(`/api/transliterate?dest_lang=${encodeURIComponent("dest_lang")}&text=${encodeURIComponent("text")}`, {
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
r = requests.request("GET", "/api/transliterate",
        params = {
            "dest_lang": "The language to translate to",
            "text": "The text to transliterate"
        })
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
        "source_lang": "no example",
        "dest_lang": "no example",
        "transliteration": "no example",
        "service": "no example",
        "source": "no example"
    }
}

```

#### Retourne

| Champ        | Description                      | Type   | Peut être `null`  |
| ----------   | -------------------------------- | ------ | --------- |
| `source_lang` | The source text's language  | Language      | Non      |
| `dest_lang` | The result's language  | Language      | Non      |
| `transliteration` | The transliteration result  | string      | Non      |
| `service` | The service which returned the result  | Translator      | Non      |
| `source` | The source text  | string      | Non      |

#### Erreurs possibles

| Erreur         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy  | 500  |
[Retourner à l'Index](../Pour%20commencer.md#index)

# spellcheck

Spellchecks the given text

```http
GET /api/spellcheck
```

> [../../../../translatepy/server/endpoints/api/_.py](../../../../translatepy/server/endpoints/api/_.py#L194)

### Authentification

Il n'est **pas** nécessaire d'être authentifié

### Paramètres

| Nom         | Description                      | Obligatoire         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `translators` | A comma-separated list of translators to use  | Non            | TranslatorList            |
| `text` | The text to check for spelling mistakes  | Oui            | str            |
| `source_lang` | The language `text` is in. If "auto", the translator will try to infer the language from `text`  | Non            | Language            |

### Exemple

<!-- tabs:start -->


<details>
    <summary>cURL Exemple</summary>

#### **cURL**

```bash
curl -X GET \
    --data-urlencode "translators=<A comma-separated list of translators to use>"\
    --data-urlencode "text=<The text to check for spelling mistakes>"\
    --data-urlencode "source_lang=<The language `text` is in. If \"auto\", the translator will try to infer the language from `text`>" \
    "/api/spellcheck"
```

</details>


<details>
    <summary>JavaScript Exemple</summary>

#### **JavaScript**

```javascript
fetch(`/api/spellcheck?text=${encodeURIComponent("text")}`, {
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
r = requests.request("GET", "/api/spellcheck",
        params = {
            "text": "The text to check for spelling mistakes"
        })
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
        "source_lang": "no example",
        "rich": true,
        "corrected": "no example",
        "service": "no example",
        "source": "no example"
    }
}

```

#### Retourne

| Champ        | Description                      | Type   | Peut être `null`  |
| ----------   | -------------------------------- | ------ | --------- |
| `source_lang` | The source text's language  | Language      | Non      |
| `rich` | Whether the given result features the full range of information  | bool      | Non      |
| `corrected` | The corrected text  | string      | Non      |
| `service` | The service which returned the result  | Translator      | Non      |
| `source` | The source text  | string      | Non      |

#### Erreurs possibles

| Erreur         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy  | 500  |
[Retourner à l'Index](../Pour%20commencer.md#index)

# language

Retrieves the language of the given text

```http
GET /api/language
```

> [../../../../translatepy/server/endpoints/api/_.py](../../../../translatepy/server/endpoints/api/_.py#L202)

### Authentification

Il n'est **pas** nécessaire d'être authentifié

### Paramètres

| Nom         | Description                      | Obligatoire         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `translators` | A comma-separated list of translators to use  | Non            | TranslatorList            |
| `source_lang` | Il n'y a pas de description  | Non            | Language            |
| `text` | The text to get the language for  | Oui            | str            |

### Exemple

<!-- tabs:start -->


<details>
    <summary>cURL Exemple</summary>

#### **cURL**

```bash
curl -X GET \
    --data-urlencode "translators=<A comma-separated list of translators to use>"\
    --data-urlencode "source_lang=<>"\
    --data-urlencode "text=<The text to get the language for>" \
    "/api/language"
```

</details>


<details>
    <summary>JavaScript Exemple</summary>

#### **JavaScript**

```javascript
fetch(`/api/language?text=${encodeURIComponent("text")}`, {
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
r = requests.request("GET", "/api/language",
        params = {
            "text": "The text to get the language for"
        })
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
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy  | 500  |
[Retourner à l'Index](../Pour%20commencer.md#index)

# example

Finds examples for the given text

```http
GET /api/example
```

> [../../../../translatepy/server/endpoints/api/_.py](../../../../translatepy/server/endpoints/api/_.py#L210)

### Authentification

Il n'est **pas** nécessaire d'être authentifié

### Paramètres

| Nom         | Description                      | Obligatoire         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `source_lang` | The language `text` is in. If "auto", the translator will try to infer the language from `text`  | Non            | Language            |
| `translators` | A comma-separated list of translators to use  | Non            | TranslatorList            |
| `text` | The text to get the example for  | Oui            | str            |

### Exemple

<!-- tabs:start -->


<details>
    <summary>cURL Exemple</summary>

#### **cURL**

```bash
curl -X GET \
    --data-urlencode "source_lang=<The language `text` is in. If \"auto\", the translator will try to infer the language from `text`>"\
    --data-urlencode "translators=<A comma-separated list of translators to use>"\
    --data-urlencode "text=<The text to get the example for>" \
    "/api/example"
```

</details>


<details>
    <summary>JavaScript Exemple</summary>

#### **JavaScript**

```javascript
fetch(`/api/example?text=${encodeURIComponent("text")}`, {
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
r = requests.request("GET", "/api/example",
        params = {
            "text": "The text to get the example for"
        })
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
        "positions": "no example",
        "source_lang": "no example",
        "service": "no example",
        "example": "no example",
        "reference": "no example",
        "source": "no example"
    }
}

```

#### Retourne

| Champ        | Description                      | Type   | Peut être `null`  |
| ----------   | -------------------------------- | ------ | --------- |
| `positions` | The positions of the word in the example  | list[int]      | Non      |
| `source_lang` | The source text's language  | Language      | Non      |
| `service` | The service which returned the result  | Translator      | Non      |
| `example` | The example  | string      | Non      |
| `reference` | Where the example comes from (i.e a book or a the person who said it if it's a quote)  | string      | Non      |
| `source` | The source text  | string      | Non      |

#### Erreurs possibles

| Erreur         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy  | 500  |
[Retourner à l'Index](../Pour%20commencer.md#index)

# dictionary

Retrieves meanings for the given text

```http
GET /api/dictionary
```

> [../../../../translatepy/server/endpoints/api/_.py](../../../../translatepy/server/endpoints/api/_.py#L218)

### Authentification

Il n'est **pas** nécessaire d'être authentifié

### Paramètres

| Nom         | Description                      | Obligatoire         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `translators` | A comma-separated list of translators to use  | Non            | TranslatorList            |
| `source_lang` | The language `text` is in. If "auto", the translator will try to infer the language from `text`  | Non            | Language            |
| `text` | The text to get the meaning for  | Oui            | str            |

### Exemple

<!-- tabs:start -->


<details>
    <summary>cURL Exemple</summary>

#### **cURL**

```bash
curl -X GET \
    --data-urlencode "translators=<A comma-separated list of translators to use>"\
    --data-urlencode "source_lang=<The language `text` is in. If \"auto\", the translator will try to infer the language from `text`>"\
    --data-urlencode "text=<The text to get the meaning for>" \
    "/api/dictionary"
```

</details>


<details>
    <summary>JavaScript Exemple</summary>

#### **JavaScript**

```javascript
fetch(`/api/dictionary?text=${encodeURIComponent("text")}`, {
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
r = requests.request("GET", "/api/dictionary",
        params = {
            "text": "The text to get the meaning for"
        })
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
        "source_lang": "no example",
        "rich": true,
        "service": "no example",
        "meaning": "no example",
        "source": "no example"
    }
}

```

#### Retourne

| Champ        | Description                      | Type   | Peut être `null`  |
| ----------   | -------------------------------- | ------ | --------- |
| `source_lang` | The source text's language  | Language      | Non      |
| `rich` | Whether the given result features the full range of information  | bool      | Non      |
| `service` | The service which returned the result  | Translator      | Non      |
| `meaning` | The meaning of the text  | string      | Non      |
| `source` | The source text  | string      | Non      |

#### Erreurs possibles

| Erreur         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy  | 500  |
[Retourner à l'Index](../Pour%20commencer.md#index)

# tts

Returns the speech version of the given text

```http
GET /api/tts
```

> [../../../../translatepy/server/endpoints/api/_.py](../../../../translatepy/server/endpoints/api/_.py#L226)

### Authentification

Il n'est **pas** nécessaire d'être authentifié

### Paramètres

| Nom         | Description                      | Obligatoire         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `raw` | Il n'y a pas de description  | Non            | to_bool            |
| `text` | The text to get the speech for  | Oui            | str            |
| `translators` | A comma-separated list of translators to use  | Non            | TranslatorList            |
| `source_lang` | The language `text` is in. If "auto", the translator will try to infer the language from `text`  | Non            | Language            |

### Exemple

<!-- tabs:start -->


<details>
    <summary>cURL Exemple</summary>

#### **cURL**

```bash
curl -X GET \
    --data-urlencode "raw=<>"\
    --data-urlencode "text=<The text to get the speech for>"\
    --data-urlencode "translators=<A comma-separated list of translators to use>"\
    --data-urlencode "source_lang=<The language `text` is in. If \"auto\", the translator will try to infer the language from `text`>" \
    "/api/tts"
```

</details>


<details>
    <summary>JavaScript Exemple</summary>

#### **JavaScript**

```javascript
fetch(`/api/tts?text=${encodeURIComponent("text")}`, {
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
r = requests.request("GET", "/api/tts",
        params = {
            "text": "The text to get the speech for"
        })
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
        "source_lang": "no example",
        "service": "no example",
        "extension": "no example",
        "gender": "no example",
        "result": "no example",
        "speed": 4,
        "mime_type": "no example",
        "source": "no example"
    }
}

```

#### Retourne

| Champ        | Description                      | Type   | Peut être `null`  |
| ----------   | -------------------------------- | ------ | --------- |
| `source_lang` | The source text's language  | Language      | Non      |
| `service` | The service which returned the result  | Translator      | Non      |
| `extension` | Returns the audio file extension  | Optional[str]      | Non      |
| `gender` | Gender of the 'person' saying the text  | Gender      | Non      |
| `result` | Text to speech result  | bytes      | Non      |
| `speed` | Speed of the text to speech result  | int      | Non      |
| `mime_type` | Returns the MIME type of the audio file  | Optional[str]      | Non      |
| `source` | The source text  | string      | Non      |

#### Erreurs possibles

| Erreur         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy  | 500  |
[Retourner à l'Index](../Pour%20commencer.md#index)