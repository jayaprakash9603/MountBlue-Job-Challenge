#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def maxMin(k, arr):
    # Write your code here
    # Sort the array in ascending order
    arr.sort()
    
    # Initialize the minimum unfairness with a large value
    min_unfairness = float('inf')
    
    # Iterate through the array to find the minimum unfairness for each subarray
    for i in range(len(arr) - k + 1):
        unfairness = arr[i + k - 1] - arr[i]
        min_unfairness = min(min_unfairness, unfairness)
    
    return min_unfairness

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
