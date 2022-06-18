from datetime import datetime


class Datetime(datetime):
    def __new__(self, *args, **kwargs) -> datetime:
        print(args, kwargs)
        if len(args) > 0 and isinstance(args[0], datetime):
            return args[0]
        return datetime(*args, **kwargs)
