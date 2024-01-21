#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    n = len(c)
    energy = 100  # Initial energy level
    current_cloud = 0  # Start from the first cloud

    while True:
        current_cloud = (current_cloud + k) % n  # Calculate the next cloud after jumping
        energy -= 1  # Decrease energy for each jump

        if c[current_cloud] == 1:
            energy -= 2  # Additional energy cost for landing on a thunderhead cloud

        if current_cloud == 0:
            break  # Exit the loop when back to the starting cloud

    return energy

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
