#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
        print("Inside result: {}".format(result))
        return result
    except ArithmeticError:
        print("Inside resut: {}".format(None))
        return None
