#!/usr/bin/python3
"""
Project Inheritance

i want print the list of available attributes and methods of an object.
"""


class MyList(list):
    """
    Project Inheritance

    i create a new class.
    """


    def __init__(self):
        pass


    def print_sorted(self):
        """
        Project Inheritance

        i want print the list of available attributes and methods of an object.
        """
        for index in self:
            if not isinstance(index, int):
                raise TypeError("Its not a integer")
        print(sorted(self))
        return self
