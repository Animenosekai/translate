
# Language セクションのAPIリファレンス

このファイルは「Language」セクションの全てのエンドポイントを説明します。

# Language Details

Retrieving details about the given language

```http
GET /language/details
```

> [translatepy/server/language.py](../../translatepy/server/language.py#L113)

### 認証

ログインは**不要**です

### パラメーター

| 名前         | 詳細                      | 必要         | タイプ             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `lang` | The language to lookup  | はい            | str            |
| `threshold` | The similarity threshold to use when searching for similar languages  | いいえ            | float            |
| `foreign` | Whether to include the language in foreign languages  | いいえ            | Bool            |

### 例

<!-- tabs:start -->


<details>
    <summary>cURL 例</summary>

#### **cURL**

```bash
curl -X GET \
    --data-urlencode "lang=<The language to lookup>" \
    "/language/details"
```

</details>


<details>
    <summary>JavaScript 例</summary>

#### **JavaScript**

```javascript
fetch(`/language/details?lang=${encodeURIComponent("lang")}`, {
    method: "GET"
})
.then((response) => {response.json()})
.then((response) => {
    if (response.success) {
        console.info("Successfully requested for /language/details")
        console.log(response.data)
    } else {
        console.error("An error occured while requesting for /language/details, error: " + response.error)
    }
})
```

</details>


<details>
    <summary>Python 例</summary>

#### **Python**

```python
import requests
r = requests.request("GET", "/language/details",
        params = {
            "lang": "The language to lookup"
        })
if r.status_code >= 400 or not r.json()["success"]:
    raise ValueError("An error occured while requesting for /language/details, error: " + r.json()["error"])
print("Successfully requested for /language/details")
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
        "id": "eng",
        "alpha2": "en",
        "alpha3b": "eng",
        "alpha3t": "eng",
        "alpha3": "eng",
        "name": "English",
        "inForeignLanguages": {},
        "extra": {
            "scope": "Individual",
            "type": "Living"
        }
    }
}

```

#### 返したフィールド

| フィールド        | 詳細                      | タイプ   | null可能  |
| ----------   | -------------------------------- | ------ | --------- |
| `id` | The language id  | str      | いいえ      |
| `alpha2` | The language alpha2 code  | str      | いいえ      |
| `alpha3b` | The language alpha3b code  | str      | いいえ      |
| `alpha3t` | The language alpha3t code  | str      | いいえ      |
| `alpha3` | The language alpha3 code  | str      | いいえ      |
| `name` | The language name  | str      | いいえ      |
| `inForeignLanguages` | The language in foreign languages  | object      | いいえ      |
| `extra` | The language extra data  | object      | いいえ      |

#### 起こりうるエラー

| エラー名         | 詳細                      | コード   |
| ---------------   | -------------------------------- | ------ |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy. This is the base class for the other exceptions raised by translatepy.  | 500  |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
[インデックスに戻る](../%E3%81%AF%E3%81%98%E3%82%81%E3%81%AB.md#インデックス)

# Language Search

Searching for a language

```http
GET /language/search
```

> [translatepy/server/language.py](../../translatepy/server/language.py#L135)

### 認証

ログインは**不要**です

### パラメーター

| 名前         | 詳細                      | 必要         | タイプ             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `lang` | The language to lookup  | はい            | str            |
| `limit` | The limit of languages to return. (max: 100, default: 10)  | いいえ            | int            |
| `foreign` | Whether to include the language in foreign languages  | いいえ            | Bool            |

### 例

<!-- tabs:start -->


<details>
    <summary>cURL 例</summary>

#### **cURL**

```bash
curl -X GET \
    --data-urlencode "lang=<The language to lookup>" \
    "/language/search"
```

</details>


<details>
    <summary>JavaScript 例</summary>

#### **JavaScript**

```javascript
fetch(`/language/search?lang=${encodeURIComponent("lang")}`, {
    method: "GET"
})
.then((response) => {response.json()})
.then((response) => {
    if (response.success) {
        console.info("Successfully requested for /language/search")
        console.log(response.data)
    } else {
        console.error("An error occured while requesting for /language/search, error: " + response.error)
    }
})
```

</details>


<details>
    <summary>Python 例</summary>

#### **Python**

```python
import requests
r = requests.request("GET", "/language/search",
        params = {
            "lang": "The language to lookup"
        })
if r.status_code >= 400 or not r.json()["success"]:
    raise ValueError("An error occured while requesting for /language/search, error: " + r.json()["error"])
print("Successfully requested for /language/search")
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
        "languages": [
            {
                "string": "English",
                "similarity": 100,
                "language": {
                    "id": "eng",
                    "similarity": 100,
                    "alpha2": "en",
                    "alpha3b": "eng",
                    "alpha3t": "eng",
                    "alpha3": "eng",
                    "name": "English",
                    "inForeignLanguages": {
                        "af": "Engels",
                        "sq": "Anglisht",
                        "am": "እንግሊዝኛ",
                        "ar": "الإنجليزية",
                        "hy": "Անգլերեն",
                        "...": "...",
                        "zh": "英语",
                        "he": "אנגלית",
                        "jv": "Inggris",
                        "en": "English"
                    },
                    "extra": {
                        "type": "Living",
                        "scope": "Individual"
                    }
                }
            }
        ]
    }
}

```

#### 返したフィールド

| フィールド        | 詳細                      | タイプ   | null可能  |
| ----------   | -------------------------------- | ------ | --------- |
| `languages` | The languages found  | array      | いいえ      |

#### 起こりうるエラー

| エラー名         | 詳細                      | コード   |
| ---------------   | -------------------------------- | ------ |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy. This is the base class for the other exceptions raised by translatepy.  | 500  |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
[インデックスに戻る](../%E3%81%AF%E3%81%98%E3%82%81%E3%81%AB.md#インデックス)

# Language Details (dynamic)

Retrieving details about the given language

```http
GET /language/details/<language>
```

> [translatepy/server/language.py](../../translatepy/server/language.py#L184)

### 認証

ログインは**不要**です

### パラメーター

| 名前         | 詳細                      | 必要         | タイプ             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `threshold` | The similarity threshold to use when searching for similar languages  | いいえ            | float            |
| `foreign` | Whether to include the language in foreign languages  | いいえ            | Bool            |

### ダイナミックURL

| 名前         | 詳細                      | 必要         | タイプ             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `language` | The language to lookup  | はい            | str            |

### 例

<!-- tabs:start -->


<details>
    <summary>cURL 例</summary>

#### **cURL**

```bash
curl -X GET "/language/details/<language>"
```

</details>


<details>
    <summary>JavaScript 例</summary>

#### **JavaScript**

```javascript
fetch("/language/details/<language>", {
    method: "GET"
})
.then((response) => {response.json()})
.then((response) => {
    if (response.success) {
        console.info("Successfully requested for /language/details/<language>")
        console.log(response.data)
    } else {
        console.error("An error occured while requesting for /language/details/<language>, error: " + response.error)
    }
})
```

</details>


<details>
    <summary>Python 例</summary>

#### **Python**

```python
import requests
r = requests.request("GET", "/language/details/<language>")
if r.status_code >= 400 or not r.json()["success"]:
    raise ValueError("An error occured while requesting for /language/details/<language>, error: " + r.json()["error"])
print("Successfully requested for /language/details/<language>")
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
        "id": "eng",
        "alpha2": "en",
        "alpha3b": "eng",
        "alpha3t": "eng",
        "alpha3": "eng",
        "name": "English",
        "inForeignLanguages": {},
        "extra": {
            "scope": "Individual",
            "type": "Living"
        }
    }
}

```

#### 返したフィールド

| フィールド        | 詳細                      | タイプ   | null可能  |
| ----------   | -------------------------------- | ------ | --------- |
| `id` | The language id  | str      | いいえ      |
| `alpha2` | The language alpha2 code  | str      | いいえ      |
| `alpha3b` | The language alpha3b code  | str      | いいえ      |
| `alpha3t` | The language alpha3t code  | str      | いいえ      |
| `alpha3` | The language alpha3 code  | str      | いいえ      |
| `name` | The language name  | str      | いいえ      |
| `inForeignLanguages` | The language in foreign languages  | object      | いいえ      |
| `extra` | The language extra data  | object      | いいえ      |

#### 起こりうるエラー

| エラー名         | 詳細                      | コード   |
| ---------------   | -------------------------------- | ------ |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy. This is the base class for the other exceptions raised by translatepy.  | 500  |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
[インデックスに戻る](../%E3%81%AF%E3%81%98%E3%82%81%E3%81%AB.md#インデックス)