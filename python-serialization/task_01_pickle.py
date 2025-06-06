#!/usr/bin/python3
import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        try:
            with open(filename, 'wb') as text_file:
                write_data = pickle.dump(self, text_file)
        except TypeError:
            return None

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, 'rb') as text_file:
                read_data = pickle.load(text_file)
            return read_data
        except TypeError or ValueError:
            return None
