#!/usr/bin/python3
"""
    A Python function that calculates the perimeter of an island in a 2D grid. The grid represents water (0) and land (1), and the function determines the boundary length of the landmass.
"""

def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in grid.
    Args:
        grid: 2D list of integers containing 0 (water) or 1 (land).
    Return:
        The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check top
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                # Check bottom
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                # Check left
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                # Check right
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter

