#!/usr/bin/python3
""" module of func that reads files """


def read_file(filename=""):
    """ function takes arg filename """
    with open(filename, 'r', encoding="utf-8") as file1:
        read_file = file1.read()
    print(read_file)
