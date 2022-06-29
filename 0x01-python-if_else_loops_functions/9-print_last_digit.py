#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        whole = number * -1
        last = whole % 10
    else:
        last = number % 10
    print("{}".format(last), end="")
    return last
