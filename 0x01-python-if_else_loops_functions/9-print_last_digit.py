#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        ld = -(abs(number) % 10)
    else:
        ld = number % 10
    print(f"{number}", end='')
    return ld
