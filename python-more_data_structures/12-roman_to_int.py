#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string == None:
        return 0
    roman_conversion = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
       'M': 1000
       }
    for index in roman_conversion:
        roman_string = filter(lambda conversion: int(index), roman_string)
    return roman_string