#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = set()
    shared = set(set_1) & set(set_2)
    for i in set_1:
        if i not in shared:
            new_set.add(i)
    for j in set_2:
        if j not in shared:
            new_set.add(j)
    return new_set

