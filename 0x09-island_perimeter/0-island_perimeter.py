#!/usr/bin/python3
"""Python file"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the grid.

    Args:
    grid (list of list of int): 2D grid representing land(1) and water(0)

    Returns:
    int: The perimeter of the island
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0  # Number of columns

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                if r == 0 or grid[r - 1][c] == 0:
                    perimeter += 1
                if r == rows - 1 or grid[r + 1][c] == 0:
                    perimeter += 1
                if c == 0 or grid[r][c - 1] == 0:
                    perimeter += 1
                if c == cols - 1 or grid[r][c + 1] == 0:
                    perimeter += 1

    return perimeter
