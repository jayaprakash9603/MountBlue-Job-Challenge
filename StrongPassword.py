#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    # Define character sets
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    # Initialize flags for each character type
    has_number = False
    has_lower = False
    has_upper = False
    has_special = False

    # Check the password for each character type
    for char in password:
        if char in numbers:
            has_number = True
        elif char in lower_case:
            has_lower = True
        elif char in upper_case:
            has_upper = True
        elif char in special_characters:
            has_special = True

    # Calculate the number of missing criteria
    missing_criteria = 0
    if not has_number:
        missing_criteria += 1
    if not has_lower:
        missing_criteria += 1
    if not has_upper:
        missing_criteria += 1
    if not has_special:
        missing_criteria += 1

    # Determine the minimum number of characters to add
    return max(missing_criteria, 6 - n)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
