#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    try:
        new_list = []
        for index in my_list_1:
            for index_2 in my_list_2:
                if index_2 == 0:
                    new_list.append(0)
                result = index / index_2
                new_list.append(result)
        return new_list
    except ZeroDivisionError:
        print("division by 0")
    except TypeError:
        print("wrong type")
    except IndexError:
        print("out of range")
    finally:
        return new_list
