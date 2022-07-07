#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary == {}:
        return a_dictionary
    new_list = []
    for key, value in a_dictionary.items():
        new_list.append([key, value])
    for x in new_list:
        x[1] = x[1] * 2
    jay = dict(new_list)
    return jay
