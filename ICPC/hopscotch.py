import heapq
import sys

class edge:
	def __init__(self, distance, cord):
		self.distance = distance
		self.cord = cord
	def __lt__(self, other):
		return self.distance < other.distance
	def __str__(self):
		return str("{} : {}".format(self.distance, self.cord))
	def __repr__(self):
		return str("{} : {}".format(self.distance, self.cord))

def dijkstra(grid, k, points):
	heap = []
	for nx, ny in points[0]:
		heapq.heappush(heap, edge(0, (nx, ny)))
	actual = heapq.heappop(heap)
	i, j = actual.cord
	distance = 0
	while heap:
		if grid[i][j] == k: return distance
		for nx, ny in points[grid[i][j]]:
			distance = abs(i - nx) + abs(j - ny)
			heapq.heappush(heap, edge(distance, (nx, ny)))
		actual = heapq.heappop(heap)
		i, j = actual.cord
		print(actual)
	return sys.maxsize

if __name__ == "__main__":	
	n, k = map(int, input().rstrip().split())
	points = [[] for _ in range(n ** 2) ]
	grid = []
	res = sys.maxsize

	for _ in range(n):
		grid.append(list(map(int, input().rstrip().split())))
	for i in range(len(grid)):
		for j in range(len(grid)): # Por cada uno buscamos
			points[grid[i][j] - 1].append((i, j))
	res = dijkstra(grid, k, points)
	print(-1 if res == sys.maxsize else res)