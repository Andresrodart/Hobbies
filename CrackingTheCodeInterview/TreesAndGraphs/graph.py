class Graph:
	def __init__(self, length):
		self.adjacencyList = [[] for _ in range(length)]
		self.length = length
	def addEdge(self, source, destination, undirected = False):
		self.adjacencyList[source].append(destination)
		if undirected: self.adjacencyList[destination].append(source) 
	def findPath(self, source, destination):
		queue = [(source, [source])]
		visited = [False] * self.length
		while queue:
			node, path = queue.pop(0)
			if not visited[node]:
				visited[node] = True
				if node == destination: return path
				for child in self.adjacencyList[node]: queue.append((child, path + [child]))
		return None

graph = Graph(6)
graph.addEdge(0, 3, undirected=True)
graph.addEdge(4, 1, undirected=True)
graph.addEdge(4, 0, undirected=True)
graph.addEdge(3, 1, undirected=True)
graph.addEdge(3, 2, undirected=True)
print(graph.findPath(0, 2))
print(graph.findPath(4, 1))
print(graph.findPath(4, 5))