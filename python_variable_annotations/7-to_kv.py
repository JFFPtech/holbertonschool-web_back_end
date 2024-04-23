#!/usr/bin/python3
"""Type-annotated function to_kv that takes a string k and an int OR float v as arguments and returns a tuple containing k and the square of v. The float v will be type-annotated as a Union."""

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple containing a string and the square of a number"""
    return (k, v * v)