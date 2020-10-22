
def whenConnected(matrix, i, j):
	stack = [(i, j, 0, [(i, j)])]
	visited = set()
	while stack:
		# print(stack[-1])
		i, j, steps, path = stack.pop(0)
		if (i, j) not in visited:
			visited.add((i, j))
			node = matrix[i][j]
			if i > 0 and matrix[i - 1][j] != node: 
				stack.append((i - 1, j, steps + 1, path + [(i - 1, j)]))
			if j > 0 and matrix[i][j - 1] != node:
				stack.append((i, j - 1, steps + 1, path + [(i , j - 1)]))
			if i + 1 < len(matrix) and matrix[i + 1][j] != node:
				stack.append((i + 1, j, steps + 1, path + [(i + 1 , j)]))
			if j + 1 < len(matrix[i]) and matrix[i][j + 1] != node:
				stack.append((i, j + 1, steps + 1, path + [(i , j + 1)]))
			if (i > 0 and matrix[i - 1][j] == node) or (j > 0 and matrix[i][j - 1] == node) or (i + 1 < len(matrix) and matrix[i + 1][j] == node) or (j + 1 < len(matrix[i]) and matrix[i][j + 1] == node):
				return steps, path
	return -1, []

def set_memo(path, when, memo):
	for location in path:
		memo[location] = when
		when -= 1

def bfs(matrix, res, visited):
	queue = []
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			node = matrix[i][j]
			if (i > 0 and matrix[i - 1][j] == node) or (j > 0 and matrix[i][j - 1] == node) or (i + 1 < len(matrix) and matrix[i + 1][j] == node) or (j + 1 < len(matrix[i]) and matrix[i][j + 1] == node):
				res[i][j] = 0
				queue.append((i, j))
				visited[i][j] = True
	while queue:
		i, j = queue.pop(0)
		up = down = left = right = 1005
		if i > 0:
			if not visited[i - 1][j]: queue.append((i - 1, j))
			up = res[i - 1][j]
		if j > 0:
			if not visited[i][j - 1]: queue.append((i, j - 1))
			left = res[i][j - 1]
		if i + 1 < len(matrix):
			if not visited[i + 1][j]: queue.append((i + 1, j))
			down = res[i + 1][j]
		if j + 1 < len(matrix[i]):
			if not visited[i][j + 1]: queue.append((i, j + 1))
			right = res[i][j + 1]
		if not visited[i][j]:
			res[i][j] = min(up, down, left, right) + 1
			visited[i][j] = True
n, m, t = map(int, input().rstrip().split(' '))
matrix = []
res = [[1005] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]
when = 0
memo = {}
for i in range(n):
	matrix.append(input())
while t > 0:
	i, j, p =  map(int, input().split(' '))
	bfs(matrix, res, visited)
	# print(*res, sep='\n')
	if res[i - 1][j - 1] >= 1005: print(matrix[i - 1][j - 1])
	else:
		when = res[i - 1][j - 1]
	# 	if (i - 1, j - 1) in memo: when = memo[(i - 1, j - 1)]
	# 	else:
	# 		when, path = whenConnected(matrix, i - 1, j - 1)
	# 		set_memo(path, when, memo)
		if when == -1 or (p + when) % 2 == 0 or when > p: print(matrix[i - 1][j - 1])
		else: print('0' if matrix[i - 1][j - 1] == '1' else '1')
	t -= 1