#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

def acmTeam(topic):
    # Write your code here
    n = len(topic)
    m = len(topic[0])

    max_topics_known = 0
    team_count = 0

    for i in range(n):
        for j in range(i + 1, n):
            topics_i = int(topic[i], 2)
            topics_j = int(topic[j], 2)

            topics_known = bin(topics_i | topics_j).count('1')

            if topics_known > max_topics_known:
                max_topics_known = topics_known
                team_count = 1
            elif topics_known == max_topics_known:
                team_count += 1

    return [max_topics_known, team_count]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
