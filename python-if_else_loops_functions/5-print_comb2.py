#!/usr/bin/python3
for numbers in range(0, 100):
    if (numbers <= 9):
       print("0{:d}, ".format(numbers), end="")
    elif (numbers <= 98):
        print("{:d}, ".format(numbers), end="")
    else:
        print("99 ")


