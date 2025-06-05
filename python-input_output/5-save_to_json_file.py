#!/usr/bin/python3
'''
Function for write a filetext
'''
import json


def save_to_json_file(my_obj, filename):
    '''
    Function for write a filetext
    '''
    with open(filename, 'w') as text_file:
        json.dump(my_obj, text_file)