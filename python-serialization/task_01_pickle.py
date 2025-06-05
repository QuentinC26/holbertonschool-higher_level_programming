#!/usr/bin/python3
import pickle

class CustomObject:

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def serialize(self, filename):
        with open(filename, 'wb') as text_file:
            write_data = pickle.dumps(text_file)
    
    @classmethod
    def deserialize(cls, filename):
        with open(filename, 'rb') as text_file:
            read_data = pickle.load(text_file)
        return read_data
