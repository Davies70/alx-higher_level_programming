#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    whole = number * -1
    last = (number % 10) * -1
else:
    whole = number
    last = number % 10
if last > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, last))
elif last == 0:
    print("Last digit of {} is {} and is 0".format(number, last))
elif last < 6 and last_digit != 0:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, lasti))
