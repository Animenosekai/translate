from queue import Queue as _Queue
from threading import Thread
from translatepy.utils.annotations import List


class Queue(_Queue):
    def __init__(self, maxsize: int = 0) -> None:
        super().__init__(maxsize=maxsize)

    def _threads_are_alive(self, threads: List[Thread]):
        for thread in threads:
            if thread.is_alive():
                return True
        return False

    def get(self, threads: List[Thread] = None):
        '''
        Remove and return an item from the queue.

        It waits for a value or the termination of all threads
        '''
        if threads is None:
            threads = []

        with self.not_empty:
            while not self._qsize() and self._threads_are_alive(threads):
                self.not_empty.wait()
            if not self._qsize():
                raise ValueError("No thread returned a value")
            item = self._get()
            self.not_full.notify()
            return item
