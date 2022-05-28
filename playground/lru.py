"""
lru.py

LRU cache implementation for the translatepy project.
"""

import gc
import sys
from collections import OrderedDict
from multiprocessing.pool import ThreadPool


class SizeLimitedLRUCache(OrderedDict):
    """
    Special implementation of a size limited LRU cache.
    """

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
        self.pool = ThreadPool(100)
        super().__init__(*args, **kwds)

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
        value = super().__getitem__(key)
        self.move_to_end(key)
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
                new_obj_size = self.get_size(value)

                while self.get_size(self) + new_obj_size > self.max_size:
                    try:
                        oldest = next(iter(self))
                    except StopIteration:
                        break
                    del self[oldest]

                super().__setitem__(key, value)
                self.move_to_end(key)
        else:
            # if we can overflow the cache, we can just add the object and check for the size later
            super().__setitem__(self, key, value)
            # super().__setitem__(key, value)
            self.move_to_end(key)

            def _set_item():
                while self.get_size(self) > self.max_size:
                    try:
                        oldest = next(iter(self))
                    except StopIteration:
                        break
                    del self[oldest]
        self.pool.apply(_set_item)

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


if __name__ == "__main__":
    a = SizeLimitedLRUCache()
    for i in range(1000000):
        print(i)
        a[i] = i
