#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]

    if len(argv) == 0:
        print("0")
    else:
        for index in argv:
            if index != int:
                print("")
            else:
                print(sum(int(argv)))
