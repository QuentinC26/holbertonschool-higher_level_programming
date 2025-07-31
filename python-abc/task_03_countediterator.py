#!/usr/bin/python3
from abc import ABC, abstractmethod

class CountedIterator(ABC):
    @abstractmethod
    def __init__(self, iterator, counter=0):
        self.iterator = iter(iterator)
        self.counter = counter
        super().__init__()

    def get_count(self):
        return self.counter

    def __next__(self):
        next(self.iterator)
        if next(self.iterator):
            counter = counter + 1
            return counter
        else:
            raise StopIteration("")