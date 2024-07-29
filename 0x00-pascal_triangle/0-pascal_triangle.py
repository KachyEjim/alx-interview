#!/usr/bin/python3
"""Function that returns a pascal triangle when given an input"""


def pascal_triangle(n: int) -> list[list[int]]:
    """
    Calculates and returns a pascal triangele

    """
    triangle = [[1]] if n > 0 else []
    for x in range(1, n):
        row = [1] * (x + 1)
        for i in range(1, x):
            row[i] = triangle[x - 1][i - 1] + triangle[x - 1][i]
        triangle.append(row)
    return triangle
