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
    new_text = ""
    for index in text:
        new_text = new_text + index
        if index in ['.', '?', ':']:
            new_text = new_text.strip()
            print(new_text)
            print()
            new_text = ""
    if new_text.strip():
        print(new_text.strip())