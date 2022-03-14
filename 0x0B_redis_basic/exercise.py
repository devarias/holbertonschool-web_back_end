#!/usr/bin/env python3
""" module docs """


from typing import Union
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
