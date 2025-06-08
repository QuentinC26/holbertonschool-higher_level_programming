#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]

    my_sum = []
    if len(argv) == 0:
        print("0")
    else:
        for index in sys.argv[1:]:
            if index != int:
                conversion = int(index)
                my_sum.append(conversion)
        print(sum(my_sum))
