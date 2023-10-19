#!/usr/bin/python3
def uniq_add(my_list=[]):
    res = 0
    ls = set(my_list)
    for i in ls:
        res += i
    return res
