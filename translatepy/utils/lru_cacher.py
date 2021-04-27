# Based on: https://github.com/ZhymabekRoman/platonus_api_wrapper/blob/main/platonus_api_wrapper/utils/lru_cacher.py

import logging
from functools import lru_cache, wraps
from datetime import datetime, timedelta

logger = logging.getLogger('translatepy')


def timed_lru_cache(seconds: int, maxsize: int = 128):
    def wrapper_cache(func):
        func = lru_cache(maxsize)(func)

        func.lifetime = timedelta(seconds=seconds)
        func.expiration = datetime.utcnow() + func.lifetime

        @wraps(func)
        def wrapped_func(self, *args, **kwargs):
            logger.debug("Time now: " + str(datetime.utcnow()))
            logger.debug("Cached value's expiration time: " + str(func.expiration))

            # self._cached_functions_list = func

            if datetime.utcnow() >= func.expiration:
                logger.debug("The data in the cache is out of date, clearing the cache...")

                func.cache_clear()
                func.expiration = datetime.utcnow() + func.lifetime

            return func(self, *args, **kwargs)

        return wrapped_func

    return wrapper_cache
