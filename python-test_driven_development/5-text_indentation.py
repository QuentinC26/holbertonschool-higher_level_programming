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
    return_of_line_after = [".", ":", "?"]
    for index, characters in enumerate(text):
        if characters in return_of_line_after:
            print(characters, end="\n")
            print()
        elif characters == " ":
            if text[index-1] in return_of_line_after:
                continue
            else:
                print(characters, end="")
        else:
            print(characters, end="")
