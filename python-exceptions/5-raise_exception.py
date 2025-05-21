#!/usr/bin/python3
def raise_exception():
    word = "hello"
    if not type(word) is int:
        raise TypeError
