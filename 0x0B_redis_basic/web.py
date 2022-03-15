#!/usr/bin/env python3
""" module docs """

from functools import wraps
import redis
from requests import get
from typing import Callable

r = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """ method docs """

    @wraps(method)
    def wrapper(url):
        """ method docs """
        r.incr(f"count:{url}")
        cached_html = r.get(f"cached:{url}")
        if cached_html:
            return cached_html.decode('utf-8')
        html = method(url)
        r.setex(f"cached:{url}", 10, html)
        return html
    return wrapper


@count_requests
def get_page(url: str) -> str:
    """ method docs """
    response = get(url)
    return response.text
