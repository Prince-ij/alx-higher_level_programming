#!/usr/bin/python3
"""
    This module contains a function that adds two numbers

"""


def add_integer(a, b=98):
    """
        Function that adds two numbers

        Args:
            a: First number
            b: Second number

        Returns:
            Addition of two given numbers

        Raises:
            TypeError: if a or b  is not int/float

    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an int/float")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an int/float")

    a = int(a)
    b = int(b)

    return a + b
