#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    # Convert the string to lowercase
    s_lower = s.lower()

    # Create a set to store the unique lowercase letters in the string
    unique_letters = set()

    # Iterate through the string to populate the set
    for char in s_lower:
        if char.isalpha():
            unique_letters.add(char)

    # Check if the set contains all lowercase letters of the alphabet
    if len(unique_letters) == 26:
        return "pangram"
    else:
        return "not pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
