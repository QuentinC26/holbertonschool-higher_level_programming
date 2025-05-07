#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastnumber = number % 10

if (lastnumber > 5):
    print(f"Last digit of {number} is {lastnumber} and is greater than 5")
if (lastnumber == 0):
    print(f"Last digit of {number} is {lastnumber} and is 0")
if (lastnumber != 0 & number < 6):
    print(f"Last digit of {number} is {lastnumber} and is less than 6 and not 0")
