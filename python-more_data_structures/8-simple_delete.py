#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key == "":
        return a_dictionary
    else:
        key = a_dictionary.pop("track", None)
        return a_dictionary
