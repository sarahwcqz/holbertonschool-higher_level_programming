#!/usr/bin/python3
"""
This module contains a function that prints a square of a given size
using the '#' character.
"""


def print_square(size):
    """
    Prints a square with the character '#'.

    The square has a side length equal to `size`. Each line contains
    exactly `size` characters, and there are `size` lines in total.

    Args:
        size (int): The size length of the square. Must be a non-negative
        integer.

    Raises:
        TypeError: If `size` is not an integer.
        ValueError: If `size` is less than 0.

    Example:
        >>> print_square(3)
        ###
        ###
        ###
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
