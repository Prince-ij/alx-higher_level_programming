#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        print(my_list)
    else:
        for i in reversed(my_list):
            print("{:d}".format(i))
