#!/usr/bin/env python3
""" Pagination with Python """
from typing import Tuple


def index_range(page, page_size: int) -> Tuple[int, int]:
    """ Calculates the index range to start """
    start_index = (page - 1) * page_size
    
    end_index = page + page_size - 1
    
    return (start_index, end_index)
