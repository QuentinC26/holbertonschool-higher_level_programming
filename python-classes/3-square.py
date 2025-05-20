#!/usr/bin/python3
"""
Square Class.

Square class is a class that represents a square.
I add Private instance attribute: size
"""


class Square:
    '''
    Square Class.

    Square class is a class that represents a square.
    I add Private instance attribute: size
    '''
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        # i add self.__size **2 for have the area of Square.
        return self.__size ** 2
