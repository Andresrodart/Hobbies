#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stockmax' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY prices as parameter.
#

def stockmax(prices):
    result = 'none'
    n = len(prices)
    for i, j in zip(range(n), range(n-1, -1, -1)):
        print(i, ' ', j)
    return result

    # Write your code here

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        prices = list(map(int, input().rstrip().split()))
        result = stockmax(prices)
        print(result)
        #fptr.write(str(result) + '\n')
        #fptr.close()
