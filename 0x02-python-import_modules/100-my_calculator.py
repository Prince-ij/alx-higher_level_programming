#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import mul, sub, add, div
if __name__ == "__main__":
    la = len(argv)
    if la != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    choice = {'+': add, '-': sub, '*': mul, '/': div}
    ops = ['+', '-', '/', '*']
    a, b, op = int(argv[1]), int(argv[3]), argv[2]
    for r in choice:
        if r == op:
            res = choice[r](a, b)
            break
    if op not in ops:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    else:
        print(f"{a} {op} {b} = {res}")
