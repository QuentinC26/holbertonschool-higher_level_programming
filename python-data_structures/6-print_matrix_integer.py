#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    for row in matrix:
        # row = ligne horizontal
        for index in range(len(row)):
            if index != len(row) - 1:
                print("{:d}".format(row[index]), end=" ")
            else:
                print("{:d}".format(row[index]))
        if len(row) == 0:
            print("")
