#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Write your code here
    # Function to calculate the sum of digits of a number
    def calculate_sum(num):
        return sum(map(int, str(num)))

    # Calculate the initial super digit
    initial_super_digit = calculate_sum(n) * k

    # Function to calculate the super digit of a number
    def calculate_super_digit(super_digit):
        while super_digit >= 10:
            super_digit = calculate_sum(super_digit)
        return super_digit

    # Calculate the final super digit
    result = calculate_super_digit(initial_super_digit)

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
