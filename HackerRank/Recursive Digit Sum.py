#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n, k):
    res = 0
    n = str(n)
    if len(n) == 1:
        return n           
    for i in range(len(n)):
        res += int(n[i])
    if k != 0:
        res = res * k
    return superDigit(res, 0)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = str(nk[0])

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
