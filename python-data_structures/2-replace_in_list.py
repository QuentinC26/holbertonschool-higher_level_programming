#!/usr/bin/python3
def replace_in_list(my_list, idx, element) :

    if 0 <= idx < len(my_list):
        #ce qui correspond à if idx >= 0 et if idx < len(my_list)
        my_list[idx] = element
        return my_list
    else:
        return my_list

