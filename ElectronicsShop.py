#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    # Initialize the maximum amount spent to -1
    max_spent = -1

    # Iterate through each combination of keyboard and USB drive prices
    for keyboard_price in keyboards:
        for drive_price in drives:
            # Calculate the total cost for the current combination
            total_cost = keyboard_price + drive_price

            # Check if the total cost is within the budget and greater than the current maximum spent
            if total_cost <= b and total_cost > max_spent:
                max_spent = total_cost

    return max_spent

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
