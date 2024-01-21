#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sansaXor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def sansaXor(arr):
    # Write your code here
    n = len(arr)
    result = 0

    # If the number of elements is even, XOR of all subarrays cancels out.
    if n % 2 == 0:
        return 0

    # If the number of elements is odd, XOR of elements at odd indices.
    for i in range(0, n, 2):
        result ^= arr[i]

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = sansaXor(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
