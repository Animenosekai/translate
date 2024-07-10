from queue import Queue as _Queue
from threading import Thread
import typing


class Queue(_Queue):
    def __init__(self, maxsize: int = 0) -> None:
        super().__init__(maxsize=maxsize)

    def _threads_are_alive(self, threads: typing.List[Thread]):
        for thread in threads:
            if thread.is_alive():
                return True
        return False

    def get(self, threads: typing.Optional[typing.List[Thread]] = None,
            timeout: typing.Optional[int] = None):
        '''
        Remove and return an item from the queue.

        It waits for a value or the termination of all threads
        '''
        threads = threads or []

        with self.not_empty:
            while not self._qsize() and self._threads_are_alive(threads):
                self.not_empty.wait(timeout=timeout)
            if not self._qsize():
                raise ValueError("No thread returned a value or the timeout has been reached")
            item = self._get()
            self.not_full.notify()
            return item
