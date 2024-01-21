#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    bird_count = {}

    # Count the occurrences of each bird type
    for bird in arr:
        bird_count[bird] = bird_count.get(bird, 0) + 1

    # Find the bird type with the maximum count
    max_count = max(bird_count.values())
    most_frequent_birds = [bird for bird, count in bird_count.items() if count == max_count]

    # Return the smallest id among the most frequently sighted birds
    return min(most_frequent_birds)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
