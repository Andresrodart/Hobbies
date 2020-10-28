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
	checked = {}
	for nx, ny in points[0]:
		heapq.heappush(heap, edge(0, (nx, ny)))
	while heap:
		actual = heapq.heappop(heap)
		i, j = actual.cord
		if grid[i][j] == k: return actual.distance
		for nx, ny in points[grid[i][j]]:
			if (nx, ny) not in checked: 
				distance = abs(i - nx) + abs(j - ny) + actual.distance
				checked[(nx, ny)] = edge(distance, (nx, ny))
			else: 
				distance = min(abs(i - nx) + abs(j - ny) +  actual.distance, checked[(nx, ny)].distance)
				checked[(nx, ny)].distance = distance
			heapq.heappush(heap, checked[(nx, ny)])
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