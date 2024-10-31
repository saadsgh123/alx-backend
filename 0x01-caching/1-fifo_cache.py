#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Defines a class for caching information in key-value pairs
        Methods:
            put(key, item) - store a key-value pair
            get(key) - retrieve the value associated with a key
    """

    def __init__(self):
        """
            Return the value linked to a given key, or None
        """
        BaseCaching.__init__(self)

    def distract(self):
        """
            Return the value linked to a given key, or None
        """
        ordered_key = []
        for key in self.cache_data.keys():
            ordered_key.append(ord(key))
        for _ in ordered_key:
            for i in range(len(ordered_key) - 1):
                if ordered_key[i] > ordered_key[i + 1]:
                    temp = ordered_key[i]
                    ordered_key[i] = ordered_key[i + 1]
                    ordered_key[i + 1] = temp
        del self.cache_data[chr(ordered_key[0])]
        print("DISCARD: {}".format(chr(ordered_key[0])))

    def put(self, key, item):
        """
            Return the value linked to a given key, or None
        """
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                self.distract()
            self.cache_data[key] = item

    def get(self, key):
        """
        Return the value linked to a given key, or None
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
