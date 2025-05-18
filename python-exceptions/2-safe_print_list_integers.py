#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for index, arguments in enumerate(my_list):
            if index >= x:
                break
            print("{:d}".format(arguments), end="")
            if isinstance(my_list, int):
                print("{:d}".format(my_list))
                return True
            count = count + 1
    except TypeError:
        pass
    print("")
    return count
