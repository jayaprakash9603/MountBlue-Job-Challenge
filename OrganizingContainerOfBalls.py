#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#

def organizingContainers(container):
    # Write your code here
    # Calculate the sum of balls for each container and each type
    container_sums = [sum(row) for row in container]
    ball_type_sums = [sum(col) for col in zip(*container)]

    # Sort both sums arrays
    container_sums.sort()
    ball_type_sums.sort()

    # Check if the sums arrays are equal
    if container_sums == ball_type_sums:
        return "Possible"
    else:
        return "Impossible"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
