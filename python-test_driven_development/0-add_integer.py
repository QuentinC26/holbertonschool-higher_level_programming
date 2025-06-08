#!/usr/bin/python3
'''
i add two integers
'''


def add_integer(a, b=98):
    '''
    i add two integers
    '''
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("a must be an integer")
    else:
        number_a = int(a)
        number_b = int(b)
        return number_a + number_b
