#!/usr/bin/python3
for numbers in range(0, 100):
    if (numbers <= 98):
        hexa = hex(numbers)
        hexa = hex(numbers).lstrip('0x').upper()
        print("{:d}, ".format(numbers, hexa), end="")
    elif (numbers == 99):
        print("{:d}".format(numbers), )


