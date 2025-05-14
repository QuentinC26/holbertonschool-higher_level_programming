#!/usr/bin/python3
def max_integer(my_list=[]):

    if len(my_list) == 0:
        return None
    
    max_val = my_list[0]
    # max_val = maximum_value
    for index in my_list:
        if index > max_val:
            max_val = index
    return max_val