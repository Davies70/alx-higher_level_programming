#!/usr/bin/python3
"""module created
   contains the funtion add_integer

"""


def add_integer(a, b=98):
    """function that adds integers
       takes the args a, b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
