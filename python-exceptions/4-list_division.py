#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for index in range(list_length):
        if not isinstance(my_list_1[index], (int, float)):
            new_list.append(0)
            print("wrong type")
        if not isinstance(my_list_2[index], (int, float)):
            new_list.append(0)
            print("wrong type")
        try:
            if index == 0:
                new_list.append(0)
            result = my_list_1[index] / my_list_2[index]
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(result)
    return new_list