#!/usr/bin/python3
'''
print a text with 2 new lines after each of these characters: ., ? and :
'''


def text_indentation(text):
    '''
    prints a text with 2 new lines after each of these characters: ., ? and :
    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    new_text = text.replace(".", ".\n\n").replace("?", "?\n\n").replace(":", ":\n\n")
    print(new_text)
