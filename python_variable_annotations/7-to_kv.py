#!/usr/bin/python3
"""Function to_kv takes string k and an int arguments, returns a tuple"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple containing a string and the square of a number"""
    return (k, v * v)
