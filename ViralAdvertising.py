#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    # Write your code here
    shared = 5  # Initial number of people who receive the advertisement
    liked_cumulative = 0  # Cumulative number of people who liked the ad

    for day in range(1, n + 1):
        liked_today = shared // 2  # Number of people who liked the ad today
        liked_cumulative += liked_today
        shared = liked_today * 3  # Number of people who will receive the ad tomorrow

    return liked_cumulative

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
