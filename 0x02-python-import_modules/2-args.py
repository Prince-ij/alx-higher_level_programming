#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    L = len(argv) - 1
    if L < 1:
        print(f"{L} arguments.")
    elif L == 1:
        print(f"{L} argument:\n{L}: {argv[1]}")
    else:
        print(f"{L} arguments:")
        for i in range(1, L + 1):
            print(f"{i}: {argv[i]}")
