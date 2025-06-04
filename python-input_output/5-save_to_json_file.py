#!/usr/bin/python3
'''
Function for write a filetext
'''
import json


def save_to_json_file(my_obj, filename):
    '''
    Function for write a filetext
    '''
    with open('filename', 'w', encoding="UTF-8") as text_file:
        write_data = text_file.write(filename)
    return json.dumps(my_obj)
