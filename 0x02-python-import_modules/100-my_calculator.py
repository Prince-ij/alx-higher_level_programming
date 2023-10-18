#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import mul, sub,add, div
if __name__ == "__main__":
    a, b, op = int(argv[1]), int(argv[3]), argv[2]
    la = len(argv) - 1
    ops = ['+', '-', '/', '*']
    choice = {'+': add, '-': sub, '*': mul, '/': div}
    for r in choice:
        if r == op:
            res = choice[r](a, b)
            break
    if la != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    elif op not in ops:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    else:
        print(f"{a} {op} {b} = {res}")
