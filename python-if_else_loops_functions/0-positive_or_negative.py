#!/usr/bin/python3
import random
number = random.randint(-10, 10)

# the condition is for print the number is negative, zero or positive

if number < 0:
    print(f"{number} is negative")
if number == 0:
    print(f"{number} is zero")
if number > 0:
    print(f"{number} is positive")
