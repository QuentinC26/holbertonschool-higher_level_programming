#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    try:
        new_list = []
        for index in my_list_1:
            for index_2 in my_list_2:
                if not index / index_2:
                    return 0
                result = index / index_2
            new_list.append(result)
        return new_list
    except ZeroDivisionError:
        print("division by 0")
        if not isinstance(my_list_1, (int, float)) or not isinstance(my_list_2, (int, float)):
            print("wrong type")
        if index >= len(my_list_1) or index_2 >= len(my_list_2):
            print("out of range")
    finally:
        return new_list