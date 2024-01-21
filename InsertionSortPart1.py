#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    # Store the value of the last element
    key = arr[-1]
    
    # Initialize an index for comparisons
    i = n - 2
    
    # Compare key with each element to the left until a smaller element is found
    while i >= 0 and arr[i] > key:
        # Shift the larger element to the right
        arr[i + 1] = arr[i]
        # Print the interim array
        print(*arr)
        # Move to the next index to the left
        i -= 1
    
    # Insert the stored value at the correct position
    arr[i + 1] = key
    
    # Print the final array
    print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
