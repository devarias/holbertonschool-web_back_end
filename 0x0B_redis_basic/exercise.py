#!/usr/bin/env python3
""" module docs """


from typing import Callable, Optional, Union
from uuid import uuid4
import redis


class Cache:
    """ class docs """

    _redis = redis.Redis()

    def __init__(self) -> None:
        """ constructor docs """
        self._redis.flushdb()

    def store(self, data: Union[bytes, float, int, str]) -> str:
        """ method docs """
        random_key = str(uuid4())
        self._redis.set(random_key, data)

        return random_key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[bytes, float, int, str]:
        """ method docs """
        value = self._redis.get(key)
        return fn(value) if fn else value

    def get_str(self, key: str) -> str:
        """ method docs """
        return self._redis.get(key).decode("utf-8")

    def get_int(self, key: str) -> int:
        """ method docs """
        value = self._redis.get(key)
        try:
            value = int(value.decode("utf-8"))
        except ValueError:
            value = 0
        return value
