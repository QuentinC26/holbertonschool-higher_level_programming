#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]
    number_argument = len(argv)

    if number_argument == 0:
        print("0")
    elif number_argument != int:
        print("")
    else:
        for index in range(number_argument):
            print(sum(number_arguments))
