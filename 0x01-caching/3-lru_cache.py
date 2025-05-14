#!/usr/bin/python3
"""3. LRU Caching"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """LRU Caching"""

    def __init__(self):
        """ Initiliaze
        """
        self.queue = []
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if (key and item):
            if self.cache_data.get(key):
                self.queue.remove(key)
            self.queue.append(key)
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                delete = self.queue.pop(0)
                self.cache_data.pop(delete)
                print('DISCARD: {}'.format(delete))

    def get(self, key):
        """ Get an item by key
        """
        if self.cache_data.get(key):
            self.queue.remove(key)
            self.queue.append(key)
        return self.cache_data.get(key, None)
