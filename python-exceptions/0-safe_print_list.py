#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for index, arguments in enumerate(my_list, start=1):
            print("{:d}".format(arguments), end="")
            if index == 2:
                break
        print("")
        return x
    except:
        print("Your code is wrong !!")

    