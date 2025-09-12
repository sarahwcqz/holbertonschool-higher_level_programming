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
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
        isinstance

    for row in matrix:
        for obj in row:
            if not isinstance(obj, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    return list(map(lambda row: list(map(lambda x: round(x / div, 2), row)), matrix))
