#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'toys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY w as parameter.
#

def toys(w):
    # Sort the list of weights
    w.sort()

    containers = 0
    i = 0

    while i < len(w):
        # Increment the container count
        containers += 1

        # Determine the maximum weight allowed in the current container
        max_weight = w[i] + 4

        # Skip all items within the weight limit
        while i < len(w) and w[i] <= max_weight:
            i += 1

    return containers

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    w = list(map(int, input().rstrip().split()))

    result = toys(w)

    fptr.write(str(result) + '\n')

    fptr.close()
