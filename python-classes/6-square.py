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
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 and value[1] < 0:
            raise ValueError("position must be a tuple of 2 positive integers")
        if not len(value) == 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] >= 0 or value[1] >= 0:
            print(" ")
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print("")
            return
        else:
            for horizontal in range(self.__position[1]):
                print()
            for vertical in range(self.size):
                print(" " * self.__position[0] + "#" * self.__size)

    def area(self):
        # i add self.__size **2 for have the area of Square.
        return self.__size**2
