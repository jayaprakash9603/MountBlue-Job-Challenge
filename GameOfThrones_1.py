#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gameOfThrones' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def gameOfThrones(s):
    # Write your code here
    char_count = {}

    # Count the frequency of each character in the string
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Count the number of characters with odd frequency
    odd_count = 0
    for count in char_count.values():
        if count % 2 != 0:
            odd_count += 1

    # If there is at most one character with an odd frequency, it's possible to rearrange into a palindrome
    if odd_count <= 1:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
