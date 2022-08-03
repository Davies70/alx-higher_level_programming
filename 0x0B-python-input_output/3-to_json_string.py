#!/usr/bin/python3
""" JSON Module """


import json


def to_json_string(my_obj):
    """ returns JSON representation of my_obj """
    return json.dumps(my_obj)
