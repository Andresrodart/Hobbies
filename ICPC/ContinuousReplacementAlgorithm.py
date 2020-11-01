import bisect
class node:
	def __init__(self, value):
		self.value = value
		self.chields = []
	def add_child(self, child):
		bisect.insort_left(self.chields, child)


def dfs(u, nodes):
	visited = set()
	stack = [u]
	min_item = u.value
	while stack:
		u = stack.pop(0)
		if u not in visited:
			visited.add(u)
			if len(min_item) == len(u.value): min_item = min(min_item, u.value)
			else: min_item = min(min_item, u.value, key=len)
			for child in u.chields: stack.append(nodes[child])
	return min_item

N = int(input())
nodes = {}
res = []
while N:
	u, v = input().split()
	new_node = nodes.get(u, node(u))
	new_node.add_child(v)
	nodes[u] = new_node
	new_node = nodes.get(v, node(v))
	new_node.add_child(u)
	nodes[v] = new_node
	N -= 1
message = input()
for string in message.split():
	if string in nodes: 
		res.append(dfs(nodes[string], nodes))
	else: res.append(string)
print(' '.join(res))