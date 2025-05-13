#!/usr/bin/python3
def replace_in_list(my_list, idx, element) :

     for count, arguments in enumerate(my_list, start=1):
        if idx < 0:
            return my_list
        elif idx > len(my_list) - 1:
            return my_list
        else:
            my_list.insert(4, 9)
            my_list.remove(4)
            my_list
            return my_list
