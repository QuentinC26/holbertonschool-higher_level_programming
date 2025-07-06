#!/usr/bin/python3
'''
print a text with 2 new lines after each of these characters: ., ? and :
'''


def text_indentation(text):
    '''
    print a text with 2 new lines after each of these characters: ., ? and :
    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    print(text.replace(". ", ".\n\n").replace("? ", "?\n\n").replace(": ", ":\n\n"), end="")
