#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
import math

def encryption(s):
    # Write your code here
    strippedString = ''.join(s.split(' '))
    length = len(strippedString)
    x = math.sqrt(length)
    columns = math.ceil(x)
    
    # no use of rows in this solution
    # rows = math.floor(x)
    # if rows*columns<len(strippedString):
    #     rows = columns
    
    resultString = ''
    for i in range(0,columns):
        for j in range(i,length,columns):
            resultString += strippedString[j]
        resultString += '\t'
    
    return resultString

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()

