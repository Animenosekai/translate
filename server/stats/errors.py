from schemas.types import Granularity

from endpoints.translation import errors
from datetime import datetime, timedelta


def get_errors_count(granularity: Granularity = "hour"):
    replacement = {"minute": 0, "second": 0, "microsecond": 0}
    delta = timedelta(days=1)

    if granularity == "day":
        replacement.update({
            "hour": 0
        })
        delta = timedelta(days=31)
    elif granularity == "month":
        replacement.update({
            "day": 1,
            "hour": 0
        })
        delta = timedelta(days=365)
    elif granularity == "year":
        replacement.update({
            "month": 1,
            "day": 1,
            "hour": 0
        })
        delta = timedelta(days=365 * 10)

    dataset = errors.find({
        "timestamp": {
            "$gte": datetime.utcnow() - delta
        }
    })

    data = {}

    for document in dataset:
        current_key = document.timestamp.replace(**replacement)
        try:
            data[current_key][document.service] += 1
        except KeyError:
            try:
                data[current_key][document.service] = 1
            except KeyError:
                data[current_key] = {document.service: 1}

    services = set()
    for _, results in data.items():
        services.update(results.keys())  # getting the missing services

    for _, results in data.items():
        for service in services.difference(results.keys()):
            results[service] = 0  # filling the missing services

    results = []

    for hour in data:
        data[hour]["__timestamp__"] = int(hour.timestamp())
        results.append(data[hour])

    return {"services": services, "results": results}
