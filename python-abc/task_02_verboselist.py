#!/usr/bin/python3
from abc import ABC, abstractmethod

class VerboseList(list):

    def append(self, list):
        super().append(list)
        print("Added [{}] to the list.".format(list))
        return list
    def extend(self, list):
        super().extend(list)
        print("Extended the list with [{}] items.".format(len(list)))
    def remove(self, list):
        super().remove(list)
        print("Removed [{}] from the list.".format(list))
    def pop(self, list):
        super().pop(list)
        print("Popped [{}] from the list.".format((list)))
