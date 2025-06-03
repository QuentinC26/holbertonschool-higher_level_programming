#!/usr/bin/python3
'''
Function for write a filetext
'''


def append_write(filename="", text=""):
    '''
    Function for write a filetext
    '''
    with open(filename, 'a', encoding="UTF-8") as the_text:
        write_data = the_text.write(text)
    return len(text)
