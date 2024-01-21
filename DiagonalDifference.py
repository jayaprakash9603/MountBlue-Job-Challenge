#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
     # Initialize variables to store the sums of the two diagonals
    primary_diagonal_sum = 0
    secondary_diagonal_sum = 0

    # Calculate the sums of the diagonals
    for i in range(len(arr)):
        primary_diagonal_sum += arr[i][i]
        secondary_diagonal_sum += arr[i][len(arr) - 1 - i]

    # Calculate the absolute difference between the sums
    absolute_difference = abs(primary_diagonal_sum - secondary_diagonal_sum)

    return absolute_difference

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
