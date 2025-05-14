#!/usr/bin/python3
def no_c(my_string):

    letters = ""

    for characters in my_string:
        if characters != 'c' and characters != 'C':
            letters += characters
            # ça correspond à : letters = letters + characters
    return letters
