#!/usr/bin/python3
"""
Function for divided the matrix
"""


def matrix_divided(matrix, div):
    """
    Function for divided the matrix
    """
    new_matrix = []

    for row in matrix:
        new_row = []
        for index in row:
            if len(row) != len(matrix[0]):
                raise TypeError(
                    "Each row of the matrix must have the same size"
                    )
            if not isinstance(index, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of list) of integers/floats"
                    )
            if not isinstance(div, (int, float)):
                raise TypeError("div must be a number")
            if div == 0:
                raise ZeroDivisionError("division by zero")
            result = index / div
            """round is for have 2 decimals after the float"""
            good_result = round(result, 2)
            new_row.append(good_result)
        new_matrix.append(new_row)
    return new_matrix
