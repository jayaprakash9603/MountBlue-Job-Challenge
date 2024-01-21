#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def get_factors_of_lcm(arr):
    result = arr[0]
    for i in range(1, len(arr)):
        result = lcm(result, arr[i])
    return result

def get_multiples_of_gcd(arr):
    result = arr[0]
    for i in range(1, len(arr)):
        result = gcd(result, arr[i])
    return result

def getTotalX(a, b):
    factors_of_lcm = get_factors_of_lcm(a)
    multiples_of_gcd = get_multiples_of_gcd(b)
    
    count = 0
    x = factors_of_lcm
    while x <= multiples_of_gcd:
        if multiples_of_gcd % x == 0:
            count += 1
        x += factors_of_lcm
    
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
