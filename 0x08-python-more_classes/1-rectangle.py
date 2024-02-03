#!/usr/bin/python3
""" A Rectangle class """


class Rectangle:
    """ This creates a rectangle class """

    def __init__(self, width=0, height=0):
        """ Initializes width & height """

        self.width = width
        self.height = height

    @property
    def width(self):
        return self.width

    @property
    def height(self):
        return self.height

    @width.setter
    def width(self, value):
        if !(isinstance(value, int)):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.width = value

    @height.setter
    def height(self, value):
        if !(isinstance(value, int)):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.height = height
