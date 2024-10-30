#!/usr/bin/env python3
""" BaseCaching module
"""

from basic_caching import BaseCaching


class BasicCache(BaseCaching):
    """
        Defines a class for caching information in key-value pairs
        Methods:
            put(key, item) - store a key-value pair
            get(key) - retrieve the value associated with a key
    """

    def __init__(self):
        BaseCaching.__init__(self)

    def put(self, key, value):
        """
            Initialize the class using the parent class __init__ method
        """
        if key is None or value is None:
            pass
        else:
            self.cache_data[key] = value

    def get(self, key):
        """
        Return value linked to key.
        If key is None or doesn't exist, return None
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
