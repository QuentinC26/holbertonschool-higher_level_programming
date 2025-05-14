#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx > len(my_list):
        return my_list
    if idx < 0:
        return my_list
    my_list.remove(4)
    my_list
    return my_list