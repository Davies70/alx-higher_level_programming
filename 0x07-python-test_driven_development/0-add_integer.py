#!/usr/bin/python3
"""module created
"""


def add_integer(a, b=98):
    """ function that adds integers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")
    return int(a) + int(b)
