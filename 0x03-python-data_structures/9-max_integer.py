#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        p = len(my_list) - 1
        j = 0
        while p > 1:
            while j < p:
                if my_list[j] > my_list[j + 1]:
                    temp = my_list[j]
                    my_list[j] = my_list[j + 1]
                    my_list[j + 1] = temp
                j += 1
            p -= 1
        k = len(my_list) - 1
        return my_list[k]
