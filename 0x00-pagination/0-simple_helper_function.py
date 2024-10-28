#!/usr/bin/env python3
"""
function should return a tuple of size
"""
import csv
from typing import List


def index_range(page, page_size):
    """
    function should return a tuple of size
    :param page:
    :param page_size:
    :return: return in a list for those particular pagination parameters
    """
    return (page * page_size) - page_size, page * page_size


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        if not isinstance(page, int) and not isinstance(page_size, int):
            assert ()
        if page <= 0 and page_size <= 0:
            assert ()
        return self.dataset()[:(page * page_size)]