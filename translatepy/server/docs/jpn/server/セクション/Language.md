
# Language セクションのAPIリファレンス

このファイルは「Language」セクションの全てのエンドポイントを説明します。

# __language__

This represents a non implemented endpoint

```http
* /api/language/<string:language>
```

> [../../../../endpoints/api/language.py](../../../../endpoints/api/language.py#L17)

### 認証

ログインは**不要**です

### ダイナミックURL

| 名前         | 詳細                      | 必要         | タイプ             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `language` | 詳細なし  | はい            | Language            |

### 例

<!-- tabs:start -->


<details>
    <summary>cURL 例</summary>

#### **cURL**

```bash
curl -X * "/api/language/<string:language>"
```

</details>


<details>
    <summary>JavaScript 例</summary>

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
    <summary>Python 例</summary>

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

#### 起こりうるエラー

| エラー名         | 詳細                      | コード   |
| ---------------   | -------------------------------- | ------ |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy  | 500  |
[インデックスに戻る](../%E3%81%AF%E3%81%98%E3%82%81%E3%81%AB.md#インデックス)

# search

This represents a non implemented endpoint

```http
* /api/language/search
```

> [../../../../endpoints/api/language.py](../../../../endpoints/api/language.py#L22)

### 認証

ログインは**不要**です

### パラメーター

| 名前         | 詳細                      | 必要         | タイプ             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `limit` | 詳細なし  | いいえ            | int            |
| `query` | 詳細なし  | はい            | str            |

### 例

<!-- tabs:start -->


<details>
    <summary>cURL 例</summary>

#### **cURL**

```bash
curl -X * \
    --data-urlencode "limit=<>"\
    --data-urlencode "query=<>" \
    "/api/language/search"
```

</details>


<details>
    <summary>JavaScript 例</summary>

#### **JavaScript**

```javascript
fetch(`/api/language/search?query=${encodeURIComponent("query")}`, {
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
    <summary>Python 例</summary>

#### **Python**

```python
import requests
r = requests.request("*", "/api/language/search",
        params = {
            "query": "query"
        })
if r.status_code >= 400 or not r.json()["success"]:
    raise ValueError("An error occured while requesting for /api/language/search, error: " + r.json()["error"])
print("Successfully requested for /api/language/search")
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
        "languages": "no example"
    }
}

```

#### 返したフィールド

| フィールド        | 詳細                      | タイプ   | null可能  |
| ----------   | -------------------------------- | ------ | --------- |
| `languages` | The language search results  | <class 'list'>      | いいえ      |

#### 起こりうるエラー

| エラー名         | 詳細                      | コード   |
| ---------------   | -------------------------------- | ------ |
| `UNKNOWN_LANGUAGE` | When one of the provided language could not be understood by translatepy. Extra information like the string similarity and the most similar string are provided in `data`.  | 400  |
| `TRANSLATEPY_EXCEPTION` | Generic exception raised when an error occured on translatepy  | 500  |
[インデックスに戻る](../%E3%81%AF%E3%81%98%E3%82%81%E3%81%AB.md#インデックス)