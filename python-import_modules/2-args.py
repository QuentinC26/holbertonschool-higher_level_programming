#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]
    number_argument = len(argv)

    if number_argument == 0:
        print("0 arguments.")
    elif number_argument == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(number_argument))

    for index, arguments in enumerate(argv, start=1):
        print("{}: {}".format(index, arguments))
