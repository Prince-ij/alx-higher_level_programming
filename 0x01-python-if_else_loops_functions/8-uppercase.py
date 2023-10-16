#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if 96 < ord(i) < 123:
            i = chr(ord(i) - 32)
        print("{:c}".format(i), end='')
    print()
