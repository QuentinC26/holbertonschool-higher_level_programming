#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for index in range(x):
        try:
            if index >= x:
                break
            print("{:d}".format(my_list[index]), end="")
            count = count + 1
            if isinstance(my_list, int):
                print("{:d}".format(x))
        except ValueError:
            pass
        except TypeError:
            pass
    print("")
    return count
