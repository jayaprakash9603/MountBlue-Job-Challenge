#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    ranked_scores = sorted(set(ranked), reverse=True)  # Remove duplicates and sort in descending order
    player_ranks = []

    i = len(ranked_scores) - 1  # Start from the bottom of the leaderboard
    for player_score in player:
        while i >= 0 and player_score >= ranked_scores[i]:
            i -= 1  # Move up the leaderboard if the player's score is greater than or equal to the current score
        player_ranks.append(i + 2)  # Add 2 because the index is 0-based, and the ranks start from 1

    return player_ranks

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
