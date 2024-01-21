#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    # Find the maximum value in the array
    max_val = max(arr)

    # Initialize an array to store counts
    count_arr = [0] * (max_val + 1)

    # Count occurrences of each element
    for num in arr:
        count_arr[num] += 1

    # Reconstruct the sorted array based on counts
    sorted_arr = []
    for i in range(len(count_arr)):
        sorted_arr.extend([i] * count_arr[i])

    return sorted_arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
