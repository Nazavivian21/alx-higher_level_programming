#!/usr/bin/python3
"""The pascal_triangle method module"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing the Pascal’s \
        triangle of n"""
    if n <= 0:
        return []

    result = [[1]]
    for i in range(1, n):
        prev_row = result[-1]
        current_row = [1]

        for j in range(1, i):
            current_row.append(prev_row[j - 1] + prev_row[j])

        current_row.append(1)
        result.append(current_row)

    return result
