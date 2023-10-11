#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    for r in set(my_list):
        new_list.append(r)

    return new_list
