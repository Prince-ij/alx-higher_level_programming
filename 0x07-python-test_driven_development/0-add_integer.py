#!/usr/bin/env python3
def add(a, b=98):
   """ add two numbers and return float
        numbers must be either float or int
                """

   if not isinstance(a, (int, float)) and not /
   isinstance(b, (int, float)):
       raise TypeError("a must be an integer or be 
       must be an integer")
    a = int(a)
    b = int(b)
    return a + b
