#!/usr/bin/python3
""" module of function that appends to file """


def append_write(filename="", text=""):
    """ funtion takes agrs filename, text) """
    with open(filename, 'a', encoding="utf-8") as file1:
        file1.write(text)
    with open(filename, 'r', encoding="utf-8") as file2:
        data = file2.read()
    return len(text)
