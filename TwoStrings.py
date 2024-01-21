#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoStrings' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def twoStrings(s1, s2):
    # Write your code here
    # Create sets of characters for each string
    set_s1 = set(s1)
    set_s2 = set(s2)

    # Check if there is any common character
    common_characters = set_s1.intersection(set_s2)

    # Return "YES" if there are common characters, otherwise "NO"
    return "YES" if common_characters else "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
