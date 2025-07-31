#!/usr/bin/python3
from abc import ABC, abstractmethod

class CountedIterator(ABC):
    def __init__(self, iterator, counter=0):
        self.iterator = iter(iterator)
        self.counter = counter

    def get_count(self):
        return self.counter

    def __next__(self):
        new_iterator = next(self.iterator)
        self.counter = self.counter + 1
        if not new_iterator:
            raise StopIteration("")
        else:
            return new_iterator
            