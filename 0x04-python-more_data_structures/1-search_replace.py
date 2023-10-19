#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for i in my_list:
        if search == i:
           my_list[my_list.index(i] = replace
           new_list.append(i)
    return new_list
