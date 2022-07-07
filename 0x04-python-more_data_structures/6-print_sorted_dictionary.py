#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_value = sorted(a_dictionary.items())
    for k in (new_value):
        print("{}: {}".format(k[0], k[1]))
