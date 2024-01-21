#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    # Write your code here
    # Sort the array
    arr.sort()

    # Initialize the minimum absolute difference with a large value
    min_absolute_difference = float('inf')

    # Iterate through the sorted array and find the minimum absolute difference
    for i in range(1, len(arr)):
        absolute_difference = abs(arr[i] - arr[i - 1])
        min_absolute_difference = min(min_absolute_difference, absolute_difference)

    return min_absolute_difference

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
