#!/usr/bin/python3
""" is_kind_of_class module """


def is_kind_of_class(obj, a_class):
    """ is_kind_of_class function with 2 args"""
    if isinstance(obj, a_class) or type(obj) == a_class:
        return True
    else:
        return False
