#!/usr/bin/python3
"""Function element_length takes a list as argument and returns 
a list of integers representing the length each element in the list."""

from typing import Iterable, List, Tuple, Sequence

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
