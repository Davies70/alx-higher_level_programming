#!/usr/bin/python3
def multiple_returns(sentence):
    if isinstance(sentence, str):
        length = len(sentence)
        if length == 0:
            first == None
        else:
            first = sentence[0]
        return (length, first)
