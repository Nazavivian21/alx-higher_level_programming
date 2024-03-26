#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        first_char = None
        tup = length, first_char
        return tup
    else:
        length = len(sentence)
        first_char = sentence[0]
        tup = length, first_char
        return tup
