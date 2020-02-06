#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the redJohn function below.
def redJohn(n):
    if n < 4:
        return 0
    elif n == 4:
        return 1
    else:
        a = (int(n / 4) + int(n % 4))
        return math.factorial(a)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = redJohn(n)

        fptr.write(str(result) + '\n')

    fptr.close()
