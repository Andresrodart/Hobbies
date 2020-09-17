import copy

def buildOrder(projects, dependencies):
	projects = set(projects) 	# all projects most have unique names, set will allow constant remove and look up
	heads = set(projects)		# this will be use to store only, no dependence projects
	visited = {}				# used for BFS
	graph = {}					# Graph in adjacency list representation
	res = []					# the result, the order to build projects
	for letter in projects:		# initialize the graph and visited O(P)
		graph[letter] = []
		visited[letter] = False
	for parent, child in dependencies: 			# create graph O(Edges)
		graph[parent].append(child)
		if child in heads: heads.remove(child)	# clean the node that are dependant
	for root in heads:
		error = BFS(root, graph, res, projects, visited)
		if error: return 'No posible'
	return ' '.join(res)
def BFS(root, graph, res, projects, visited):
	queue = [root]
	while queue:
		node = queue.pop(0)
		if not visited[node]:
			visited[node] = True
			res.append(node)
			for child in graph[node]:
				queue.append(child)
				if child not in projects: return -1
			projects.remove(node)
	return None

print(buildOrder(['a', 'b', 'c', 'd', 'e', 'f', 'g'], [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c'), ('e', 'g')]))
print(buildOrder(['a', 'b', 'c', 'd', 'e', 'f'], [('c', 'a'), ('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]))