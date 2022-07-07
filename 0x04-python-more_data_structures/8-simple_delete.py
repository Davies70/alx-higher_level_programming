#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key not in (a_dictionary.items()):
        return a_dictionary
    elif a_dictionary == {}:
        return a_dictionary
    else:
        del a_dictionary[key]
        return a_dictionary
