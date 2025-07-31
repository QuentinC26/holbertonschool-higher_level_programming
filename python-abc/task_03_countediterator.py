#!/usr/bin/python3
from abc import ABC, abstractmethod

class CountedIterator(ABC):
    def __init__(self, iterator, counter):
        self.iterator = iter(iterator)
        self.counter = counter

    def get_count(self):
        return self.counter

    def __next__(self):
        pass