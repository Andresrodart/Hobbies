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
	n = len(prices)
	maxProfit = 0
	sellPrice = prices[n - 1]
	
	if n == 1:
		return 0

	for i in range(n - 2, -1, -1):
		if sellPrice > prices[i]:
			maxProfit = maxProfit + (sellPrice - prices[i])
		else :
			sellPrice = prices[i]

	return maxProfit

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
