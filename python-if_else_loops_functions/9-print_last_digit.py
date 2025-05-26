#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        last = number % -10
        last = last * (-1)
        print(last, end="")
        return last
    else:
        print(number % 10, end="")
        return number % 10
