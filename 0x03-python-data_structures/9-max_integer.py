#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None

    maxInt = my_list[0]
    for i in my_list:
        if i > maxInt:
            maxInt = i
    return maxInt
