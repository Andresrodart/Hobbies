def height(arry, i):
	if len(arry) == 0: return i
	return max(height(arry[:len(arry) // 2], i + 1), height(arry[len(arry) // 2 + 1:], i + 1))
def listOfDepths(graph):
	LL = [[] for _ in range(height(graph, 0))]
	LL[0] = [graph[0]]
	_listOfDepths(graph, LL, 0, 1)
	return LL
def _listOfDepths(graph, LL, parent, level):
	if level > len(LL) - 1: return 
	LL[level].append([graph[parent * 2 + 1]])
	LL[level].append([graph[parent * 2 + 2]])
	_listOfDepths(graph, LL, parent * 2 + 1, level + 1)
	_listOfDepths(graph, LL, parent * 2 + 2, level + 1)

LL = listOfDepths([7, 3, 11, 1, 5, 9, 13, 0, 2, 4, 6, 8, 10, 12, 14])
for list_ in LL: print(list_)
LL = listOfDepths([7, 3, 11, 1, 5, 9, 13])
for list_ in LL: print(list_)