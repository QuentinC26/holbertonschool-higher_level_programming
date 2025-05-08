#!/usr/bin/python3
for numbers in range(0, 100):
    if (numbers <= 9):
        pass
    elif (numbers <= 98):
        print("{}, ".format(numbers), end="")
    elif (numbers == 99):
        print("{}".format(numbers))
