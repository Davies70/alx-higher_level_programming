#!/usr/bin/python3
""" module for saving object to file """


import json


def save_to_json_file(my_obj, filename):
    """ function takes 2 args """
    with open(filename, 'w', encoding="utf-8") as file1:
        file1.write(json.dumps(my_obj))
