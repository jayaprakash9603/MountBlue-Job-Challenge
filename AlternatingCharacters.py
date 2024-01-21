#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternatingCharacters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternatingCharacters(s):
    # Write your code here
    # Initialize a variable to count the number of deletions
    deletions = 0

    # Iterate through the string to count consecutive matching characters
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            # Increment the deletion count for consecutive matching characters
            deletions += 1

    return deletions

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
