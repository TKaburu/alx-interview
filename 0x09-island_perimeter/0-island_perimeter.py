#!/usr/bin/python3

"""Island perimeter function"""


def island_perimeter(grid):
    """
    This function calculates the boder/perimeter of an island
    """
    rows = len(grid)
    # check if the grid is not empty
    if rows > 0:
        # set colums if grid is not empty
        columns = len(grid[0])
    else:
        columns = 0

    perimeter = 0  # will keep track of the total perimeter of the island

    # land == 1 water == 0
    for row in range(rows):
        for column in range(columns):
            if grid[row][column] == 1:
                # we add 4 cause an island has 4 sides
                perimeter = perimeter + 4
                # check if above is a land
                if row > 0 and grid[row-1][column] == 1:
                    # minu 2 because we have 2 boders side by side since
                    # both are land
                    perimeter = perimeter - 2
                # checks if to the left is land
                if column > 0 and grid[row][column-1] == 1:
                    perimeter = perimeter - 2

    return perimeter
