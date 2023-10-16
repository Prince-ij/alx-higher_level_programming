#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if 96 < ord(i) < 123:
            i = ord(i) - 32
        print("{:c}".format(chr(i)), end='')
    print()
