#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    for count, arguments in enumerate(my_list, start=1):
        if idx < 0:
            return my_list
        elif idx > len(my_list) - 1:
            return my_list
        else:
            copy = my_list.copy()
            copy.insert(4, 9)
            copy.remove(4)
            return copy
