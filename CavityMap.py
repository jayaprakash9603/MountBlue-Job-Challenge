#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cavityMap' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY grid as parameter.
#

def cavityMap(grid):
    # Write your code here
    n = len(grid)
    result = []

    # Check if a cell is a cavity
    def is_cavity(row, col):
        if 0 < row < n - 1 and 0 < col < n - 1:
            current_depth = int(grid[row][col])
            top = int(grid[row - 1][col])
            bottom = int(grid[row + 1][col])
            left = int(grid[row][col - 1])
            right = int(grid[row][col + 1])

            return current_depth > top and current_depth > bottom and current_depth > left and current_depth > right
        return False

    # Iterate through the interior cells
    for i in range(n):
        row_result = ''
        for j in range(n):
            if is_cavity(i, j):
                row_result += 'X'
            else:
                row_result += grid[i][j]
        result.append(row_result)

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
