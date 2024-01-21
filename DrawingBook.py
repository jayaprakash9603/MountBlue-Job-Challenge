#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here
    # Calculate the number of pages to turn from the beginning
    pages_from_start = p // 2

    # Calculate the number of pages to turn from the end
    pages_from_end = (n // 2) - (p // 2)

    # Return the minimum of the two values
    return min(pages_from_start, pages_from_end)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
