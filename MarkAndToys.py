#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumToys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY prices
#  2. INTEGER k
#

def maximumToys(prices, k):
    # Write your code here
    # Sort the toy prices in ascending order
    prices.sort()

    # Initialize variables
    num_toys = 0
    remaining_budget = k

    # Iterate through the sorted toy prices
    for price in prices:
        # If the current toy is within the budget, buy it
        if price <= remaining_budget:
            num_toys += 1
            remaining_budget -= price
        else:
            # If the budget is exhausted, break the loop
            break

    return num_toys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
