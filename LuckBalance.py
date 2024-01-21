#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#

def luckBalance(k, contests):
    # Write your code here
    important_contests = []
    total_luck = 0

    for luck, importance in contests:
        if importance == 0:
            # Unimportant contest
            total_luck += luck
        else:
            # Important contest
            important_contests.append(luck)

    # Sort important contests in descending order
    important_contests.sort(reverse=True)

    # Add luck balance of the first k important contests
    total_luck += sum(important_contests[:k])

    # Subtract luck balance of the remaining important contests
    total_luck -= sum(important_contests[k:])

    return total_luck

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
