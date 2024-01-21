#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    # Write your code here
    element_last_index = {}
    min_distance = float('inf')

    for i, num in enumerate(a):
        if num in element_last_index:
            distance = i - element_last_index[num]
            min_distance = min(min_distance, distance)
        element_last_index[num] = i

    return min_distance if min_distance != float('inf') else -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
