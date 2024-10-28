#!/usr/bin/env python3
"""
function should return a tuple of size
"""


def index_range(page, page_size):
    """
    function should return a tuple of size
    :param page:
    :param page_size:
    :return: return in a list for those particular pagination parameters
    """
    return (page * page_size) - page_size, page * page_size
