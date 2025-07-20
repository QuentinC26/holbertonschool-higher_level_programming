#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for index in range(list_length):
        if index >= len(my_list_1) or index >= len(my_list_2):
            print("out of range")
            new_list.append(0)
            continue
        if not isinstance(my_list_1[index], (int, float)):
            print("wrong type")
            new_list.append(0)
            continue
        if not isinstance(my_list_2[index], (int, float)):
            print("wrong type")
            new_list.append(0)
            continue
        try:
            if my_list_2[index] == 0:
                print("division by 0")
                new_list.append(0)
            else:
                result = my_list_1[index] / my_list_2[index]
                new_list.append(result)
        except IndexError:
            pass
        finally:
            pass
    return new_list
