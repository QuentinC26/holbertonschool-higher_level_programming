#!/usr/bin/python3
from abc import ABC, abstractmethod

class CountedIterator(ABC):
    def __init__(self, iterator, counter=0):
        self.iterator = iter(iterator)
        self.counter = counter

    def get_count(self):
        return self.counter

    def __next__(self):
        next(self.iterator)
        self.counter = counter + 1
        if not next(self.iterator):
            raise StopIteration("")
        else:
            return next(self.iterator)