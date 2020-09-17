# Asumo que no se conoce el número de nodos
# Uso un arreglo de vistos para no repetir
# Si uso DFS en un nodo árbol recursivo podría no salir nunca 
# BFS me asegura encontrar el camino mas corto entre los nodos, por lo que si existe el camino lo encontrara antes
def RoutesBetweenNodes(graph, _from, _to):
	queue, visited = [_from], set()
	while queue:
		actual = queue.pop(0)
		if actual == _to: return True
		elif actual not in visited:
			visited.add(actual)
			for node in graph[actual]: queue.append(node)
	return False

graph = [
[1],
[2, 3],
[4],
[],
[],
[6],
[]
]
print(RoutesBetweenNodes(graph, 0, 4))
print(RoutesBetweenNodes(graph, 0, 5))