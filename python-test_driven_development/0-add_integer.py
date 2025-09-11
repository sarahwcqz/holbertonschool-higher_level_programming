#!/usr/bin/python3
"""
This module contains a function to add two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats and returns the integer result.
    Floats are casted to integers before addition.
    Raises TypeError if arguments are not int or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    res = a + b
    return res
