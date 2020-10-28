import heapq
import sys
# import time
from typing import List
# start_time = time.time()

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

def dijkstra(grid: List[List[int]], k: int, points: List[edge]) -> int:
	heap = []
	checked = set()
	for node in points[0]:
		node.distance = 0
		heapq.heappush(heap, node)
	while heap:
		actual = heapq.heappop(heap)
		i, j = actual.cord
		if grid[i][j] == k: return actual.distance
		if actual.cord not in checked:
			checked.add(actual.cord)
			for node in points[grid[i][j]]:
				nx, ny = node.cord
				node.distance = min(abs(i - nx) + abs(j - ny) +  actual.distance, node.distance)
				heapq.heappush(heap, node)
	return sys.maxsize

if __name__ == "__main__":	
	n, k = map(int, input().rstrip().split())
	points = [[] for _ in range(n ** 2) ]
	distance = [sys.maxsize for _ in range(n ** 2) ]
	grid = []
	res = sys.maxsize

	for _ in range(n):
		grid.append(list(map(int, input().rstrip().split())))
	for i in range(len(grid)):
		for j in range(len(grid)): # Por cada uno buscamos
			points[grid[i][j] - 1].append(edge(sys.maxsize, (i, j)))
	res = dijkstra(grid, k, points)
	print(-1 if res == sys.maxsize else res)
	# print("--- %s seconds ---" % (time.time() - start_time))
