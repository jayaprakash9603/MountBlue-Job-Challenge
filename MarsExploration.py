#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    # Write your code here
    # Initialize a counter for altered characters
    altered_count = 0

    # Iterate through the received signal in blocks of three characters
    for i in range(0, len(s), 3):
        # Check each character in the current block
        for j in range(3):
            # The expected character in the SOS message
            expected_char = "SOS"[j]

            # Check if the current character is different from the expected character
            if s[i + j] != expected_char:
                altered_count += 1

    return altered_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
