#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jimOrders' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY orders as parameter.
#

def jimOrders(orders):
    # Write your code here
    # Create a list of tuples containing order number, prep time, and serve time
    serve_times = [(i + 1, orders[i][0], orders[i][1] + orders[i][0]) for i in range(len(orders))]
    
    # Sort the list of tuples by serve time
    serve_times.sort(key=lambda x: x[2])
    
    # Extract customer numbers in the sorted order
    result = [customer[0] for customer in serve_times]
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
