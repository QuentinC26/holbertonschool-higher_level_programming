#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    number_argument = len(sys.argv[1:])

    if len(sys.argv[0:]):
        print("{} arguments.".format(number_argument))
    if number_argument == 1 :
        print("{} argument:".format(number_argument))
        print("{}: {}".format(number_argument, sys.argv[1:]))
    if number_argument >= 2:
        print("{} arguments:".format(number_argument))
        print("{}: {}".format(number_argument, sys.argv[1:]))
