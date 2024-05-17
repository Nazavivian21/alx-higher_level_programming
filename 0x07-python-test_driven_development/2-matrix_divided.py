#!/usr/bin/python3
"""This module divides the integers or floats in matrix"""


def matrix_divided(matrix, div):
    """This function returns the quotient of all elements in a matrix. """
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                 "matrix must be a matrix (list of lists) of integers/floats"
                )

    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row] for row in matrix]
