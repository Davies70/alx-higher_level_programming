#!/usr/bin/python3
""" sort class module
"""


class MyList(list):
    """class created
    """
    def print_sorted(self):
        """function that sorts list"""
        print(sorted(self))
