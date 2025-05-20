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
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value=0):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        # i add self.__size **2 for have the area of Square.
        return self.__size**2
