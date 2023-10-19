#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    start = 0
    var = 0
    for i in new_list:
        if search == i:
            new_list[my_list.index(i, start)] = replace
            var = my_list.index(i, start)
            start = var + 1
    return new_list
