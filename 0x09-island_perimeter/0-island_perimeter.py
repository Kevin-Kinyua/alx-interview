#!/usr/bin/python3
"""Island Perimeter """

def island_perimeter(grid):
    """ island_perimeter()

    Parameters:
      - grid: Grid representing the island for which we want the perimeter.

    Returns:
      - perimeter of the island.
    """
    def get_perimeter(i, j):
        """ get_perimeter()

        Parameters:
          - i: current row being evaluated
          - j: current column being evaluated

        Returns:
          - 1, 0 or sum of perimeter of the current cell under consideration.
        """
        if (i < 0 or i > len(grid) - 1) or (j < 0 or j > len(grid[i]) - 1):
            return 1
        if grid[i][j] == 0:
            return 1
        if grid[i][j] == 'v':
            return 0
        grid[i][j] = 'v'
        return (get_perimeter(i, j-1) + get_perimeter(i-1, j)
                + get_perimeter(i, j+1) + get_perimeter(i+1, j))

    result = 0
    if type(grid) != list:
        return 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                result = get_perimeter(row, col)
    return result

