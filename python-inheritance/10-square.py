#!/usr/bin/python3
"""
Project Inheritance

i create a class.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Project Inheritance

    i create a new class.
    """
    def __init__(self, size):
        super().__init__(size, size)
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size <= 0:
            raise ValueError("size must be greater than 0")
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size
