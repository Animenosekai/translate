from traceback import print_exc
from schemas.types import Granularity

from endpoints.translation import timings
from datetime import datetime, timedelta


def get_timings(granularity: Granularity = "hour"):
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

    dataset = timings.find({
        "timestamp": {
            "$gte": datetime.utcnow() - delta
        }
    })

    data = {}

    for document in dataset:
        current_key = document.timestamp.replace(**replacement)
        try:
            for service, value in document.timings.items():
                service = str(service).replace("*dot*", ".")
                try:
                    data[current_key][service].append(value)
                except KeyError:
                    data[current_key][service] = [value]
        except KeyError:
            data[current_key] = {str(service).replace("*dot*", "."): [v] for service, v in document.timings.items()}

    services = set()

    for _, results in data.items():
        services.update(results.keys())  # getting the missing services

    results = []

    for hour in data:
        result = {
            "__timestamp__": int(hour.timestamp())
        }
        for service, values in data[hour].items():
            if len([v for v in values if v > 0]) > 0:
                result[str(service).replace("*dot*", ".")] = round(sum(values) / len(values) * 1000, 2)  # in ms
        results.append(result)

    return {"services": services, "results": results}
