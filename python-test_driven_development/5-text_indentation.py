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
    if text == "" or text.isspace():
        print("")
        return
    new_text = ""
    for index in text:
        if new_text == "" and index == " ":
            continue
        new_text = new_text + index
        if index in ['.', '?', ':']:
            print(new_text.strip() + "\n")
            new_text = ""
    if new_text.strip():
        print(new_text.strip(), end="")
