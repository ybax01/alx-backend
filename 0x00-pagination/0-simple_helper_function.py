#!/usr/bin/env python3
"""0. Simple helper function"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return
    in a list for those particular pagination parameters.
    """
    return page * page_size - page_size, page * page_size
