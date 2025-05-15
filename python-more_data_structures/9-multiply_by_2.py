#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = []

    if a_dictionary is None:
        return
    for index, value in sorted(a_dictionary.items()):
        new_dictionary.append(value*2)
    return new_dictionary
