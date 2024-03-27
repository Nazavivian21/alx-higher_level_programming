#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_matrix = []
    for row in matrix:
        for col in row:
            squared_matrix.append([col**2])
    return squared_matrix
