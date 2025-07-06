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
    for index in text:
        if index == "?":
            print(text)
            print("")
            print("")
        elif index == ":":
            print(text)
            print("")
            print("")
        elif index == ",":
            print(text)
            print("")
            print("")
        else:
            print(text)
