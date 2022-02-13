#!/usr/bin/python3
"""  module docs """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """class docs"""

    def put(self, key, item):
        """ method docs """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ method docs """
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
