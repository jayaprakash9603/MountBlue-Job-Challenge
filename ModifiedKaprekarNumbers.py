#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p, q):
    # Write your code here
    kaprekar_list = []

    for num in range(p, q + 1):
        square = num ** 2
        str_square = str(square)
        length = len(str_square)

        # Split the square into two parts
        right_part = str_square[length // 2:]
        left_part = str_square[:length // 2] or '0'

        # Convert the parts back to integers and check if they add up to the original number
        if int(left_part) + int(right_part) == num:
            kaprekar_list.append(num)

    if kaprekar_list:
        print(" ".join(map(str, kaprekar_list)))
    else:
        print("INVALID RANGE")

if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
