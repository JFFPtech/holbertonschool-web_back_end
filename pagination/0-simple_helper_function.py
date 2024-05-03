#!/usr/bin/env python3
""" Pagination with Python """


def index_range(page, page_size):
    """ Calculates the index range to start """
    start_index = (page - 1) * page_size
    
    end_index = start_index + page_size - 1
    
    return start_index, end_index
