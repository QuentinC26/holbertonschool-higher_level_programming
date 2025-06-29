#!/usr/bin/python3
'''
 prints a square with the character #
'''


def print_square(size):
    '''
    prints a square with the character #
    '''
    triangle = "#"
    if size == float and size < 0:
        raise TypeError("size must be an integer") 
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for row in range(size):
        for index in range(size - 1):
            print(triangle, end="")
        print(triangle)
