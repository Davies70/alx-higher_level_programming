#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    p = len(my_list) - 1
    if idx > p:
        return my_list
    else:
        isinstance(my_list, list)
        my_list_2 = []
        for i in my_list:
            my_list_2.append(i)
    my_list_2[idx] = element
    return my_list_2
