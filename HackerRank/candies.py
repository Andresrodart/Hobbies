import math
import os
import random
import re
import sys

# Complete the candies function below.
def checkCandies(arr, dp):
	if arr[0] <= arr[1]: dp[0] = min(max(dp[0], 1), 1)
	for i in range(1, len(arr)):
		if arr[i - 1] == arr[i]: dp[i] = max(dp[i - 1] - 1, 1, dp[i])
		elif arr[i - 1] > arr[i]: dp[i] = min(dp[i - 1], max(dp[i], 1))
		else: dp[i] = max(dp[i - 1] + 1, dp[i]) 
def candies(n, arr):
	print(arr)
	dp = [0] * n
	checkCandies(arr, dp)
	print(dp)
	arr.reverse()
	dp.reverse()
	checkCandies(arr, dp)
	dp.reverse()
	print(dp)
	res = 0
	for num in dp: res += num
	return res
if __name__ == '__main__':
	n = int(input())
	arr = []

	for _ in range(n):
		arr_item = int(input())
		arr.append(arr_item)

	result = candies(n, arr)
	print(result)