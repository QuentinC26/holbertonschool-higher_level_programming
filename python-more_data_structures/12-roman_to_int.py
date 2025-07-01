#!/usr/bin/python3
def roman_to_int(roman_string):
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
    int_list = []
    for key, value in roman_conversion.items():
        for index in reversed(roman_string):
            if index == key:
                index = value
                int_list.append(index)
    for count in reversed(int_list):
        if int_list == 0 or 1:
            roman_string = sum(int_list)
            return roman_string
        elif int_list[0] < int_list[1]:
            roman_string = int_list[1] - int_list[0]
            return roman_string
        else:
            roman_string = sum(int_list)
            return roman_string