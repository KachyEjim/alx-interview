#!/usr/bin/python3
"""Function that returns a pascal triangle when given an input"""


def pascal_triangle(n):
    """
    Calculates and returns a pascal triangele

    """
    if n <= 0:
        return []
    triangle = []
    for x in range(n):
        row = [1] * (x + 1)
        for i in range(1, x):
            row[i] = triangle[x - 1][i - 1] + triangle[x - 1][i]
        triangle.append(row)
    return triangle
