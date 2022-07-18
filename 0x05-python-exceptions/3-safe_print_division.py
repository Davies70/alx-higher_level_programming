#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        c = a / b
        result = c
        print("Inside result: {}".format(c))
    except ArithmeticError:
        print("Inside result: {}".format(None))
        result = None
    finally:
        return result

