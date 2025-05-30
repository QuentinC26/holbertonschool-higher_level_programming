#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
Project Inheritance

i create a class.
"""


class Rectangle(BaseGeometry):
    """
    Project Inheritance

    i create a new class.
    """
    def __init__(self, width, height):
        if not isinstance(height, int) or not isinstance(width, int):
            raise TypeError("height must be an integer")
        if height <= 0 or width <= 0:
            raise ValueError("height and must are be greater than 0")
        self.__width = width
        self.__height = height
