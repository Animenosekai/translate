
# Work セクションのAPIリファレンス

このファイルは「Work」セクションの全てのエンドポイントを説明します。

# translate

Translates the text in the given language

```http
GET /api/translate
```

> [../../../../endpoints/api/_.py](../../../../endpoints/api/_.py#L113)

### 認証

ログインは**不要**です

### パラメーター

| 名前         | 詳細                      | 必要         | タイプ             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `translators` | A comma-separated list of translators to use  | いいえ            | TranslatorList            |

### 例

<!-- tabs:start -->


<details>
    <summary>cURL 例</summary>

#### **cURL**

```bash
curl -X GET \
    --data-urlencode "translators=<A comma-separated list of translators to use>" \
    "/api/translate"
```

</details>


<details>
    <summary>JavaScript 例</summary>

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
    <summary>Python 例</summary>

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
        "dest_lang": "no example",
        "source": "no example",
        "translation": "no example"
    }
}

```

#### 返したフィールド

| フィールド        | 詳細                      | タイプ   | null可能  |
| ----------   | -------------------------------- | ------ | --------- |
| `source_lang` | The source text's language  | Language      | いいえ      |
| `service` | The service which returned the result  | Translator      | いいえ      |
| `dest_lang` | The result's language  | Language      | いいえ      |
| `source` | The source text  | string      | いいえ      |
| `translation` | The translation result  | string      | いいえ      |

#### 起こりうるエラー

| エラー名         | 詳細                      | コード   |
| ---------------   | -------------------------------- | ------ |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy  | 500  |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
[インデックスに戻る](../%E3%81%AF%E3%81%98%E3%82%81%E3%81%AB.md#インデックス)

# translate_html

Translates the HTML in the given language

```http
GET /api/translate/html
```

> [../../../../endpoints/api/_.py](../../../../endpoints/api/_.py#L121)

### 認証

ログインは**不要**です

### パラメーター

| 名前         | 詳細                      | 必要         | タイプ             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `translators` | A comma-separated list of translators to use  | いいえ            | TranslatorList            |

### 例

<!-- tabs:start -->


<details>
    <summary>cURL 例</summary>

#### **cURL**

```bash
curl -X GET \
    --data-urlencode "translators=<A comma-separated list of translators to use>" \
    "/api/translate/html"
```

</details>


<details>
    <summary>JavaScript 例</summary>

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
    <summary>Python 例</summary>

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

### レスポンス

#### レスポンスの例

```json
{
    "success": true,
    "message": "Successfully processed your request",
    "error": null,
    "data": {
        "source_lang": "no example",
        "source": "no example",
        "service": "no example"
    }
}

```

#### 返したフィールド

| フィールド        | 詳細                      | タイプ   | null可能  |
| ----------   | -------------------------------- | ------ | --------- |
| `source_lang` | The source text's language  | Language      | いいえ      |
| `source` | The source text  | string      | いいえ      |
| `service` | The service which returned the result  | Translator      | いいえ      |

#### 起こりうるエラー

| エラー名         | 詳細                      | コード   |
| ---------------   | -------------------------------- | ------ |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy  | 500  |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
[インデックスに戻る](../%E3%81%AF%E3%81%98%E3%82%81%E3%81%AB.md#インデックス)

# stream

Streams all translations available using the different translators

```http
* /api/stream
```

> [../../../../endpoints/api/_.py](../../../../endpoints/api/_.py#L133)

### 認証

ログインは**不要**です

### 例

<!-- tabs:start -->


<details>
    <summary>cURL 例</summary>

#### **cURL**

```bash
curl -X * "/api/stream"
```

</details>


<details>
    <summary>JavaScript 例</summary>

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
    <summary>Python 例</summary>

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

#### 起こりうるエラー

| エラー名         | 詳細                      | コード   |
| ---------------   | -------------------------------- | ------ |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy  | 500  |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
[インデックスに戻る](../%E3%81%AF%E3%81%98%E3%82%81%E3%81%AB.md#インデックス)

# transliterate

Transliterates the text in the given language

```http
GET /api/transliterate
```

> [../../../../endpoints/api/_.py](../../../../endpoints/api/_.py#L186)

### 認証

ログインは**不要**です

### パラメーター

| 名前         | 詳細                      | 必要         | タイプ             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `translators` | A comma-separated list of translators to use  | いいえ            | TranslatorList            |

### 例

<!-- tabs:start -->


<details>
    <summary>cURL 例</summary>

#### **cURL**

```bash
curl -X GET \
    --data-urlencode "translators=<A comma-separated list of translators to use>" \
    "/api/transliterate"
```

</details>


<details>
    <summary>JavaScript 例</summary>

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
    <summary>Python 例</summary>

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
        "source": "no example",
        "service": "no example",
        "transliteration": "no example"
    }
}

```

#### 返したフィールド

| フィールド        | 詳細                      | タイプ   | null可能  |
| ----------   | -------------------------------- | ------ | --------- |
| `source_lang` | The source text's language  | Language      | いいえ      |
| `dest_lang` | The result's language  | Language      | いいえ      |
| `source` | The source text  | string      | いいえ      |
| `service` | The service which returned the result  | Translator      | いいえ      |
| `transliteration` | The transliteration result  | string      | いいえ      |

#### 起こりうるエラー

| エラー名         | 詳細                      | コード   |
| ---------------   | -------------------------------- | ------ |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy  | 500  |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
[インデックスに戻る](../%E3%81%AF%E3%81%98%E3%82%81%E3%81%AB.md#インデックス)

# spellcheck

Spellchecks the given text

```http
GET /api/spellcheck
```

> [../../../../endpoints/api/_.py](../../../../endpoints/api/_.py#L194)

### 認証

ログインは**不要**です

### パラメーター

| 名前         | 詳細                      | 必要         | タイプ             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `translators` | A comma-separated list of translators to use  | いいえ            | TranslatorList            |

### 例

<!-- tabs:start -->


<details>
    <summary>cURL 例</summary>

#### **cURL**

```bash
curl -X GET \
    --data-urlencode "translators=<A comma-separated list of translators to use>" \
    "/api/spellcheck"
```

</details>


<details>
    <summary>JavaScript 例</summary>

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
    <summary>Python 例</summary>

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
        "source": "no example",
        "service": "no example",
        "corrected": "no example"
    }
}

```

#### 返したフィールド

| フィールド        | 詳細                      | タイプ   | null可能  |
| ----------   | -------------------------------- | ------ | --------- |
| `source_lang` | The source text's language  | Language      | いいえ      |
| `rich` | Whether the given result features the full range of information  | bool      | いいえ      |
| `source` | The source text  | string      | いいえ      |
| `service` | The service which returned the result  | Translator      | いいえ      |
| `corrected` | The corrected text  | string      | いいえ      |

#### 起こりうるエラー

| エラー名         | 詳細                      | コード   |
| ---------------   | -------------------------------- | ------ |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy  | 500  |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
[インデックスに戻る](../%E3%81%AF%E3%81%98%E3%82%81%E3%81%AB.md#インデックス)

# language

Retrieves the language of the given text

```http
GET /api/language
```

> [../../../../endpoints/api/_.py](../../../../endpoints/api/_.py#L202)

### 認証

ログインは**不要**です

### パラメーター

| 名前         | 詳細                      | 必要         | タイプ             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `translators` | A comma-separated list of translators to use  | いいえ            | TranslatorList            |

### 例

<!-- tabs:start -->


<details>
    <summary>cURL 例</summary>

#### **cURL**

```bash
curl -X GET \
    --data-urlencode "translators=<A comma-separated list of translators to use>" \
    "/api/language"
```

</details>


<details>
    <summary>JavaScript 例</summary>

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
    <summary>Python 例</summary>

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

### レスポンス

#### レスポンスの例

```json
{
    "success": true,
    "message": "Successfully processed your request",
    "error": null,
    "data": {
        "source_lang": "no example",
        "source": "no example",
        "service": "no example"
    }
}

```

#### 返したフィールド

| フィールド        | 詳細                      | タイプ   | null可能  |
| ----------   | -------------------------------- | ------ | --------- |
| `source_lang` | The source text's language  | Language      | いいえ      |
| `source` | The source text  | string      | いいえ      |
| `service` | The service which returned the result  | Translator      | いいえ      |

#### 起こりうるエラー

| エラー名         | 詳細                      | コード   |
| ---------------   | -------------------------------- | ------ |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy  | 500  |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
[インデックスに戻る](../%E3%81%AF%E3%81%98%E3%82%81%E3%81%AB.md#インデックス)

# example

Finds examples for the given text

```http
GET /api/example
```

> [../../../../endpoints/api/_.py](../../../../endpoints/api/_.py#L210)

### 認証

ログインは**不要**です

### パラメーター

| 名前         | 詳細                      | 必要         | タイプ             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `translators` | A comma-separated list of translators to use  | いいえ            | TranslatorList            |

### 例

<!-- tabs:start -->


<details>
    <summary>cURL 例</summary>

#### **cURL**

```bash
curl -X GET \
    --data-urlencode "translators=<A comma-separated list of translators to use>" \
    "/api/example"
```

</details>


<details>
    <summary>JavaScript 例</summary>

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
    <summary>Python 例</summary>

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

### レスポンス

#### レスポンスの例

```json
{
    "success": true,
    "message": "Successfully processed your request",
    "error": null,
    "data": {
        "reference": "no example",
        "example": "no example",
        "source_lang": "no example",
        "positions": "no example",
        "source": "no example",
        "service": "no example"
    }
}

```

#### 返したフィールド

| フィールド        | 詳細                      | タイプ   | null可能  |
| ----------   | -------------------------------- | ------ | --------- |
| `reference` | Where the example comes from (i.e a book or a the person who said it if it's a quote)  | string      | いいえ      |
| `example` | The example  | string      | いいえ      |
| `source_lang` | The source text's language  | Language      | いいえ      |
| `positions` | The positions of the word in the example  | list[int]      | いいえ      |
| `source` | The source text  | string      | いいえ      |
| `service` | The service which returned the result  | Translator      | いいえ      |

#### 起こりうるエラー

| エラー名         | 詳細                      | コード   |
| ---------------   | -------------------------------- | ------ |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy  | 500  |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
[インデックスに戻る](../%E3%81%AF%E3%81%98%E3%82%81%E3%81%AB.md#インデックス)

# dictionary

Retrieves meanings for the given text

```http
GET /api/dictionary
```

> [../../../../endpoints/api/_.py](../../../../endpoints/api/_.py#L218)

### 認証

ログインは**不要**です

### パラメーター

| 名前         | 詳細                      | 必要         | タイプ             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `translators` | A comma-separated list of translators to use  | いいえ            | TranslatorList            |

### 例

<!-- tabs:start -->


<details>
    <summary>cURL 例</summary>

#### **cURL**

```bash
curl -X GET \
    --data-urlencode "translators=<A comma-separated list of translators to use>" \
    "/api/dictionary"
```

</details>


<details>
    <summary>JavaScript 例</summary>

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
    <summary>Python 例</summary>

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

### レスポンス

#### レスポンスの例

```json
{
    "success": true,
    "message": "Successfully processed your request",
    "error": null,
    "data": {
        "source_lang": "no example",
        "meaning": "no example",
        "rich": true,
        "source": "no example",
        "service": "no example"
    }
}

```

#### 返したフィールド

| フィールド        | 詳細                      | タイプ   | null可能  |
| ----------   | -------------------------------- | ------ | --------- |
| `source_lang` | The source text's language  | Language      | いいえ      |
| `meaning` | The meaning of the text  | string      | いいえ      |
| `rich` | Whether the given result features the full range of information  | bool      | いいえ      |
| `source` | The source text  | string      | いいえ      |
| `service` | The service which returned the result  | Translator      | いいえ      |

#### 起こりうるエラー

| エラー名         | 詳細                      | コード   |
| ---------------   | -------------------------------- | ------ |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy  | 500  |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
[インデックスに戻る](../%E3%81%AF%E3%81%98%E3%82%81%E3%81%AB.md#インデックス)

# tts

Returns the speech version of the given text

```http
GET /api/tts
```

> [../../../../endpoints/api/_.py](../../../../endpoints/api/_.py#L226)

### 認証

ログインは**不要**です

### パラメーター

| 名前         | 詳細                      | 必要         | タイプ             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `translators` | A comma-separated list of translators to use  | いいえ            | TranslatorList            |

### 例

<!-- tabs:start -->


<details>
    <summary>cURL 例</summary>

#### **cURL**

```bash
curl -X GET \
    --data-urlencode "translators=<A comma-separated list of translators to use>" \
    "/api/tts"
```

</details>


<details>
    <summary>JavaScript 例</summary>

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
    <summary>Python 例</summary>

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

### レスポンス

#### レスポンスの例

```json
{
    "success": true,
    "message": "Successfully processed your request",
    "error": null,
    "data": {
        "source_lang": "no example",
        "extension": "no example",
        "result": "no example",
        "source": "no example",
        "service": "no example",
        "gender": "no example",
        "mime_type": "no example",
        "speed": 4
    }
}

```

#### 返したフィールド

| フィールド        | 詳細                      | タイプ   | null可能  |
| ----------   | -------------------------------- | ------ | --------- |
| `source_lang` | The source text's language  | Language      | いいえ      |
| `extension` | Returns the audio file extension  | Optional[str]      | いいえ      |
| `result` | Text to speech result  | bytes      | いいえ      |
| `source` | The source text  | string      | いいえ      |
| `service` | The service which returned the result  | Translator      | いいえ      |
| `gender` | Gender of the 'person' saying the text  | Gender      | いいえ      |
| `mime_type` | Returns the MIME type of the audio file  | Optional[str]      | いいえ      |
| `speed` | Speed of the text to speech result  | int      | いいえ      |

#### 起こりうるエラー

| エラー名         | 詳細                      | コード   |
| ---------------   | -------------------------------- | ------ |
| `NO_RESULT` | When no result is returned from the translator(s)  | 500  |
| `UNKNOWN_TRANSLATOR` | When one of the provided translator/service could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy  | 500  |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
[インデックスに戻る](../%E3%81%AF%E3%81%98%E3%82%81%E3%81%AB.md#インデックス)