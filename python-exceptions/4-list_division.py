#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for index in range(list_length):
        if index > len(my_list_1) or index > len(my_list_2):
            print("out of range")
            new_list.append(0)
        if not isinstance(my_list_1[index], (int, float)):
            print("wrong type")
            new_list.append(0)
        if not isinstance(my_list_2[index], (int, float)):
            print("wrong type")
            new_list.append(0)
        try:
            if index == 0:
                new_list.append(0)
            result = my_list_1[index] / my_list_2[index]
        except ZeroDivisionError:
            print("division by 0")
        finally:
            new_list.append(result)
    return new_list