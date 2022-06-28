
# Stats セクションのAPIリファレンス

このファイルは「Stats」セクションの全てのエンドポイントを説明します。

# Timings Stats

Get all timings

```http
GET /stats/timings
```

> [server/endpoints/stats.py](../../server/endpoints/stats.py#L17)

### 認証

ログインは**不要**です

### パラメーター

| 名前         | 詳細                      | 必要         | タイプ             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `granularity` | The granularity of the stats  | いいえ            | Granularity            |

### 例

<!-- tabs:start -->


<details>
    <summary>cURL 例</summary>

#### **cURL**

```bash
curl -X GET "/stats/timings"
```

</details>


<details>
    <summary>JavaScript 例</summary>

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
    <summary>Python 例</summary>

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

#### 起こりうるエラー

| エラー名         | 詳細                      | コード   |
| ---------------   | -------------------------------- | ------ |
| `DATABASE_DISABLED` | When the server disabled any database interaction  | 501  |
[インデックスに戻る](../%E3%81%AF%E3%81%98%E3%82%81%E3%81%AB.md#インデックス)

# Errors Stats

Get all errors count for each service

```http
GET /stats/errors
```

> [server/endpoints/stats.py](../../server/endpoints/stats.py#L28)

### 認証

ログインは**不要**です

### パラメーター

| 名前         | 詳細                      | 必要         | タイプ             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `granularity` | The granularity of the stats  | いいえ            | Granularity            |

### 例

<!-- tabs:start -->


<details>
    <summary>cURL 例</summary>

#### **cURL**

```bash
curl -X GET "/stats/errors"
```

</details>


<details>
    <summary>JavaScript 例</summary>

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
    <summary>Python 例</summary>

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

#### 起こりうるエラー

| エラー名         | 詳細                      | コード   |
| ---------------   | -------------------------------- | ------ |
| `DATABASE_DISABLED` | When the server disabled any database interaction  | 501  |
[インデックスに戻る](../%E3%81%AF%E3%81%98%E3%82%81%E3%81%AB.md#インデックス)