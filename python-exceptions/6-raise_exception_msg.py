#!/usr/bin/python3
def raise_exception_msg(message=""):
    word = "hello"
    if not type(word) is int:
        raise NameError(message)
