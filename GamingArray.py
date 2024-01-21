#!/bin/python3

import sys


g = int(input().strip())
for a0 in range(g):
    n = int(input().strip())
    game = map(int, input().strip().split())
    if n==0:
        print("ANDY")
        continue
    elif n==1:
        print("BOB")
        continue
    maxes = []
    cur_max = -float("inf")
    for i, num in enumerate(game):
        if num > cur_max:
            cur_max = num
            maxes.append(i)
    if len(maxes) % 2 == 0:
        print("ANDY")
    else:
        print("BOB")