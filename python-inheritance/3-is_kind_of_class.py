#!/usr/bin/python3
"""
Project Inheritance

i want print the list of available attributes and methods of an object.
"""


def is_kind_of_class(obj, a_class):
    """
    Project Inheritance

    i want print the list of available attributes and methods of an object.
    """
    if type(obj) is a_class or isinstance(obj, a_class):
        return True
    else:
        return False
