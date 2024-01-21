#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'squares' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#
import math
def squares(a, b):
    # Count the number of perfect squares in the range [a, b]
    count = 0
    current_square = math.isqrt(a)
    
    # If a is a perfect square within the range, increment count
    if current_square**2 == a:
        count += 1
    
    # Continue checking for perfect squares in the remaining range
    current_square += 1
    while current_square**2 <= b:
        count += 1
        current_square += 1

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
