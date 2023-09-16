
# Work セクションのAPIリファレンス

このファイルは「Work」セクションの全てのエンドポイントを説明します。

# translate

Translates the text in the given language

```http
GET /api/translate
```

> [../../../../translatepy/server/endpoints/api/_.py](../../../../translatepy/server/endpoints/api/_.py#L113)

### 認証

ログインは**不要**です

### パラメーター

| 名前         | 詳細                      | 必要         | タイプ             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `dest_lang` | The language to translate to  | はい            | Language            |
| `translators` | A comma-separated list of translators to use  | いいえ            | TranslatorList            |
| `text` | The text to translate  | はい            | str            |
| `source_lang` | The language `text` is in. If "auto", the translator will try to infer the language from `text`  | いいえ            | Language            |

### 例

<!-- tabs:start -->


<details>
    <summary>cURL 例</summary>

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
    <summary>JavaScript 例</summary>

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
    <summary>Python 例</summary>

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

### レスポンス

#### レスポンスの例

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

#### 返したフィールド

| フィールド        | 詳細                      | タイプ   | null可能  |
| ----------   | -------------------------------- | ------ | --------- |
| `source_lang` | The source text's language  | Language      | いいえ      |
| `dest_lang` | The result's language  | Language      | いいえ      |
| `service` | The service which returned the result  | Translator      | いいえ      |
| `translation` | The translation result  | string      | いいえ      |
| `source` | The source text  | string      | いいえ      |

#### 起こりうるエラー

| エラー名         | 詳細                      | コード   |
| ---------------   | -------------------------------- | ------ |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy  | 500  |
[インデックスに戻る](../%E3%81%AF%E3%81%98%E3%82%81%E3%81%AB.md#インデックス)

# translate_html

Translates the HTML in the given language

```http
GET /api/translate/html
```

> [../../../../translatepy/server/endpoints/api/_.py](../../../../translatepy/server/endpoints/api/_.py#L121)

### 認証

ログインは**不要**です

### パラメーター

| 名前         | 詳細                      | 必要         | タイプ             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `threads_limit` | The maximum number of threads to spawn at a time to translate  | いいえ            | int            |
| `translators` | A comma-separated list of translators to use  | いいえ            | TranslatorList            |
| `dest_lang` | The language to translate to  | はい            | Language            |
| `strict` | If the function should raise something is one of the nodes couldn't be translated.
If `False`, the node will be left as is and the `result` part will be `None`  | いいえ            | to_bool            |
| `source_lang` | The language `text` is in. If "auto", the translator will try to infer the language from each node in `html`  | いいえ            | Language            |
| `parser` | The BeautifulSoup parser to use to parse the HTML  | いいえ            | str            |
| `html` | The HTML you want to translate  | はい            | str            |

### 例

<!-- tabs:start -->


<details>
    <summary>cURL 例</summary>

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
    <summary>JavaScript 例</summary>

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
    <summary>Python 例</summary>

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

### レスポンス

#### レスポンスの例

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

#### 返したフィールド

| フィールド        | 詳細                      | タイプ   | null可能  |
| ----------   | -------------------------------- | ------ | --------- |
| `service` | The service which returned the result  | Translator      | いいえ      |
| `source_lang` | The source text's language  | Language      | いいえ      |
| `source` | The source text  | string      | いいえ      |

#### 起こりうるエラー

| エラー名         | 詳細                      | コード   |
| ---------------   | -------------------------------- | ------ |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy  | 500  |
[インデックスに戻る](../%E3%81%AF%E3%81%98%E3%82%81%E3%81%AB.md#インデックス)

# stream

Streams all translations available using the different translators

```http
* /api/stream
```

> [../../../../translatepy/server/endpoints/api/_.py](../../../../translatepy/server/endpoints/api/_.py#L133)

### 認証

ログインは**不要**です

### パラメーター

| 名前         | 詳細                      | 必要         | タイプ             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `timeout` | 詳細なし  | いいえ            | int            |
| `translators` | 詳細なし  | いいえ            | TranslatorList            |
| `text` | 詳細なし  | はい            | str            |
| `source_lang` | 詳細なし  | いいえ            | Language            |
| `dest_lang` | 詳細なし  | はい            | Language            |

### 例

<!-- tabs:start -->


<details>
    <summary>cURL 例</summary>

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
    <summary>JavaScript 例</summary>

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
    <summary>Python 例</summary>

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

#### 起こりうるエラー

| エラー名         | 詳細                      | コード   |
| ---------------   | -------------------------------- | ------ |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy  | 500  |
[インデックスに戻る](../%E3%81%AF%E3%81%98%E3%82%81%E3%81%AB.md#インデックス)

# transliterate

Transliterates the text in the given language

```http
GET /api/transliterate
```

> [../../../../translatepy/server/endpoints/api/_.py](../../../../translatepy/server/endpoints/api/_.py#L186)

### 認証

ログインは**不要**です

### パラメーター

| 名前         | 詳細                      | 必要         | タイプ             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `dest_lang` | The language to translate to  | はい            | Language            |
| `translators` | A comma-separated list of translators to use  | いいえ            | TranslatorList            |
| `text` | The text to transliterate  | はい            | str            |
| `source_lang` | The language `text` is in. If "auto", the translator will try to infer the language from `text`  | いいえ            | Language            |

### 例

<!-- tabs:start -->


<details>
    <summary>cURL 例</summary>

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
    <summary>JavaScript 例</summary>

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
    <summary>Python 例</summary>

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

### レスポンス

#### レスポンスの例

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

#### 返したフィールド

| フィールド        | 詳細                      | タイプ   | null可能  |
| ----------   | -------------------------------- | ------ | --------- |
| `source_lang` | The source text's language  | Language      | いいえ      |
| `dest_lang` | The result's language  | Language      | いいえ      |
| `transliteration` | The transliteration result  | string      | いいえ      |
| `service` | The service which returned the result  | Translator      | いいえ      |
| `source` | The source text  | string      | いいえ      |

#### 起こりうるエラー

| エラー名         | 詳細                      | コード   |
| ---------------   | -------------------------------- | ------ |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy  | 500  |
[インデックスに戻る](../%E3%81%AF%E3%81%98%E3%82%81%E3%81%AB.md#インデックス)

# spellcheck

Spellchecks the given text

```http
GET /api/spellcheck
```

> [../../../../translatepy/server/endpoints/api/_.py](../../../../translatepy/server/endpoints/api/_.py#L194)

### 認証

ログインは**不要**です

### パラメーター

| 名前         | 詳細                      | 必要         | タイプ             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `translators` | A comma-separated list of translators to use  | いいえ            | TranslatorList            |
| `text` | The text to check for spelling mistakes  | はい            | str            |
| `source_lang` | The language `text` is in. If "auto", the translator will try to infer the language from `text`  | いいえ            | Language            |

### 例

<!-- tabs:start -->


<details>
    <summary>cURL 例</summary>

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
    <summary>JavaScript 例</summary>

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
    <summary>Python 例</summary>

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

### レスポンス

#### レスポンスの例

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

#### 返したフィールド

| フィールド        | 詳細                      | タイプ   | null可能  |
| ----------   | -------------------------------- | ------ | --------- |
| `source_lang` | The source text's language  | Language      | いいえ      |
| `rich` | Whether the given result features the full range of information  | bool      | いいえ      |
| `corrected` | The corrected text  | string      | いいえ      |
| `service` | The service which returned the result  | Translator      | いいえ      |
| `source` | The source text  | string      | いいえ      |

#### 起こりうるエラー

| エラー名         | 詳細                      | コード   |
| ---------------   | -------------------------------- | ------ |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy  | 500  |
[インデックスに戻る](../%E3%81%AF%E3%81%98%E3%82%81%E3%81%AB.md#インデックス)

# language

Retrieves the language of the given text

```http
GET /api/language
```

> [../../../../translatepy/server/endpoints/api/_.py](../../../../translatepy/server/endpoints/api/_.py#L202)

### 認証

ログインは**不要**です

### パラメーター

| 名前         | 詳細                      | 必要         | タイプ             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `translators` | A comma-separated list of translators to use  | いいえ            | TranslatorList            |
| `source_lang` | 詳細なし  | いいえ            | Language            |
| `text` | The text to get the language for  | はい            | str            |

### 例

<!-- tabs:start -->


<details>
    <summary>cURL 例</summary>

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
    <summary>JavaScript 例</summary>

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
    <summary>Python 例</summary>

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

### レスポンス

#### レスポンスの例

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

#### 返したフィールド

| フィールド        | 詳細                      | タイプ   | null可能  |
| ----------   | -------------------------------- | ------ | --------- |
| `service` | The service which returned the result  | Translator      | いいえ      |
| `source_lang` | The source text's language  | Language      | いいえ      |
| `source` | The source text  | string      | いいえ      |

#### 起こりうるエラー

| エラー名         | 詳細                      | コード   |
| ---------------   | -------------------------------- | ------ |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy  | 500  |
[インデックスに戻る](../%E3%81%AF%E3%81%98%E3%82%81%E3%81%AB.md#インデックス)

# example

Finds examples for the given text

```http
GET /api/example
```

> [../../../../translatepy/server/endpoints/api/_.py](../../../../translatepy/server/endpoints/api/_.py#L210)

### 認証

ログインは**不要**です

### パラメーター

| 名前         | 詳細                      | 必要         | タイプ             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `source_lang` | The language `text` is in. If "auto", the translator will try to infer the language from `text`  | いいえ            | Language            |
| `translators` | A comma-separated list of translators to use  | いいえ            | TranslatorList            |
| `text` | The text to get the example for  | はい            | str            |

### 例

<!-- tabs:start -->


<details>
    <summary>cURL 例</summary>

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
    <summary>JavaScript 例</summary>

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
    <summary>Python 例</summary>

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

### レスポンス

#### レスポンスの例

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

#### 返したフィールド

| フィールド        | 詳細                      | タイプ   | null可能  |
| ----------   | -------------------------------- | ------ | --------- |
| `positions` | The positions of the word in the example  | list[int]      | いいえ      |
| `source_lang` | The source text's language  | Language      | いいえ      |
| `service` | The service which returned the result  | Translator      | いいえ      |
| `example` | The example  | string      | いいえ      |
| `reference` | Where the example comes from (i.e a book or a the person who said it if it's a quote)  | string      | いいえ      |
| `source` | The source text  | string      | いいえ      |

#### 起こりうるエラー

| エラー名         | 詳細                      | コード   |
| ---------------   | -------------------------------- | ------ |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy  | 500  |
[インデックスに戻る](../%E3%81%AF%E3%81%98%E3%82%81%E3%81%AB.md#インデックス)

# dictionary

Retrieves meanings for the given text

```http
GET /api/dictionary
```

> [../../../../translatepy/server/endpoints/api/_.py](../../../../translatepy/server/endpoints/api/_.py#L218)

### 認証

ログインは**不要**です

### パラメーター

| 名前         | 詳細                      | 必要         | タイプ             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `translators` | A comma-separated list of translators to use  | いいえ            | TranslatorList            |
| `source_lang` | The language `text` is in. If "auto", the translator will try to infer the language from `text`  | いいえ            | Language            |
| `text` | The text to get the meaning for  | はい            | str            |

### 例

<!-- tabs:start -->


<details>
    <summary>cURL 例</summary>

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
    <summary>JavaScript 例</summary>

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
    <summary>Python 例</summary>

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

### レスポンス

#### レスポンスの例

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

#### 返したフィールド

| フィールド        | 詳細                      | タイプ   | null可能  |
| ----------   | -------------------------------- | ------ | --------- |
| `source_lang` | The source text's language  | Language      | いいえ      |
| `rich` | Whether the given result features the full range of information  | bool      | いいえ      |
| `service` | The service which returned the result  | Translator      | いいえ      |
| `meaning` | The meaning of the text  | string      | いいえ      |
| `source` | The source text  | string      | いいえ      |

#### 起こりうるエラー

| エラー名         | 詳細                      | コード   |
| ---------------   | -------------------------------- | ------ |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy  | 500  |
[インデックスに戻る](../%E3%81%AF%E3%81%98%E3%82%81%E3%81%AB.md#インデックス)

# tts

Returns the speech version of the given text

```http
GET /api/tts
```

> [../../../../translatepy/server/endpoints/api/_.py](../../../../translatepy/server/endpoints/api/_.py#L226)

### 認証

ログインは**不要**です

### パラメーター

| 名前         | 詳細                      | 必要         | タイプ             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `raw` | 詳細なし  | いいえ            | to_bool            |
| `text` | The text to get the speech for  | はい            | str            |
| `translators` | A comma-separated list of translators to use  | いいえ            | TranslatorList            |
| `source_lang` | The language `text` is in. If "auto", the translator will try to infer the language from `text`  | いいえ            | Language            |

### 例

<!-- tabs:start -->


<details>
    <summary>cURL 例</summary>

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
    <summary>JavaScript 例</summary>

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
    <summary>Python 例</summary>

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

### レスポンス

#### レスポンスの例

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

#### 返したフィールド

| フィールド        | 詳細                      | タイプ   | null可能  |
| ----------   | -------------------------------- | ------ | --------- |
| `source_lang` | The source text's language  | Language      | いいえ      |
| `service` | The service which returned the result  | Translator      | いいえ      |
| `extension` | Returns the audio file extension  | Optional[str]      | いいえ      |
| `gender` | Gender of the 'person' saying the text  | Gender      | いいえ      |
| `result` | Text to speech result  | bytes      | いいえ      |
| `speed` | Speed of the text to speech result  | int      | いいえ      |
| `mime_type` | Returns the MIME type of the audio file  | Optional[str]      | いいえ      |
| `source` | The source text  | string      | いいえ      |

#### 起こりうるエラー

| エラー名         | 詳細                      | コード   |
| ---------------   | -------------------------------- | ------ |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy  | 500  |
[インデックスに戻る](../%E3%81%AF%E3%81%98%E3%82%81%E3%81%AB.md#インデックス)