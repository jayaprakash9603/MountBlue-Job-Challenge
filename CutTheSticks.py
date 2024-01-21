#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    # Write your code here
    result = []
    
    while arr:
        # Append the number of sticks before each cut
        result.append(len(arr))
        
        # Find the minimum length of sticks
        min_length = min(arr)
        
        # Cut the sticks and discard the pieces of the minimum length
        arr = [x - min_length for x in arr if x > min_length]
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
