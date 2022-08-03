#!/usr/bin/python3
""" JSON Module """


import json


def from_json_string(my_str):
    """ returns python representation of JSON string """
    return json.loads(my_str)
