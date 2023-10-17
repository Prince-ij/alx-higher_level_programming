#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""
    for i, j in enumerate(str):
        if i != n:
            new_str += j
    return new_str
