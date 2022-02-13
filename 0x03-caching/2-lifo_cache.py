#!/usr/bin/python3
""" module docs """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ class docs """

    def __init__(self):
        super().__init__()
        self.last_key = ''

    def put(self, key, item):
        """ method docs """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                print("DISCARD: {}".format(self.last_key))
                self.cache_data.pop(self.last_key)
            self.last_key = key

    def get(self, key):
        """ method docs """
        if key in self.cache_data:
            return self.cache_data[key]
        if key is None or self.cache_data.get(key) is None:
            return None
