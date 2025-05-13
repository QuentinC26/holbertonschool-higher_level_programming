#!/usr/bin/python3
def element_at(my_list, idx):

    for count, arguments in enumerate(my_list, start=1):
        if idx < 0:
            return None
        elif idx > len(my_list) - 1:
            return None
        else:
            return idx + 1
