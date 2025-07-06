#!/usr/bin/python3
'''
print a text with 2 new lines after each of these characters: ., ? and :
'''


def text_indentation(text):
    return_of_line_after = [".", ":", "?"]
    for index, characters in enumerate(text):
        if characters in return_of_line_after:
            print(i, end="\n")
            print()
        elif characters == " ":
            if text[index-1] in return_of_line_after:
                continue
            else:
                print(characters, end="")
        else:
            print(characters, end="")
