import sys
if __name__ == "__main__":
	N, K, T = map(int, input().split(' '))
	distances = list(map(int, input().split(' ')))
	# distances.sort()
	maxSum = start = stop = -1
	auxSum = auxStart = auxStop = 0	
	for x in range(1, N):
		DiffDistance = distances[x] - distances[x - 1]
		if auxSum + DiffDistance <= K:
			auxSum += DiffDistance
			auxStop = x
		else: 
			if maxSum < auxSum and auxSum <= K:
				maxSum = auxSum
				start = auxStart
				stop = auxStop
			auxStop = x
			auxStart = x
			auxSum = DiffDistance
	if maxSum == -1 or maxSum < T: 	print(-1)
	else:
		c = T
		for j in range(1, N):
			i = j - 1
			if i >= start and j <= stop: continue
			c += distances[j] - distances[i]
		print(start, stop, c)