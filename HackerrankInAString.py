#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hackerrankInString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def hackerrankInString(s):
    # Write your code here
    # Define the pattern to match
    pattern = "hackerrank"
    
    # Initialize variables to keep track of matching characters
    match_index = 0
    for char in s:
        # Check if the current character matches the expected character in the pattern
        if char == pattern[match_index]:
            # Move to the next expected character in the pattern
            match_index += 1
            # If all characters in the pattern are matched, return "YES"
            if match_index == len(pattern):
                return "YES"
    
    # If the loop completes without returning, it means the pattern is not found
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
