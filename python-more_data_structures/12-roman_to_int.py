#!/usr/bin/python3
def roman_to_int(roman_string):
    count = 0
    if not isinstance(roman_string, str) or roman_string is None:
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
    for index in roman_string:
        if index == "I":
            roman_string = roman_conversion.get('I')
        elif index == "V":
            roman_string = roman_conversion.get('V')
        elif index == "X":
            roman_string = roman_conversion.get('X')
        elif index == "L":
            roman_string = roman_conversion.get('L')
        elif index == "C":
            roman_string = roman_conversion.get('C')
        elif index == "D":
            roman_string = roman_conversion.get('D')
        elif index == "X":
            roman_string = roman_conversion.get('M')
    return roman_string
