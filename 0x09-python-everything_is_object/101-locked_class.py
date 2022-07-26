#!/usr/bin/python3
"""module of LockedClass"""


class LockedClass:
    """ class that prevents dynamica
        instance allocation
    """
    __slot__ = ['first_name']
