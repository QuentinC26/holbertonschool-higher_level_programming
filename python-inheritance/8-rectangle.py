#!/usr/bin/python3
if __name__ == "__main__":
    from base_geometry import BaseGeometry

class BaseGeometry:
    """
    Project Inheritance

    i create a class.
    """
    def area(self):
        """
        Project Inheritance

        i create a class.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Project Inheritance

        i create a class.
        """
        if not type(value) == int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    Project Inheritance

    i create a new class.
    """
    def __init__(self, width, height):
        self.integer_validator("height", height)
        self.integer_validator("height", width)
        self.__width = width
        self.__height = height
