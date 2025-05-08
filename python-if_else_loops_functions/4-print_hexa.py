#!/usr/bin/python3
for numbers in range(0, 99):
    hexadecimal = hex(numbers)
    print("{:d} = {hexadecimal}".format(numbers, hexadecimal))
