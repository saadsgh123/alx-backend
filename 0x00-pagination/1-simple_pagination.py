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
        """
        Takes 2 integer arguments and returns requested page from the dataset
        Args:
            page (int): required page number. must be a positive integer
            page_size (int): number of records per page. must be a +ve integer
        Return:
            list of lists containing required data from the dataset
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        index = index_range(page, page_size)
        data = self.dataset()[index[0]:index[1]]
        try:
            return data
        except IndexError:
            return []
