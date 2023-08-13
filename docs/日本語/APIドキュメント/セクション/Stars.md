
# Stars セクションのAPIリファレンス

このファイルは「Stars」セクションの全てのエンドポイントを説明します。

# Stars

Get all starred translations

```http
GET /stars
```

> [server/endpoints/stars.py](../../server/endpoints/stars.py#L49)

### 認証

ログインは**不要**です

### 例

<!-- tabs:start -->


<details>
    <summary>cURL 例</summary>

#### **cURL**

```bash
curl -X GET "/stars"
```

</details>


<details>
    <summary>JavaScript 例</summary>

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
    <summary>Python 例</summary>

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

#### 起こりうるエラー

| エラー名         | 詳細                      | コード   |
| ---------------   | -------------------------------- | ------ |
| `DATABASE_DISABLED` | When the server disabled any database interaction  | 501  |
[インデックスに戻る](../%E3%81%AF%E3%81%98%E3%82%81%E3%81%AB.md#インデックス)

# Translation Star

 - ### GETを使って

Get the stars for a translation

```http
GET /stars/<translation_id>
```

> [server/endpoints/stars.py](../../server/endpoints/stars.py#L82)

#### 認証

ログインは**不要**です

#### ダイナミックURL

| 名前         | 詳細                      | 必要         | タイプ             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `translation_id` | The ID of the translation to get  | はい            | str            |

#### 例

<!-- tabs:start -->


<details>
    <summary>cURL 例</summary>

##### **cURL**

```bash
curl -X GET "/stars/<translation_id>"
```

</details>


<details>
    <summary>JavaScript 例</summary>

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
    <summary>Python 例</summary>

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

#### レスポンス

##### レスポンスの例

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

##### 返したフィールド

| フィールド        | 詳細                      | タイプ   | null可能  |
| ----------   | -------------------------------- | ------ | --------- |
| `source` | The source text  | string      | いいえ      |
| `result` | The result text  | string      | いいえ      |
| `language` | The translation languages  | string      | いいえ      |
| `users` | The number of users who starred the translation  | <class 'int'>      | いいえ      |

##### 起こりうるエラー

| エラー名         | 詳細                      | コード   |
| ---------------   | -------------------------------- | ------ |
| `FORBIDDEN` | You are not allowed to star this translation  | 403  |
| `NOT_FOUND` | The translation could not be found  | 404  |
| `DATABASE_DISABLED` | When the server disabled any database interaction  | 501  |
[インデックスに戻る](../%E3%81%AF%E3%81%98%E3%82%81%E3%81%AB.md#インデックス)

 - ### POSTを使って

Star a translation

```http
POST /stars/<translation_id>
```

> [server/endpoints/stars.py](../../server/endpoints/stars.py#L82)

#### 認証

ログインは**不要**です

#### パラメーター

| 名前         | 詳細                      | 必要         | タイプ             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `token` | The token to authenticate the translation  | はい            | TranslationToken            |

#### ダイナミックURL

| 名前         | 詳細                      | 必要         | タイプ             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `translation_id` | The ID of the translation to star  | はい            | str            |

#### 例

<!-- tabs:start -->


<details>
    <summary>cURL 例</summary>

##### **cURL**

```bash
curl -X POST \
    --data-urlencode "token=<The token to authenticate the translation>" \
    "/stars/<translation_id>"
```

</details>


<details>
    <summary>JavaScript 例</summary>

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
    <summary>Python 例</summary>

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

#### レスポンス

##### レスポンスの例

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

##### 返したフィールド

| フィールド        | 詳細                      | タイプ   | null可能  |
| ----------   | -------------------------------- | ------ | --------- |
| `source` | The source text  | string      | いいえ      |
| `result` | The result text  | string      | いいえ      |
| `language` | The translation languages  | string      | いいえ      |
| `users` | The number of users who starred the translation  | <class 'int'>      | いいえ      |

##### 起こりうるエラー

| エラー名         | 詳細                      | コード   |
| ---------------   | -------------------------------- | ------ |
| `FORBIDDEN` | You are not allowed to star this translation  | 403  |
| `NOT_FOUND` | The translation could not be found  | 404  |
| `DATABASE_DISABLED` | When the server disabled any database interaction  | 501  |
[インデックスに戻る](../%E3%81%AF%E3%81%98%E3%82%81%E3%81%AB.md#インデックス)

 - ### DELETEを使って

Unstar a translation

```http
DELETE /stars/<translation_id>
```

> [server/endpoints/stars.py](../../server/endpoints/stars.py#L82)

#### 認証

ログインは**不要**です

#### ダイナミックURL

| 名前         | 詳細                      | 必要         | タイプ             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `translation_id` | The ID of the translation to unstar  | はい            | str            |

#### 例

<!-- tabs:start -->


<details>
    <summary>cURL 例</summary>

##### **cURL**

```bash
curl -X DELETE "/stars/<translation_id>"
```

</details>


<details>
    <summary>JavaScript 例</summary>

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
    <summary>Python 例</summary>

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

##### 起こりうるエラー

| エラー名         | 詳細                      | コード   |
| ---------------   | -------------------------------- | ------ |
| `FORBIDDEN` | You are not allowed to star this translation  | 403  |
| `NOT_FOUND` | The translation could not be found  | 404  |
| `DATABASE_DISABLED` | When the server disabled any database interaction  | 501  |
[インデックスに戻る](../%E3%81%AF%E3%81%98%E3%82%81%E3%81%AB.md#インデックス)
