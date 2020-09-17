import math
import os
import random
import re
import sys

# Complete the roadsAndLibraries function below.
def roadsAndLibraries(n, c_lib, c_road, cities):
	if c_lib < c_road: return n * c_lib
	cities = graphForm(cities, n)
	res = 0
	visited = [False] * n
	for i in range(n):
		if visited[i]: continue 
		count = DFS(cities, visited, i)
		if count > 0: res +=  (count - 1) * c_road + c_lib
	return res

def DFS(matrix, visited, root):
	stack = [root]
	visited_ = 0
	while stack:
		root = stack.pop()
		if not visited[root]:  
			visited[root] = True
			visited_ += 1
			for road in matrix[root]: stack.append(road)
	return visited_

def graphForm(cities, n):
	graph = [[] for _ in range(n)]
	for road in cities:
		graph[road[0] - 1].append(road[1] - 1)
		graph[road[1] - 1].append(road[0] - 1)
	return graph
	
if __name__ == '__main__':
	q = int(input())
	for q_itr in range(q):
		nmC_libC_road = input().split()
		n = int(nmC_libC_road[0])
		m = int(nmC_libC_road[1])
		c_lib = int(nmC_libC_road[2])
		c_road = int(nmC_libC_road[3])
		cities = []
		for _ in range(m):	cities.append(list(map(int, input().rstrip().split())))
		result = roadsAndLibraries(n, c_lib, c_road, cities)
		print(result)