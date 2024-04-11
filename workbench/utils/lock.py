import threading
from typing import List


class ReentrantRWLock:
    """
    A lock object that allows many simultaneous "read locks", but only one "write lock."
    it also ignores multiple write locks from the same thread
    """

    def __init__(self):
        self._writer = None  # current writer
        self._readers: List[int] = []  # list of unique readers
        self._read_ready = threading.Condition(threading.Lock())
        self._with_ops_write = (
            []
        )  # stack for 'with' keyword for write or read operations, 0 for read 1 for write
        self._ops_arr_lock = threading.Lock()  # lock for previous list

    def acquire_read(self):
        """
        Acquire a read lock. Blocks only if a another thread has acquired the write lock.
        """
        ident = threading.current_thread().ident
        if self._writer == ident or ident in self._readers:
            return
        with self._read_ready:
            self._readers.append(ident)

    def release_read(self):
        """
        Release a read lock if exists from this thread
        """
        ident = threading.current_thread().ident
        if self._writer == ident or ident not in self._readers:
            return
        with self._read_ready:
            self._readers.remove(ident)
            if len(self._readers) == 0:
                self._read_ready.notifyAll()

    def acquire_write(self):
        """
        Acquire a write lock. Blocks until there are no acquired read or write locks from another thread.
        """
        ident = threading.current_thread().ident
        if self._writer == ident:
            return
        self._read_ready.acquire()
        me_included = 1 if ident in self._readers else 0
        while len(self._readers) - me_included > 0:
            self._read_ready.wait()
        self._writer = ident

    def release_write(self):
        """
        Release a write lock if exists from this thread.
        """
        if not self._writer or not self._writer == threading.current_thread().ident:
            return
        self._writer = None
        self._read_ready.release()

    def __enter__(self):
        with self._ops_arr_lock:
            if len(self._with_ops_write) == 0:
                raise RuntimeError(
                    "ReentrantRWLock: used 'with' block without call to for_read or for_write"
                )
            write = self._with_ops_write[-1]
        if write:
            self.acquire_write()
        else:
            self.acquire_read()

    def __exit__(self, exc_type, exc_value, tb):
        with self._ops_arr_lock:
            write = self._with_ops_write.pop()
        if write:
            self.release_write()
        else:
            self.release_read()
        if exc_type is not None:
            return False  # exception happened
        return True

    def for_read(self):
        """
        used for 'with' block
        """
        with self._ops_arr_lock:
            self._with_ops_write.append(0)
        return self

    def for_write(self):
        """
        used for 'with' block
        """
        with self._ops_arr_lock:
            self._with_ops_write.append(1)
        return self
