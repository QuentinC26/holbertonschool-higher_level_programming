#!/usr/bin/python3
"""
Project Inheritance

i create a class.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Project Inheritance

    i create a new class.
    """
    def __init__(self, width, height): 
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
