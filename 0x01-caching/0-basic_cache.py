#!/usr/bin/python3
"""0. Basic dictionary"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Basic Caching System
    """
    def put(self, key, item):
        """ Add an item in the cache
        """
        if (key is not None and item is not None):
            self.cache_date[key] = item

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key, None)
