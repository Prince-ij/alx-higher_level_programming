#!/usr/bin/python3
""" Module for task 2 def matrix_divided(matrix, div) """


def matrix_divided(matrix, div):
    """ Divide all elements of Matrix by div """

    for i in matrix:
        for j in i:
            if not (isinstance(j, int) or isinstance(j, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    length = [length(row) for row in matrix]
    length = length[0]
        for i in matrix:
            if length(i) != length:
                raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(int, div) or isintance(div, float):
        raise TypeError("div must be a number")

