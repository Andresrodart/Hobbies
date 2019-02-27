#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    sum = -1000;
    for i in range(0, 4):
        for x in range(0,4):
                top = arr[i][x]+arr[i][x+1]+arr[i][x+2];
                middle = arr[i+1][x+1];
                bottom = arr[i+2][x]+arr[i+2][x+1]+arr[i+2][x+2];
                if top+middle+bottom > sum:
                    sum=top+middle+bottom;
    return sum;

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
