#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    if my_list == None:
        return None
    if x == 0:
        return None
    try:
        while (i < x):
            print(my_list[i], end='')
            i += 1
        print()
        return i
    except:
        print()
        return i
