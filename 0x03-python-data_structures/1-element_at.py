#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    p = len(my_list)
    if idx > (p - 1):
        return None
    else:
        return my_list[idx]
