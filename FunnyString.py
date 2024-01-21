#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):
    # Write your code here
    # Get the reverse of the string
    reversed_s = s[::-1]

    # Calculate the absolute differences for the original and reversed strings
    diff_s = [abs(ord(s[i]) - ord(s[i + 1])) for i in range(len(s) - 1)]
    diff_reversed_s = [abs(ord(reversed_s[i]) - ord(reversed_s[i + 1])) for i in range(len(reversed_s) - 1)]

    # Check if the differences are the same for both strings
    if diff_s == diff_reversed_s:
        return "Funny"
    else:
        return "Not Funny"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
