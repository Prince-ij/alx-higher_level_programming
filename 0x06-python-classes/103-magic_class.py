#!/usr/bin/python3
"""
Defines a MagicClass that replicates the given Python bytecode functionality.
"""

import math


class MagicClass:
    """
    A class that replicates the functionality as the given Python bytecode.
    """

    def __init__(self, radius=0):
        """
        Initializes a new instance of MagicClass with the provided radius.

        Args:
            radius (int or float): The radius of the MagicClass object.
        Raises:
            TypeError: If the radius is not a number.
        """
        if not isinstance(radius, (int, float)):
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculates and returns the area of the MagicClass object.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates and returns the circumference of the MagicClass object.
        """
        return 2 * math.pi * self.__radius


if __name__ == '__main__':
    magic = MagicClass(5)
    print(magic.area())
    print(magic.circumference())
