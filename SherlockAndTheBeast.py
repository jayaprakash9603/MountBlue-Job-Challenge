#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'decentNumber' function below.
#
# The function accepts INTEGER n as parameter.
#

def decentNumber(n):
    # Find the maximum number of 5's that can be added to the number
    max_fives = n // 3 * 3

    # Check if the remaining digits can be filled with 3's
    remaining_digits = n - max_fives

    # Adjust the number of 5's and 3's to meet the properties of a Decent Number
    while remaining_digits % 5 != 0 and max_fives >= 0:
        max_fives -= 3
        remaining_digits = n - max_fives

    if max_fives >= 0 and remaining_digits % 5 == 0:
        decent_num = '5' * max_fives + '3' * remaining_digits
        print(decent_num)
    else:
        print(-1)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        decentNumber(n)
