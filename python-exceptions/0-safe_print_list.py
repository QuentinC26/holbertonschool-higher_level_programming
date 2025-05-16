#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for index, arguments in enumerate(my_list):
            if index >= x:
                break
            print("{}".format(arguments), end="")
            count = count + 1
        print("")
    except TestError:
        return count
