#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = {}

    if a_dictionary is None:
        return
    for key, value in a_dictionary.items():
        new_dictionary[key] = value*2
    return new_dictionary
