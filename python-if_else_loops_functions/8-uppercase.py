#!/usr/bin/python3
def uppercase(str):
    for index in str:
        if ord(index) >= 65 and ord(index) <= 90:
            print("{}".format(str))
            return True
    print("{}".format(str))
