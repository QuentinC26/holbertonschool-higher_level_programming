#!/usr/bin/python3
'''
Function for write a filetext
'''
import json


def save_to_json_file(my_obj, filename):
    '''
    Function for write a filetext
    '''
    with open('my_obj.json', 'w', encoding='utf-8') as filename:
        write_data = json.dump(my_obj, filename)
    return write_data