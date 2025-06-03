#!/usr/bin/python3
'''
Function for write a filetext
'''


def write_file(filename="", text=""):
    '''
    Function for write a filetext
    '''
    with open(filename, 'w', encoding="UTF-8") as the_text:
        write_data = the_text.write(text)
    return len(text)
