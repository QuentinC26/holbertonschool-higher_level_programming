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
        print("Removed [{}] from the list.".format(list))
        super().remove(list)
    def pop(self, index=None):
        if index is None:
            element = super().pop()
        else:
            element = super().pop(index)
        print("Popped [{}] from the list.".format((element)))