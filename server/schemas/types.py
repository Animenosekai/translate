from datetime import datetime


class Datetime(datetime):
    def __new__(self, *args, **kwargs) -> datetime:
        if len(args) > 0 and isinstance(args[0], datetime):
            return args[0]
        return datetime(*args, **kwargs)


class StringEnum(str):
    """A string enum, only accepting certain values"""
    ACCEPTED = tuple()
    DEFAULT = ""
    UPPER = True
    LOWER = False

    def __new__(self, value: str, **kw):
        value = str(value).replace(" ", "")
        if self.UPPER:
            value = value.upper()
        elif self.LOWER:
            value = value.lower()
        if value not in self.ACCEPTED:
            value = self.DEFAULT
        return str.__new__(self, value, **kw)

class Granularity(StringEnum):
    ACCEPTED = ("hour", "day", "month", "year")
    UPPER = False
    LOWER = True
    DEFAULT = "hour"