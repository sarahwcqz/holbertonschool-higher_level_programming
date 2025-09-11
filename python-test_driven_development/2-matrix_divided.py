#!/usr/bin/python3
"""
This module provides a function that divides all elements
of a matrix by a given number.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given
    number.

    The function checks that the matrix is a list of lists of integers or
    floats, with all rows of the same size. It also validates that `div`
    is a non-zero number. Each element of the matrix is divided by `div`
    and the result is rounded to 2 decimal places.

    Args:
        matrix (list of lists of int/float): The matrix to be divided.
        div (int or float): The number to divide all elements by.

    Raises:
        TypeError: If `matrix` is not a list of lists of integers/floats.
        TypeError: If each row of the matrix does not have the same size.
        TypeError: If `div` is not a number.
        ZeroDivisionError: If `div` is equal to 0.

    Returns:
        list of lists of float: A new matrix containing the results of
        the division.

    Example:
        >>> matrix = [[1, 2, 3], [4, 5, 6]]
        >>> print(matrix_divided(matrix, 2))
        [[0.5, 1.0, 1.5], [2.0, 2.5, 3.0]]
    """
