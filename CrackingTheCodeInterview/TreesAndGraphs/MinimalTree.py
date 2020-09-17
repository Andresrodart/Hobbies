def minimalTree(arry):
	graph = [None] * (2 ** height(arry, 0) - 1)
	mid = arry[len(arry) // 2]
	graph[0] = mid
	_minimalTree(arry[:len(arry) // 2], graph, 0 * 2 + 1)
	_minimalTree(arry[len(arry) // 2 + 1:], graph, 0 * 2 + 2)
	return graph
def _minimalTree(arry, graph, i):
	if len(arry) == 0: return
	graph[i] = arry[len(arry) // 2]
	_minimalTree(arry[:len(arry) // 2], graph, i * 2 + 1)
	_minimalTree(arry[len(arry) // 2 + 1:], graph, i * 2 + 2)
def height(arry, i):
	if len(arry) == 0: return i
	return max(height(arry[:len(arry) // 2], i + 1), height(arry[len(arry) // 2 + 1:], i + 1))
print(minimalTree([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]))