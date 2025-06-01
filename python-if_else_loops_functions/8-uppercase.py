#!/usr/bin/python3
def uppercase(str):
    for index in str:
        if index >= 'a' and index <= 'z':
            index = chr(ord(index) - 32)
        print("{}".format(index), end="")
    print("".format(index))
