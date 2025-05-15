#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    my_dictionary = {}

    for index, value in sorted(a_dictionary.items()):
        print(f"{index}: {value}")
