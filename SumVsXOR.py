#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sumXor' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def sumXor(n):
    # Write your code here
    # Count the number of unset bits in n
    count_unset_bits = 0
    while n:
        if n % 2 == 0:
            count_unset_bits += 1
        n //= 2
    
    # Calculate the total number of values satisfying the condition
    result = 2 ** count_unset_bits
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = sumXor(n)

    fptr.write(str(result) + '\n')

    fptr.close()
