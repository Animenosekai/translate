# Based on: https://github.com/ZhymabekRoman/platonus_api_wrapper/blob/main/platonus_api_wrapper/utils/lru_cacher.py

import logging
from functools import lru_cache, wraps
from datetime import datetime, timedelta
from collections import OrderedDict

logger = logging.getLogger('translatepy')


class LRUDictCache(OrderedDict):

    def __init__(self, maxsize=1024, *args, **kwds):
        self.maxsize = maxsize
        super().__init__(*args, **kwds)

    def __getitem__(self, key):
        value = super().__getitem__(key)
        self.move_to_end(key)
        return value

    def __setitem__(self, key, value):
        if key in self:
            self.move_to_end(key)
        super().__setitem__(key, value)
        if len(self) > self.maxsize:
            oldest = next(iter(self))
            del self[oldest]

    def clear(self):
        super().clear()


def timed_lru_cache(seconds: int, maxsize: int = 128):
    def wrapper_cache(func):
        func = lru_cache(maxsize)(func)

        func.lifetime = timedelta(seconds=seconds)
        func.expiration = datetime.utcnow() + func.lifetime

        @wraps(func)
        def wrapped_func(self, *args, **kwargs):
            logger.debug("Time now: {}".format(datetime.utcnow()))
            logger.debug("Cached value's expiration time: {}".format(func.expiration))

            # self._cached_functions_list = func

            if datetime.utcnow() >= func.expiration:
                logger.debug("The data in the cache is out of date, clearing the cache...")

                func.cache_clear()
                func.expiration = datetime.utcnow() + func.lifetime

            return func(self, *args, **kwargs)

        return wrapped_func

    return wrapper_cache
