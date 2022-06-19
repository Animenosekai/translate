
# Stats Section API Reference

This file lists and explains the different endpoints available in the Stats section.

## Timings Stats

Get all timings

```http
GET /stats/timings
```

> [server/endpoints/stats.py](../../server/endpoints/stats.py#L17)

### Authentication

Login is **not** required

### Parameters

| Name         | Description                      | Required         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `granularity` | The granularity of the stats  | False            | Granularity            |

### Example

<!-- tabs:start -->

#### **cURL**

```bash
curl -X GET "/stats/timings"
```

#### **JavaScript**

```bash
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

#### **Python**

```bash
import requests
r = requests.request("GET", "/stats/timings")
if r.status_code >= 400 or not r.json()["success"]:
    raise ValueError("An error occured while requesting for /stats/timings, error: " + r.json()["error"])
print("Successfully requested for /stats/timings")
print(r.json()["data"])
```
<!-- tabs:end -->

#### Possible Errors

| Exception         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `DATABASE_DISABLED` | When the server disabled any database interaction  | 501  |
[Return to the Index](../Getting%20Started.md#index)

## Erros Stats

Get all errors count for each service

```http
GET /stats/errors
```

> [server/endpoints/stats.py](../../server/endpoints/stats.py#L28)

### Authentication

Login is **not** required

### Parameters

| Name         | Description                      | Required         | Type             |
| ------------ | -------------------------------- | ---------------- | ---------------- |
| `granularity` | The granularity of the stats  | False            | Granularity            |

### Example

<!-- tabs:start -->

#### **cURL**

```bash
curl -X GET "/stats/errors"
```

#### **JavaScript**

```bash
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

#### **Python**

```bash
import requests
r = requests.request("GET", "/stats/errors")
if r.status_code >= 400 or not r.json()["success"]:
    raise ValueError("An error occured while requesting for /stats/errors, error: " + r.json()["error"])
print("Successfully requested for /stats/errors")
print(r.json()["data"])
```
<!-- tabs:end -->

#### Possible Errors

| Exception         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `DATABASE_DISABLED` | When the server disabled any database interaction  | 501  |
[Return to the Index](../Getting%20Started.md#index)