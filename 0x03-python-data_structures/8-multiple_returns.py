#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        length == None
    first = sentence[0]
    data = (length, first)
    return data
