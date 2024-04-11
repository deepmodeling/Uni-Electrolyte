import redis
import os
import urllib.parse
from abc import ABCMeta, abstractmethod
from pathlib import Path
import threading
import gzip
from loguru import logger

from utils.lock import ReentrantRWLock
from config import VAR_ROOT
from utils.tracer import trace_time

local = threading.local()


class Store(metaclass=ABCMeta):
    @abstractmethod
    def get(self, path):
        pass

    @abstractmethod
    def put(self, path, data):
        pass

    @abstractmethod
    def delete(self, path):
        pass

    @abstractmethod
    def exists(self, path):
        pass



class RedisStore(Store):
    def __init__(self, host="localhost", port=6379, db=0, password=None):
        self._redis = redis.Redis(
            host=host, port=port, db=db, password=password, decode_responses=False
        )

    @trace_time
    def get(self, path):
        value = self._redis.get(path)
        if not value:
            return
        return gzip.decompress(value).decode("utf-8")

    @trace_time
    def put(self, path, data):
        data = gzip.compress(data.encode("utf-8"))
        self._redis.set(path, data)

    def delete(self, path):
        self._redis.delete(path)

    def exists(self, path):
        return self._redis.exists(path)

    @classmethod
    def from_url(cls, redis_url):
        url = urllib.parse.urlparse(redis_url)
        return cls(
            host=url.hostname,
            port=url.port,
            db=int(url.path[1:]),
            password=url.password,
        )


def get_store():
    if getattr(local, "store", None) is None:
        redis_url = os.getenv("REDIS_URL") or "redis://127.0.0.1:6379/0"
        local.store = RedisStore.from_url(redis_url)
    return local.store
