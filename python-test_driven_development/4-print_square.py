#!/usr/bin/python3
'''
 prints a square with the character #
'''


def print_square(size):
    '''
    prints a square with the character #
    '''
    triangle = 0
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == float and size < 0:
        raise TypeError("size must be an integer") 
    else:
        for index in range(size):
            size = "#"
            print(size)