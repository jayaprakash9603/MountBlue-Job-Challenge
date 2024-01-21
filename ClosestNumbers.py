#!/bin/python3

import math
import os
import random
import re
import sys

def closestNumbers(arr):
    # Step 1: Sort the array in ascending order
    arr.sort()

    # Initialize variables
    min_diff = float('inf')
    result_pairs = []

    # Step 2: Iterate through the sorted array
    for i in range(len(arr) - 1):
        # Calculate absolute difference between adjacent elements
        diff = abs(arr[i] - arr[i+1])

        # Update minimum difference and reset pairs list if a smaller difference is found
        if diff < min_diff:
            min_diff = diff
            result_pairs = [arr[i], arr[i+1]]
        elif diff == min_diff:
            # If the difference is equal to the minimum, add the pair to the result
            result_pairs.extend([arr[i], arr[i+1]])

    # Step 3: Return the pairs with the minimum absolute difference
    return result_pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
