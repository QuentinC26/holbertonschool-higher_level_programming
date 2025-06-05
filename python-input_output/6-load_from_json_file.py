#!/usr/bin/python3
'''
Function for read a filetext
'''
import json


def load_from_json_file(filename):
    '''
    Function for read a filetext
    '''
    with open(filename, 'r') as text_file:
        read_data = json.load(text_file)
    return read_data
