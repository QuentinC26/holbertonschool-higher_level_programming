#!/usr/bin/python3
for numbers in range(0, 9):
    for numbers_two in range(numbers + 1, 10):
        if (numbers == 8 and numbers_two == 9):
            print("{:d}{:d} ".format(numbers, numbers_two))
        else:
            print("{:d}{:d}, ".format(numbers, numbers_two), end="")
