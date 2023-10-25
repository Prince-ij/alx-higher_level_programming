#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes a new Square.

        Args:
            size (float or int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square."""
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates the area of the square."""
        return self.__size * self.__size

    def __lt__(self, other):
        """Less than comparison for squares."""
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal comparison for squares."""
        return self.area() <= other.area()

    def __eq__(self, other):
        """Equality comparison for squares."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Not equal comparison for squares."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Greater than comparison for squares."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal comparison for squares."""
        return self.area() >= other.area()


if __name__ == '__main__':
    s_5 = Square(5)
    s_6 = Square(6)

    if s_5 < s_6:
        print("Square 5 < Square 6")
    if s_5 <= s_6:
        print("Square 5 <= Square 6")
    if s_5 == s_6:
        print("Square 5 == Square 6")
    if s_5 != s_6:
        print("Square 5 != Square 6")
    if s_5 > s_6:
        print("Square 5 > Square 6")
    if s_5 >= s_6:
        print("Square 5 >= Square 6")
