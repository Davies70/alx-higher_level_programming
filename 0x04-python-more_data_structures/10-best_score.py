#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    Best_score = 0
    Best_key = None
    for key, value in a_dictionary.items():
        if value > Best_score:
            Best_score = value
            Best_key = key
    return Best_key
