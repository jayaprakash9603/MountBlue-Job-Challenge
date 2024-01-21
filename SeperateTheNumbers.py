#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    # Write your code here
    n = len(s)

    for i in range(1, n//2 + 1):
        first_num = int(s[:i])
        current_num = first_num
        result = str(current_num)

        while len(result) < n:
            current_num += 1
            result += str(current_num)

        if result == s:
            print(f"YES {first_num}")
            return

    print("NO")

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
