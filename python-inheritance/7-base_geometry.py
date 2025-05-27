#!/usr/bin/python3
"""
Project Inheritance

i create a class.
"""


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
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

