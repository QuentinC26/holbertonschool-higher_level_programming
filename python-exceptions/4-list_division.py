#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for index in range(list_length):
        if not isinstance(my_list_1, int) or not isinstance(my_list_1, float):
            print("wrong type")
        if not isinstance(my_list_2, int) or not isinstance(my_list_2, float):
            print("wrong type")
        try:
            if index == 0:
                new_list.append(0)
            result = index / index_2
            new_list.append(result)
            return new_list
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            return new_list
