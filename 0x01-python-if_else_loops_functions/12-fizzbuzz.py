#!/usr/bin/python3
for i in range(1, 100):
    if i % 3 == 0 or i % 5 == 0:
        print("FizzBuzz", end=' ')
    else:
        print(f"{i}", end=' ')
