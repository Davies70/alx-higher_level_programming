#!/usr/bin/python3
""" module of function that writes to file """


def write_file(filename="", text=""):
    """ funtion takes agrs filename, text) """
    with open(filename, 'w', encoding="utf-8") as file1:
        file1.write(text)
    with open(filename, 'r', encoding="utf-8") as file2:
        data = file2.read()
    return len(data)
