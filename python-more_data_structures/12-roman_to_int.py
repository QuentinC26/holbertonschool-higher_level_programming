#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) or roman_string == None:
        return 0
    
    return roman(roman_string)