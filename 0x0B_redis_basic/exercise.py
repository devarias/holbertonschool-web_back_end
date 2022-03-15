#!/usr/bin/env python3
""" module docs """


from functools import wraps
import redis
from typing import Union, Optional, Callable
from uuid import uuid4


def count_calls(method: Callable) -> Callable:
    """ method doc """

    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ method doc """
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ method doc """

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ method doc """
        input = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", input)
        output = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", output)
        return output
    return wrapper


def replay(fn: Callable):
    """ method doc """
    r = redis.Redis()
    f_name = fn.__qualname__
    n_calls = r.get(f_name)
    try:
        n_calls = n_calls.decode('utf-8')
    except Exception:
        n_calls = 0
    print(f'{f_name} was called {n_calls} times:')

    ins = r.lrange(f_name + ":inputs", 0, -1)
    outs = r.lrange(f_name + ":outputs", 0, -1)

    for input, output in zip(ins, outs):
        try:
            input = input.decode('utf-8')
        except Exception:
            input = ""
        try:
            output = output.decode('utf-8')
        except Exception:
            output = ""
        print(f'{f_name}(*{input}) -> {output}')


class Cache:
    """ class docs """

    def __init__(self) -> None:
        """ constructor docs """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ method docs """
        random_key = str(uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
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
