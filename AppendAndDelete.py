#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    # Write your code here
    common_prefix_length = 0

    # Find the length of the common prefix
    for i in range(min(len(s), len(t))):
        if s[i] == t[i]:
            common_prefix_length += 1
        else:
            break

    total_operations = len(s) + len(t) - 2 * common_prefix_length

    if total_operations <= k and (k - total_operations) % 2 == 0 or k >= len(s) + len(t):
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
