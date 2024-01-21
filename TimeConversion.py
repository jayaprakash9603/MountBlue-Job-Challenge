#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
from datetime import datetime
def timeConversion(s):
    # Write your code here
    # Parse input time string
    time_12hr = datetime.strptime(s, '%I:%M:%S%p')

    # Format the time in 24-hour clock
    time_24hr = time_12hr.strftime('%H:%M:%S')

    return time_24hr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
