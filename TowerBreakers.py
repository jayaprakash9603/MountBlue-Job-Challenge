#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#
def solved(n,m):
    if m == 1 or n % 2 == 0:
        print(2)
    else:
        print(1)
if __name__ == "__main__":
    case = int(input())
    for _ in range(case):
        n,m = map(int,input().split())
        solved(n,m)