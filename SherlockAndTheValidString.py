#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
def isValid(s):
    temp = [s.count(x) for x in set(s)]
    temp2 = list(set(temp))
    
    if len(temp2) == 1:
        return 'YES'
    if len(temp2) > 2:
        return 'NO'
        
    temp = [temp.count(x) for x in temp2]
    
    if temp[0] == temp[1]:
        return 'NO'
    
    if temp [0] < temp[1]:
        return 'YES' if temp[0] == 1 and (temp2[0] == 1 or temp2[0] == (temp2[1]+1) or temp2[0] == (temp2[1]-1)) else 'NO'
    
    return 'YES' if temp[1] == 1 and (temp2[1] == 1 or temp2[1] == (temp2[0]+1) or temp2[1] == (temp2[0]-1)) else 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
