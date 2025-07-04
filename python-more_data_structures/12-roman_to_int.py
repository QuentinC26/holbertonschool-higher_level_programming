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
    for index in roman_string:
        for key, value in roman_conversion.items():
            if index == key:
                index = value
                int_list.append(index)
    for count in range(len(int_list)):
        if count != len(int_list) - 1:
            if int_list[count] < int_list[count + 1]:
                int_list[count + 1] = int_list[count + 1] - int_list[count]
                int_list[count] = 0
                count = count + 1
    return sum(int_list)
