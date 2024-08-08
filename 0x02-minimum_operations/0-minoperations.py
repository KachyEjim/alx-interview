#!/usr/bin/python3

""" Minimum Operations """


def minOperations(n):
    """RETURN THE NUMBER OF STEPS"""

    if not isinstance(n, int) or n <= 1:
        return 0

    operations: int = 0
    factor: int = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n = n // factor
        factor += 1

    return operations
