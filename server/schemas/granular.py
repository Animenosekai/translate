"""
This defines the different level of granularity for the data.

The available granularities are :
- MINUTELY
- HOURLY
- DAILY
- MONTHLY
- YEARLY

NOT USED FOR NOW
"""

from datetime import datetime
from yuno import YunoDict


class Period(YunoDict):
    service: str
    timestamp: datetime
    timings: list[int]
    errors: list[int]
