#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalizeArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equalizeArray(arr):
    # Write your code here
    # Count the frequency of each unique element
    element_count = {}
    for num in arr:
        if num in element_count:
            element_count[num] += 1
        else:
            element_count[num] = 1
    
    # Find the element with the maximum frequency
    max_freq = max(element_count.values())
    
    # Calculate the minimum number of deletions
    min_deletions = len(arr) - max_freq
    
    return min_deletions

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
