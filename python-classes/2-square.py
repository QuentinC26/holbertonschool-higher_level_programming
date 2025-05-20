#!/usr/bin/python3
"""
Square Class.

Square class is a class that represents a square.
This must add Private instance attribute: size
Im use a try and except for manage the different condition.
"""


class Square:
    '''
    Square Class.

    Square class is a class that represents a square.
    This must add Private instance attribute: size
    Im use a try and except for manage the different condition.
    '''
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
