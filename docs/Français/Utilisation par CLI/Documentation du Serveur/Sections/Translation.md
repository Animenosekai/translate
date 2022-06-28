
# Référence de la section Translation

Ce fichier liste et explique les différents *endpoints* disponible sous la section Translation

# Translate


        Translates the given text to the given language

        i.e Good morning (en) --> おはようございます (ja)
        

```http
GET /translate
```

> [translatepy/server/translation.py](../../translatepy/server/translation.py#L45)

### Authentification

Il n'est **pas** nécessaire d'être authentifié

### Paramètres

| Nom         | Description                      | Obligatoire         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `text` | The text to translate  | Oui            | str            |
| `dest` | The destination language  | Oui            | str            |
| `source` | The source language  | Non            | str            |
| `translators` | The translator(s) to use. When providing multiple translators, the names should be comma-separated.  | Non            | TranslatorList            |
| `foreign` | Whether to include the language in foreign languages  | Non            | Bool            |

### Exemple

<!-- tabs:start -->


<details>
    <summary>cURL Exemple</summary>

#### **cURL**

```bash
curl -X GET \
    --data-urlencode "text=<The text to translate>"\
    --data-urlencode "dest=<The destination language>" \
    "/translate"
```

</details>


<details>
    <summary>JavaScript Exemple</summary>

#### **JavaScript**

```javascript
fetch(`/translate?text=${encodeURIComponent("text")}&dest=${encodeURIComponent("dest")}`, {
    method: "GET"
})
.then((response) => {response.json()})
.then((response) => {
    if (response.success) {
        console.info("Successfully requested for /translate")
        console.log(response.data)
    } else {
        console.error("An error occured while requesting for /translate, error: " + response.error)
    }
})
```

</details>


<details>
    <summary>Python Exemple</summary>

#### **Python**

```python
import requests
r = requests.request("GET", "/translate",
        params = {
            "text": "The text to translate",
            "dest": "The destination language"
        })
if r.status_code >= 400 or not r.json()["success"]:
    raise ValueError("An error occured while requesting for /translate, error: " + r.json()["error"])
print("Successfully requested for /translate")
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
        "service": "Google",
        "source": "Hello world",
        "sourceLanguage": {
            "inForeignLanguages": {},
            "extra": {
                "scope": "Individual",
                "type": "Living"
            },
            "id": "eng",
            "alpha2": "en",
            "alpha3b": "eng",
            "alpha3t": "eng",
            "alpha3": "eng",
            "name": "English"
        },
        "destinationLanguage": {
            "inForeignLanguages": {},
            "extra": {
                "scope": "Individual",
                "type": "Living"
            },
            "id": "eng",
            "alpha2": "en",
            "alpha3b": "eng",
            "alpha3t": "eng",
            "alpha3": "eng",
            "name": "English"
        },
        "result": "こんにちは世界"
    }
}

```

#### Retourne

| Champ        | Description                      | Type   | Peut être `null`  |
| ----------   | -------------------------------- | ------ | --------- |
| `service` | The translator used  | str      | Non      |
| `source` | The source text  | str      | Non      |
| `sourceLanguage` | The source language  | object      | Non      |
| `destinationLanguage` | The destination language  | object      | Non      |
| `result` | The translated text  | str      | Non      |

#### Erreurs possibles

| Erreur         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy. This is the base class for the other exceptions raised by translatepy.  | 500  |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `PARAMETER_ERROR` | When a parameter is missing or invalid  | 500  |
| `PARAMETER_TYPE_ERROR` | When a parameter is of the wrong type  | 500  |
| `PARAMETER_VALUE_ERROR` | When a parameter is of the wrong value  | 500  |
| `TRANSLATION_ERROR` | When a translation error occurs  | 500  |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
[Retourner à l'Index](../Pour%20commencer.md#index)

# Translation Stream


        Translates the given text to the given language

        i.e Good morning (en) --> おはようございます (ja)
         This endpoint returns a stream of results.

```http
GET /stream
```

> [translatepy/server/translation.py](../../translatepy/server/translation.py#L101)

### Authentification

Il n'est **pas** nécessaire d'être authentifié

### Paramètres

| Nom         | Description                      | Obligatoire         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `text` | The text to translate  | Oui            | str            |
| `dest` | The destination language  | Oui            | str            |
| `source` | The source language  | Non            | str            |
| `translators` | The translator(s) to use. When providing multiple translators, the names should be comma-separated.  | Non            | TranslatorList            |
| `foreign` | Whether to include the language in foreign languages  | Non            | Bool            |

### Exemple

<!-- tabs:start -->


<details>
    <summary>cURL Exemple</summary>

#### **cURL**

```bash
curl -X GET \
    --data-urlencode "text=<The text to translate>"\
    --data-urlencode "dest=<The destination language>" \
    "/stream"
```

</details>


<details>
    <summary>JavaScript Exemple</summary>

#### **JavaScript**

```javascript
fetch(`/stream?text=${encodeURIComponent("text")}&dest=${encodeURIComponent("dest")}`, {
    method: "GET"
})
.then((response) => {response.json()})
.then((response) => {
    if (response.success) {
        console.info("Successfully requested for /stream")
        console.log(response.data)
    } else {
        console.error("An error occured while requesting for /stream, error: " + response.error)
    }
})
```

</details>


<details>
    <summary>Python Exemple</summary>

#### **Python**

```python
import requests
r = requests.request("GET", "/stream",
        params = {
            "text": "The text to translate",
            "dest": "The destination language"
        })
if r.status_code >= 400 or not r.json()["success"]:
    raise ValueError("An error occured while requesting for /stream, error: " + r.json()["error"])
print("Successfully requested for /stream")
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
        "service": "Google",
        "source": "Hello world",
        "sourceLanguage": {
            "inForeignLanguages": {},
            "extra": {
                "scope": "Individual",
                "type": "Living"
            },
            "id": "eng",
            "alpha2": "en",
            "alpha3b": "eng",
            "alpha3t": "eng",
            "alpha3": "eng",
            "name": "English"
        },
        "destinationLanguage": {
            "inForeignLanguages": {},
            "extra": {
                "scope": "Individual",
                "type": "Living"
            },
            "id": "eng",
            "alpha2": "en",
            "alpha3b": "eng",
            "alpha3t": "eng",
            "alpha3": "eng",
            "name": "English"
        },
        "result": "こんにちは世界"
    }
}

```

#### Retourne

| Champ        | Description                      | Type   | Peut être `null`  |
| ----------   | -------------------------------- | ------ | --------- |
| `service` | The translator used  | str      | Non      |
| `source` | The source text  | str      | Non      |
| `sourceLanguage` | The source language  | object      | Non      |
| `destinationLanguage` | The destination language  | object      | Non      |
| `result` | The translated text  | str      | Non      |

#### Erreurs possibles

| Erreur         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy. This is the base class for the other exceptions raised by translatepy.  | 500  |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `PARAMETER_ERROR` | When a parameter is missing or invalid  | 500  |
| `PARAMETER_TYPE_ERROR` | When a parameter is of the wrong type  | 500  |
| `PARAMETER_VALUE_ERROR` | When a parameter is of the wrong value  | 500  |
| `TRANSLATION_ERROR` | When a translation error occurs  | 500  |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
[Retourner à l'Index](../Pour%20commencer.md#index)

# Translate HTML


        Translates the given HTML string or BeautifulSoup object to the given language

        i.e
         English: `<div class="hello"><h1>Hello</h1> everyone and <a href="/welcome">welcome</a> to <span class="w-full">my website</span></div>`
         French: `<div class="hello"><h1>Bonjour</h1>tout le monde et<a href="/welcome">Bienvenue</a>à<span class="w-full">Mon site internet</span></div>`

        Note: This method is not perfect since it is not tag/context aware. Example: `<span>Hello <strong>everyone</strong></span>` will not be understood as
        "Hello everyone" with "everyone" in bold but rather "Hello" and "everyone" separately.

        Warning: If you give a `bs4.BeautifulSoup`, `bs4.element.PageElement` or `bs4.element.Tag` input (which are mutable), they will be modified.
        If you don't want this behavior, please make sure to pass the string version of the element:
        >>> result = Translate().translate_html(str(page_element), "French")

        Parameters:
        ----------
            html : str | bs4.element.PageElement | bs4.element.Tag | bs4.BeautifulSoup
                The HTML string to be translated. This can also be an instance of BeautifulSoup's `BeautifulSoup` element, `PageElement` or `Tag` element.
            destination_language : str
                The language the HTML string needs to be translated in.
            source_language : str, default = "auto"
                The language of the HTML string.
            parser : str, default = "html.parser"
                The parser that BeautifulSoup will use to parse the HTML string.
            threads_limit : int, default = 100
                The maximum number of threads that will be spawned by translate_html
            __internal_replacement_function__ : function, default = None
                This is used internally, especially by the translatepy HTTP server to modify the translation step.

        Returns:
        --------
            BeautifulSoup:
                The result will be the same element as the input `html` parameter with the values modified if the given
                input is of bs4.BeautifulSoup, bs4.element.PageElement or bs4.element.Tag instance.
            str:
                The result will be a string in any other case.

        

```http
GET /html
```

> [translatepy/server/translation.py](../../translatepy/server/translation.py#L206)

### Authentification

Il n'est **pas** nécessaire d'être authentifié

### Paramètres

| Nom         | Description                      | Obligatoire         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `code` | The HTML snippet to translate  | Oui            | str            |
| `dest` | The destination language  | Oui            | str            |
| `source` | The source language  | Non            | str            |
| `parser` | The HTML parser to use  | Non            | str            |
| `translators` | The translator(s) to use. When providing multiple translators, the names should be comma-separated.  | Non            | TranslatorList            |
| `foreign` | Whether to include the language in foreign languages  | Non            | Bool            |

### Exemple

<!-- tabs:start -->


<details>
    <summary>cURL Exemple</summary>

#### **cURL**

```bash
curl -X GET \
    --data-urlencode "code=<The HTML snippet to translate>"\
    --data-urlencode "dest=<The destination language>" \
    "/html"
```

</details>


<details>
    <summary>JavaScript Exemple</summary>

#### **JavaScript**

```javascript
fetch(`/html?code=${encodeURIComponent("code")}&dest=${encodeURIComponent("dest")}`, {
    method: "GET"
})
.then((response) => {response.json()})
.then((response) => {
    if (response.success) {
        console.info("Successfully requested for /html")
        console.log(response.data)
    } else {
        console.error("An error occured while requesting for /html, error: " + response.error)
    }
})
```

</details>


<details>
    <summary>Python Exemple</summary>

#### **Python**

```python
import requests
r = requests.request("GET", "/html",
        params = {
            "code": "The HTML snippet to translate",
            "dest": "The destination language"
        })
if r.status_code >= 400 or not r.json()["success"]:
    raise ValueError("An error occured while requesting for /html, error: " + r.json()["error"])
print("Successfully requested for /html")
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
        "services": [
            "Google",
            "Bing"
        ],
        "source": "<div><p>Hello, how are you today</p><p>Comment allez-vous</p></div>",
        "sourceLanguage": [
            "fra",
            "eng"
        ],
        "destinationLanguage": {
            "inForeignLanguages": {},
            "extra": {
                "scope": "Individual",
                "type": "Living"
            },
            "id": "eng",
            "alpha2": "en",
            "alpha3b": "eng",
            "alpha3t": "eng",
            "alpha3": "eng",
            "name": "English"
        },
        "result": "<div><p>こんにちは、今日はお元気ですか</p><p>大丈夫</p></div>"
    }
}

```

#### Retourne

| Champ        | Description                      | Type   | Peut être `null`  |
| ----------   | -------------------------------- | ------ | --------- |
| `services` | The translators used  | array      | Non      |
| `source` | The source text  | str      | Non      |
| `sourceLanguage` | The source languages  | array      | Non      |
| `destinationLanguage` | The destination language  | object      | Non      |
| `result` | The translated text  | str      | Non      |

#### Erreurs possibles

| Erreur         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy. This is the base class for the other exceptions raised by translatepy.  | 500  |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `PARAMETER_ERROR` | When a parameter is missing or invalid  | 500  |
| `PARAMETER_TYPE_ERROR` | When a parameter is of the wrong type  | 500  |
| `PARAMETER_VALUE_ERROR` | When a parameter is of the wrong value  | 500  |
| `TRANSLATION_ERROR` | When a translation error occurs  | 500  |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
[Retourner à l'Index](../Pour%20commencer.md#index)

# Transliterate


        Transliterates the given text, get its pronunciation

        i.e おはよう --> Ohayou
        

```http
GET /transliterate
```

> [translatepy/server/translation.py](../../translatepy/server/translation.py#L284)

### Authentification

Il n'est **pas** nécessaire d'être authentifié

### Paramètres

| Nom         | Description                      | Obligatoire         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `text` | The text to transliterate  | Oui            | str            |
| `dest` | The destination language  | Non            | str            |
| `source` | The source language  | Non            | str            |
| `translators` | The translator(s) to use. When providing multiple translators, the names should be comma-separated.  | Non            | TranslatorList            |
| `foreign` | Whether to include the language in foreign languages  | Non            | Bool            |

### Exemple

<!-- tabs:start -->


<details>
    <summary>cURL Exemple</summary>

#### **cURL**

```bash
curl -X GET \
    --data-urlencode "text=<The text to transliterate>" \
    "/transliterate"
```

</details>


<details>
    <summary>JavaScript Exemple</summary>

#### **JavaScript**

```javascript
fetch(`/transliterate?text=${encodeURIComponent("text")}`, {
    method: "GET"
})
.then((response) => {response.json()})
.then((response) => {
    if (response.success) {
        console.info("Successfully requested for /transliterate")
        console.log(response.data)
    } else {
        console.error("An error occured while requesting for /transliterate, error: " + response.error)
    }
})
```

</details>


<details>
    <summary>Python Exemple</summary>

#### **Python**

```python
import requests
r = requests.request("GET", "/transliterate",
        params = {
            "text": "The text to transliterate"
        })
if r.status_code >= 400 or not r.json()["success"]:
    raise ValueError("An error occured while requesting for /transliterate, error: " + r.json()["error"])
print("Successfully requested for /transliterate")
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
        "service": "Google",
        "source": "おはよう",
        "sourceLanguage": {
            "inForeignLanguages": {},
            "extra": {
                "scope": "Individual",
                "type": "Living"
            },
            "id": "eng",
            "alpha2": "en",
            "alpha3b": "eng",
            "alpha3t": "eng",
            "alpha3": "eng",
            "name": "English"
        },
        "destinationLanguage": {
            "inForeignLanguages": {},
            "extra": {
                "scope": "Individual",
                "type": "Living"
            },
            "id": "eng",
            "alpha2": "en",
            "alpha3b": "eng",
            "alpha3t": "eng",
            "alpha3": "eng",
            "name": "English"
        },
        "result": "Ohayou"
    }
}

```

#### Retourne

| Champ        | Description                      | Type   | Peut être `null`  |
| ----------   | -------------------------------- | ------ | --------- |
| `service` | The translator used  | str      | Non      |
| `source` | The source text  | str      | Non      |
| `sourceLanguage` | The source language  | object      | Non      |
| `destinationLanguage` | The destination language  | object      | Non      |
| `result` | The transliteration  | str      | Non      |

#### Erreurs possibles

| Erreur         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy. This is the base class for the other exceptions raised by translatepy.  | 500  |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `PARAMETER_ERROR` | When a parameter is missing or invalid  | 500  |
| `PARAMETER_TYPE_ERROR` | When a parameter is of the wrong type  | 500  |
| `PARAMETER_VALUE_ERROR` | When a parameter is of the wrong value  | 500  |
| `TRANSLATION_ERROR` | When a translation error occurs  | 500  |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
[Retourner à l'Index](../Pour%20commencer.md#index)

# Spellcheck


        Checks the spelling of a given text

        i.e God morning --> Good morning
        

```http
GET /spellcheck
```

> [translatepy/server/translation.py](../../translatepy/server/translation.py#L340)

### Authentification

Il n'est **pas** nécessaire d'être authentifié

### Paramètres

| Nom         | Description                      | Obligatoire         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `text` | The text to spellcheck  | Oui            | str            |
| `source` | The source language  | Non            | str            |
| `translators` | The translator(s) to use. When providing multiple translators, the names should be comma-separated.  | Non            | TranslatorList            |
| `foreign` | Whether to include the language in foreign languages  | Non            | Bool            |

### Exemple

<!-- tabs:start -->


<details>
    <summary>cURL Exemple</summary>

#### **cURL**

```bash
curl -X GET \
    --data-urlencode "text=<The text to spellcheck>" \
    "/spellcheck"
```

</details>


<details>
    <summary>JavaScript Exemple</summary>

#### **JavaScript**

```javascript
fetch(`/spellcheck?text=${encodeURIComponent("text")}`, {
    method: "GET"
})
.then((response) => {response.json()})
.then((response) => {
    if (response.success) {
        console.info("Successfully requested for /spellcheck")
        console.log(response.data)
    } else {
        console.error("An error occured while requesting for /spellcheck, error: " + response.error)
    }
})
```

</details>


<details>
    <summary>Python Exemple</summary>

#### **Python**

```python
import requests
r = requests.request("GET", "/spellcheck",
        params = {
            "text": "The text to spellcheck"
        })
if r.status_code >= 400 or not r.json()["success"]:
    raise ValueError("An error occured while requesting for /spellcheck, error: " + r.json()["error"])
print("Successfully requested for /spellcheck")
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
        "service": "Google",
        "source": "God morning",
        "sourceLang": {
            "inForeignLanguages": {},
            "extra": {
                "scope": "Individual",
                "type": "Living"
            },
            "id": "eng",
            "alpha2": "en",
            "alpha3b": "eng",
            "alpha3t": "eng",
            "alpha3": "eng",
            "name": "English"
        },
        "result": "Good morning"
    }
}

```

#### Retourne

| Champ        | Description                      | Type   | Peut être `null`  |
| ----------   | -------------------------------- | ------ | --------- |
| `service` | The translator used  | str      | Non      |
| `source` | The source text  | str      | Non      |
| `sourceLang` | The source language  | object      | Non      |
| `result` | The spellchecked text  | str      | Non      |

#### Erreurs possibles

| Erreur         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy. This is the base class for the other exceptions raised by translatepy.  | 500  |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `PARAMETER_ERROR` | When a parameter is missing or invalid  | 500  |
| `PARAMETER_TYPE_ERROR` | When a parameter is of the wrong type  | 500  |
| `PARAMETER_VALUE_ERROR` | When a parameter is of the wrong value  | 500  |
| `TRANSLATION_ERROR` | When a translation error occurs  | 500  |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
[Retourner à l'Index](../Pour%20commencer.md#index)

# Language


        Returns the language of the given text

        i.e 皆さんおはようございます！ --> Japanese
        

```http
GET /language
```

> [translatepy/server/translation.py](../../translatepy/server/translation.py#L394)

### Authentification

Il n'est **pas** nécessaire d'être authentifié

### Paramètres

| Nom         | Description                      | Obligatoire         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `text` | The text to get the language of  | Oui            | str            |
| `translators` | The translator(s) to use. When providing multiple translators, the names should be comma-separated.  | Non            | TranslatorList            |
| `foreign` | Whether to include the language in foreign languages  | Non            | Bool            |

### Exemple

<!-- tabs:start -->


<details>
    <summary>cURL Exemple</summary>

#### **cURL**

```bash
curl -X GET \
    --data-urlencode "text=<The text to get the language of>" \
    "/language"
```

</details>


<details>
    <summary>JavaScript Exemple</summary>

#### **JavaScript**

```javascript
fetch(`/language?text=${encodeURIComponent("text")}`, {
    method: "GET"
})
.then((response) => {response.json()})
.then((response) => {
    if (response.success) {
        console.info("Successfully requested for /language")
        console.log(response.data)
    } else {
        console.error("An error occured while requesting for /language, error: " + response.error)
    }
})
```

</details>


<details>
    <summary>Python Exemple</summary>

#### **Python**

```python
import requests
r = requests.request("GET", "/language",
        params = {
            "text": "The text to get the language of"
        })
if r.status_code >= 400 or not r.json()["success"]:
    raise ValueError("An error occured while requesting for /language, error: " + r.json()["error"])
print("Successfully requested for /language")
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
        "service": "Google",
        "source": "Hello world",
        "result": {
            "inForeignLanguages": {},
            "extra": {
                "scope": "Individual",
                "type": "Living"
            },
            "id": "eng",
            "alpha2": "en",
            "alpha3b": "eng",
            "alpha3t": "eng",
            "alpha3": "eng",
            "name": "English"
        }
    }
}

```

#### Retourne

| Champ        | Description                      | Type   | Peut être `null`  |
| ----------   | -------------------------------- | ------ | --------- |
| `service` | The translator used  | str      | Non      |
| `source` | The source text  | str      | Non      |
| `result` | The resulting language alpha-3 code  | object      | Non      |

#### Erreurs possibles

| Erreur         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy. This is the base class for the other exceptions raised by translatepy.  | 500  |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `PARAMETER_ERROR` | When a parameter is missing or invalid  | 500  |
| `PARAMETER_TYPE_ERROR` | When a parameter is of the wrong type  | 500  |
| `PARAMETER_VALUE_ERROR` | When a parameter is of the wrong value  | 500  |
| `TRANSLATION_ERROR` | When a translation error occurs  | 500  |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
[Retourner à l'Index](../Pour%20commencer.md#index)

# Text to Speech


        Gives back the text to speech result for the given text

        Args:
          text: the given text
          source_language: the source language

        Returns:
            the mp3 file as bytes

        Example:
            >>> from translatepy import Translator
            >>> t = Translator()
            >>> result = t.text_to_speech("Hello, how are you?")
            >>> with open("output.mp3", "wb") as output: # open a binary (b) file to write (w)
            ...     output.write(result.result)
                    # or:
                    result.write_to_file(output)
            # Or you can just use write_to_file method:
            >>> result.write_to_file("output.mp3")
            >>> print("Output of Text to Speech is available in output.mp3!")

            # the result is an MP3 file with the text to speech output
        

```http
GET /tts
```

> [translatepy/server/translation.py](../../translatepy/server/translation.py#L434)

### Authentification

Il n'est **pas** nécessaire d'être authentifié

### Paramètres

| Nom         | Description                      | Obligatoire         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `text` | The text to convert to speech  | Oui            | str            |
| `source` | The source language  | Non            | str            |
| `speed` | The speed of the speech  | Non            | int            |
| `gender` | The gender of the speech  | Non            | str            |
| `translators` | The translator(s) to use. When providing multiple translators, the names should be comma-separated.  | Non            | TranslatorList            |

### Exemple

<!-- tabs:start -->


<details>
    <summary>cURL Exemple</summary>

#### **cURL**

```bash
curl -X GET \
    --data-urlencode "text=<The text to convert to speech>" \
    "/tts"
```

</details>


<details>
    <summary>JavaScript Exemple</summary>

#### **JavaScript**

```javascript
fetch(`/tts?text=${encodeURIComponent("text")}`, {
    method: "GET"
})
.then((response) => {response.json()})
.then((response) => {
    if (response.success) {
        console.info("Successfully requested for /tts")
        console.log(response.data)
    } else {
        console.error("An error occured while requesting for /tts, error: " + response.error)
    }
})
```

</details>


<details>
    <summary>Python Exemple</summary>

#### **Python**

```python
import requests
r = requests.request("GET", "/tts",
        params = {
            "text": "The text to convert to speech"
        })
if r.status_code >= 400 or not r.json()["success"]:
    raise ValueError("An error occured while requesting for /tts, error: " + r.json()["error"])
print("Successfully requested for /tts")
print(r.json()["data"])
```

</details>
<!-- tabs:end -->

#### Erreurs possibles

| Erreur         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy. This is the base class for the other exceptions raised by translatepy.  | 500  |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `PARAMETER_ERROR` | When a parameter is missing or invalid  | 500  |
| `PARAMETER_TYPE_ERROR` | When a parameter is of the wrong type  | 500  |
| `PARAMETER_VALUE_ERROR` | When a parameter is of the wrong value  | 500  |
| `TRANSLATION_ERROR` | When a translation error occurs  | 500  |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
[Retourner à l'Index](../Pour%20commencer.md#index)