#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    new_matrix = matrix

    for row in new_matrix:
        # row = ligne horizontal
        for index in range(len(row)):
            new_matrix = matrix[index][index] * matrix[index][index]
        if len(row) == 0:
            print("")
    return new_matrix
