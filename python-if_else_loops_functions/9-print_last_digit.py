#!/usr/bin/python3
def print_last_digit(number):
    last = number % 10
    if last < 0:
        last = last * (-1)
        print(last, end="")
        return last
    else:
        print(last, end="")
        return last
