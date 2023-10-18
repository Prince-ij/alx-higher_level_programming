#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    mod = dir(hidden_4)
    for mods in mod:
        if not mods.startswith('__'):
            print(mods)
