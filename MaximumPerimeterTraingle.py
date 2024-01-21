#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#

def maximumPerimeterTriangle(sticks):
    # Write your code here
    # Sort the sticks in non-decreasing order
    sticks.sort(reverse=True)

    # Iterate through the sorted sticks to find the maximum perimeter triangle
    for i in range(len(sticks) - 2):
        if sticks[i] < sticks[i + 1] + sticks[i + 2]:
            # Found a non-degenerate triangle
            return [sticks[i + 2], sticks[i + 1], sticks[i]]

    # No non-degenerate triangle found
    return [-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
