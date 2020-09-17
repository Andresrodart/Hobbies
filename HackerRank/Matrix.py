import sys
class DisjointSet:
	def __init__(self, size):
		self.parent = [i for i in range(size)]
		self.rank = [0 for _ in range(size)]
	def make_rank(self, v):
		self.rank[v] = 1
	def union_sets(self, a, b):
		a = self.find_set(a)
		b = self.find_set(b)
		if a != b:
			if self.rank[a] < self.rank[b]: a, b = b, a
			self.parent[b] = a
			self.rank[a] += self.rank[b]
	def find_set(self, v):
		if v == self.parent[v]: return v
		self.parent[v] = self.find_set(self.parent[v])
		return self.parent[v]
def minTime(roads, machines):
	DS = DisjointSet(10**5)
	res = 0
	roads.sort(key = lambda road: road[2], reverse = True)
	for machine in machines: DS.make_rank(machine)
	for a, b, cost in roads:
		if DS.rank[DS.find_set(a)] == 1 and DS.rank[DS.find_set(b)] == 1: res += cost
		else: DS.union_sets(a, b)
	return res
	
# # Complete the minTime function below.
# def graphify(edges):
# 	graph = {}
# 	for edge in edges:
# 		if edge[0] not in graph:
# 			graph[edge[0]] = {}
# 		if edge[1] not in graph:
# 			graph[edge[1]] = {}
# 		graph[edge[0]][edge[1]] = edge[2]
# 		graph[edge[1]][edge[0]] = edge[2]
# 	return graph

# def makePairs(array):
# 	if not array or len(array) <= 1: return None
# 	res = []
# 	for i in range(len(array)):
# 		for j in range(i + 1, len(array)):
# 			res.append((array[i], array[j]))
# 	return res
# def findPath(source, destination, graph):
# 	queue = [(source, [source])]
# 	visited = set()
# 	while queue:
# 		node, path = queue.pop(0)
# 		if node not in visited:
# 			visited.add(node)
# 			if node == destination:
# 				return path
# 			for child in graph[node]:
# 				queue.append((child, path[:] + [child]))
# 	return None
# def minTime(roads, machines):
# 	graph = graphify(roads)
# 	pairs = makePairs(machines)
# 	res = 0
# 	print(machines, pairs)
# 	while pairs:
# 		minRoad = sys.maxsize
# 		pairOfCities = pairs.pop()
# 		print(graph)
# 		path = findPath(*pairOfCities, graph)
# 		print(*pairOfCities, path)
# 		roadsInPath = makePairs(path)
# 		auxA = auxB = None
# 		while roadsInPath:
# 			cityA, cityB = roadsInPath.pop()
# 			if cityA in graph and cityB in graph[cityA] and graph[cityA][cityB] < minRoad:
# 				minRoad = graph[cityA][cityB]
# 				auxA, auxB = cityA, cityB
# 		if minRoad != sys.maxsize: 
# 			res += minRoad
# 			graph[auxA].pop(auxB)
# 			graph[auxB].pop(auxA)
# 	return res

if __name__ == '__main__':
	nk = input().split()
	n = int(nk[0])
	k = int(nk[1])
	roads = []
	for _ in range(n - 1):
		roads.append(list(map(int, input().rstrip().split())))
	machines = []
	for _ in range(k):
		machines_item = int(input())
		machines.append(machines_item)
	result = minTime(roads, machines)
	print(result)