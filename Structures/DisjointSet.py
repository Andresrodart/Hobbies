class DisjointSet:
	def __init__(self, size):
		self.parent = [i for i in range(size)] # Todos los nodos son sus propios padres
		self.size = [1 for _ in range(size)]	# Todos tienen tamaño uno
	def make_set(self, v):
		self.parent[v] = v
	def union_sets(self, a, b):
		a = self.find_set(a)
		b = self.find_set(b)
		if a != b:
			if self.size[a] < self.size[b]: a, b = b, a
			self.parent[b] = a
			self.size[a] += self.size[b]
	def find_set(self, v):
		if v == self.parent[v]: return v
		self.parent[v] = self.find_set(self.parent[v])
		return self.parent[v]