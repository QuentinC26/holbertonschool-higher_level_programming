#!/usr/bin/python3
import json
'''
Function for write a filetext
'''


def to_json_string(my_obj):
    '''
    Function for write a filetext
    '''
    with open('my_obj.json', 'w', encoding="UTF-8") as the_text:
        json.dumps(the_text, indent=4,ensure_ascii=False)
    return the_text
