#!/usr/bin/python3
for numbers in range(0, 10):
    for numbers_two in range(numbers + 1, 10):
        space = ""
        if (numbers != numbers_two):
            print("{:d}{:d}, ".format(numbers, numbers_two), end="")
        elif (numbers == numbers_two and numbers <= 8 or numbers_two >= 8):
            print("{}".format(space), end="")
        if (numbers == 8 and numbers_two == 9):
            print("{:d}{:d}, ".format(numbers, numbers_two))