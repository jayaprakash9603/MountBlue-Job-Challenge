#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    # Write your code here
    # Calculate the total cost of the bill
    total_cost = sum(bill)

    # Deduct the cost of the item Anna didn't eat
    anna_share = (total_cost - bill[k]) // 2

    # Check if Brian charged Anna correctly
    if anna_share == b:
        print("Bon Appetit")
    else:
        # Print the difference Brian owes to Anna
        print(b - anna_share)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
