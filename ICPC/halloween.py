def maxCandies(i, j, candies, dp):
	if i >= len(candies) or j >= len(candies): return 0
	elif (i, j) in dp: return dp[(i, j)]
	else:
		dp[(i, j)] = max(maxCandies(i + 1, j + 1, candies, dp), candies[j] + maxCandies(j, j + 2, candies, dp))
		return dp[(i, j)]
T = int(input())
while T:
	N =int(input())
	candies = list(map(int, input().rstrip().split()))
	print(maxCandies(0, 0, candies, {}))
	T -= 1