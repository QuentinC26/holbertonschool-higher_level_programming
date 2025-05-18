#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    try:
        new_list = []
        for index_1, arguments_1 in my_list_1:
            pass
        for index_2 in my_list_2:
            pass
    except TypeError:
        pass
    finally:
        if 0 in my_list_2:
            print("division by 0")
        if not isinstance(my_list_1, (int, float)) or not isinstance(my_list_2, (int, float)):
            print("wrong type")
        if index_1 >= len(my_list_1) or index_2 >= len(my_list_2):
            print("out of range")
        return list_length
