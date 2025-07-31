#!/usr/bin/python3
"""
class student
"""


class Student:
    """
    class student
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list):
            hidden_dictionnary = {}
            for index in attrs:
                if hasattr(self, index):
                    hidden_dictionnary[index] = getattr(self, index)
            return hidden_dictionnary
        else:
            return vars(self)

    def reload_from_json(self, json):
        return json
