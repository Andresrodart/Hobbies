from collections import deque
T = int(input())
for case in range(1, T + 1):
	N, K = map(int, input().split())
	if K % N == 0: 
		row = deque([i for i in range(1, N + 1)])
		while row[0] != int(K / N):
			row.rotate(1)
		print('Case #{}: {}'.format(case, 'POSSIBLE'))
		for i in range(N):
			print(*row)
			row.rotate(1)
	else:
		if K == N + 1: print('Case #{}: {}'.format(case, 'IMPOSSIBLE'))
		else:
			rows = [set() for i in range(N)]
			cols = [set() for i in range(N)]
			exceeded = K - int(K/N) * N
			matrix = [[0]*N for i in range(N)]
			matrix[0][0], matrix[1][1] = int(K/N) + int(exceeded/2), int(K/N) + int((exceeded + 1)/2)
			matrix[0][1], matrix[1][0] = int(K/N), int(K/N)
			
			if matrix[0][0] == int(K/N) or matrix[1][1] == int(K/N):
				matrix[0][0] -= 1
				matrix[1][1] += 1
			

			for i in range(2, N): 
				matrix[i][i] = int(K/N)
				if i % 2 == 0 and i < N - 1: 
					matrix[i][i + 1] = matrix[1][1]
					matrix[i + 1][i] = matrix[0][0]
			
			for i in range(N):
				if matrix[i][i] > N:
					dif = matrix[i][i] - N
					matrix[i][i] -= dif
					matrix[int(N/2) + i][int(N/2) + i] += dif
			
			for i in range(N):
				for j in range(N):
					if matrix[i][j] != 0:
						rows[i].add(matrix[i][j])
						cols[j].add(matrix[i][j])

			for i in range(N):
				for j in range(i, N):
					if matrix[i][j] == 0:
						for k in range(1, N + 1):
							if k not in rows[i] and k not in cols[j]: 
								matrix[i][j] = k
								rows[i].add(matrix[i][j])
								cols[j].add(matrix[i][j])
								break
			for i in range(N):
				for j in range(0, i):
					if matrix[i][j] == 0:
						for k in range(1, N + 1):
							if k not in rows[i] and k not in cols[j]: 
								matrix[i][j] = k
								rows[i].add(matrix[i][j])
								cols[j].add(matrix[i][j])
								break
			isSolution = True
			for row in matrix:
				if isSolution:
					for num in row:
						if num <= 0 or num > N:
							isSolution = False
							break
				else: break
			if isSolution:
				print('Case #{}: {}'.format(case, 'POSSIBLE'))
				for i in range(N):
					print(*matrix[i])
			else: print('Case #{}: {}'.format(case, 'IMPOSSIBLE'))