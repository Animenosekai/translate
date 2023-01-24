"""
lru.py

LRU cache implementation for the translatepy project.
"""

import gc
import os
import sys
import logging
from functools import lru_cache, wraps
from collections import OrderedDict # , MutableMapping
from multiprocessing.pool import ThreadPool
from datetime import datetime, timedelta

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


class SizeLimitedLRUCache():
    """
    Special implementation of a size limited LRU cache.
    """

    __slots__ = ("_lru_size", "ordered_dict", "max_size", "allow_overflow")

    pool = ThreadPool(100)

    def __init__(self, *args, max_size: int = 1e+7, allow_overflow: bool = True, **kwds):
        """
        Initialize a cache object with a maximum cache size.

        Parameters
        ----------
        max_size : int
            Maximum size of the cache in bytes.
        """
        self.allow_overflow = bool(allow_overflow)
        self.max_size = int(max_size)
        if sys.version_info[1] >= 7:
            # In Python 3.7+, the dictionary is ordered by default.
            self.ordered_dict = {}
        else:
            self.ordered_dict = OrderedDict(*args, **kwds)
        self._lru_size = {"total_size": self.get_size(self.ordered_dict)}

    def __getitem__(self, key):
        """
        Get an item from the cache.

        Parameters
        ----------
        key : Any
            The key to get the item for.

        Returns
        -------
        Any
            The item for the given key.

        Notes
        -----
        - Calling self.__getitem__(key) is equivalent to calling self[key].
        - This is considered as an operation made to the cache and the object will be placed at the end.
        """
        value = self.ordered_dict.__getitem__(key)
        # self.ordered_dict.move_to_end(key)
        return value

    def __setitem__(self, key, value):
        """
        Set an item in the cache.

        Parameters
        ----------
        key : Any
            The key to set the item for.
        value : Any
            The item to set.

        Notes
        -----
        - Calling self.__setitem__(key, value) is equivalent to calling self[key] = value.
        - This is considered as an operation made to the cache and the object will be placed at the end.
        - The object might is not added right after this call if allow_overflow is set to False
        """
        if not self.allow_overflow:
            def _set_item():
                obj_size = self.get_size({key: value})
                self._lru_size[key] = obj_size
                self._lru_size["total_size"] += obj_size
                while self._lru_size["total_size"] > self.max_size:
                    try:
                        oldest = next(iter(self.ordered_dict))
                    except StopIteration:
                        break

                    self._lru_size["total_size"] -= self._lru_size[oldest]

                    del self.ordered_dict[oldest]
                    del self._lru_size[oldest]

                self.ordered_dict.__setitem__(key, value)
                # self.move_to_end(key)
        else:
            # if we can overflow the cache, we can just add the object and check for the size later
            # self.ordered_dict.__setitem__(self, key, value)
            
            self.ordered_dict.__setitem__(key, value)
            # self.ordered_dict.move_to_end(key)

            def _set_item():
                obj_size = self.get_size({key: value})
                self._lru_size[key] = obj_size
                self._lru_size["total_size"] += obj_size
                while self._lru_size["total_size"] > self.max_size:
                    try:
                        oldest = next(iter(self.ordered_dict))
                    except StopIteration:
                        break

                    self._lru_size["total_size"] -= self._lru_size[oldest]

                    del self.ordered_dict[oldest]
                    del self._lru_size[oldest]

        self.pool.apply(_set_item)

    def __iter__(self):
        return iter(self.ordered_dict)

    def get_size(self, obj, builtin: bool = False):
        """
        Get the size of an object.

        Parameters
        ----------
        obj : Any
            The object to get the size of.
        builtin : bool
            Whether to use the builtin sys.getsizeof function or not.
            This function is faster than the custom implementation but might yield inaccurate results for complex objects.

        Returns
        -------
        int
            The size of the object in bytes.

        Notes
        -----
        The second implementation of this function is based on the following article:
            https://towardsdatascience.com/the-strange-size-of-python-objects-in-memory-ce87bdfbb97f
        """
        if builtin:
            return sys.getsizeof(obj)
        memory_size = 0
        ids = set()
        objects = [obj]
        while objects:
            new = []
            for obj in objects:
                if id(obj) not in ids:
                    ids.add(id(obj))
                    memory_size += sys.getsizeof(obj)
                    new.append(obj)
            objects = gc.get_referents(*new)  # we could use a ThreadPool to reexecute get_size on each referent but that would create too much threads
        return memory_size

    def clear(self):
        self.ordered_dict.clear()


def timed_lru_cache(seconds: int, maxsize: int = 128):
    def wrapper_cache(func):
        func = lru_cache(maxsize)(func)

        func.lifetime = timedelta(seconds=seconds)
        func.expiration = datetime.utcnow() + func.lifetime

        @wraps(func)
        def wrapped_func(self, *args, **kwargs):
            logger.debug("Time now: {}".format(datetime.utcnow()))
            logger.debug("Cached value's expiration time: {}".format(func.expiration))

            if datetime.utcnow() >= func.expiration:
                logger.debug("The data in the cache is out of date, clearing the cache...")

                func.cache_clear()
                func.expiration = datetime.utcnow() + func.lifetime

            return func(self, *args, **kwargs)

        return wrapped_func

    return wrapper_cache
