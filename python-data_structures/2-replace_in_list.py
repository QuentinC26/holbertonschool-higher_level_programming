#!/usr/bin/python3
def replace_in_list(my_list, idx, element) :

     for count, arguments in enumerate(my_list, start=1):
        if idx < 0:
            return my_list
        elif idx > len(my_list) - 1:
            return my_list
        else:
            element = idx + 1
            return my_list
