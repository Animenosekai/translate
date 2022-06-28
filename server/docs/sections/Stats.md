
# Stats Section API Reference

This file lists and explains the different endpoints available in the Stats section.

# Timings Stats

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
| `granularity` | The granularity of the stats  | No            | Granularity            |

#### Possible Errors

| Exception         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `DATABASE_DISABLED` | When the server disabled any database interaction  | 501  |
[Return to the Index](../Getting%20Started.md#index)

# Erros Stats

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
| `granularity` | The granularity of the stats  | No            | Granularity            |

#### Possible Errors

| Exception         | Description                      | Code   |
| ---------------   | -------------------------------- | ------ |
| `DATABASE_DISABLED` | When the server disabled any database interaction  | 501  |
[Return to the Index](../Getting%20Started.md#index)