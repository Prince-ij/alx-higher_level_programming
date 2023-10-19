#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    new_matrix = list(map((lambda row: map(lambda x: x ** 2, row), matrix)))
        return new_matrix
