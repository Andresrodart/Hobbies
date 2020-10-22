
import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
	memo = {0: arr[0], 1: arr[1]}
	for i, num in enumerate(arr[2:], start=2):
		memo[i] = max(memo[i - 1], memo[i - 2] + num, memo[i - 2], num)
	return memo[len(arr) - 1]
if __name__ == '__main__':

	n = int(input())

	arr = list(map(int, input().rstrip().split()))

	res = maxSubsetSum(arr)

	print(res)