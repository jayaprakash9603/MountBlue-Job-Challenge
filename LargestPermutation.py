#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestPermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def largestPermutation(k, arr):
    n = len(arr)
    index_dict = {val: i for i, val in enumerate(arr)}
    
    for i in range(n):
        # If we have performed enough swaps, break out of the loop
        if k == 0:
            break
        
        current_value = arr[i]
        largest_value = n - i
        
        # If the current element is not the largest possible, swap it
        if current_value < largest_value:
            # Update the index_dict with the new positions
            index_dict[current_value] = index_dict[largest_value]
            index_dict[largest_value] = i
            
            # Swap the elements in the array
            arr[i], arr[index_dict[current_value]] = arr[index_dict[current_value]], arr[i]
            
            # Decrease the number of available swaps
            k -= 1
    
    return arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = largestPermutation(k, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
