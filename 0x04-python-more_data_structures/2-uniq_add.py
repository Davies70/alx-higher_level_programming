#!/usr/bin/python3
def uniq_add(my_list=[]):
    y = 0
    hard_list = (set(my_list))
    for i in hard_list:
        y = y + i
    return y
