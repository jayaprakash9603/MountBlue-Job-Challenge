#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makingAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def makingAnagrams(s1, s2):
    # Write your code here
    # Initialize dictionaries to count the frequency of characters in each string
    count_s1 = {}
    count_s2 = {}

    # Count characters in the first string
    for char in s1:
        count_s1[char] = count_s1.get(char, 0) + 1

    # Count characters in the second string
    for char in s2:
        count_s2[char] = count_s2.get(char, 0) + 1

    # Calculate the minimum number of deletions needed
    deletions = 0
    for char in set(count_s1.keys()).union(set(count_s2.keys())):
        deletions += abs(count_s1.get(char, 0) - count_s2.get(char, 0))

    return deletions

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
