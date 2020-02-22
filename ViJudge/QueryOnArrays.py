import pandas as pd

class fenwick:
	def __init__(self, n):
		self.maxList = n + 1
		self.fenwick = [0] * (n + 1)
	def update(self, l, delta):
		while l < self.maxList:
			self.fenwick[l] += delta
			l = l | (l + 1)
	def add(self, r):
		res = 0
		while r >= 0:
			res += self.fenwick[r]
			r = (r & (r + 1)) - 1
		return res

def indexOfSort(arr, l, r, elem):
	i = int((r + l) / 2)
	if l == r:
		return r if arr[r] == elem else -1
	if arr[i] == elem:
		return i
	elif arr[i] > elem:
		return indexOfSort(arr, l, i - 1, elem)
	elif arr[i] < elem:
		return indexOfSort(arr, i + 1, r, elem)

def coordinateCompression(arr, n):
	aux = sorted(arr)
	aux = pd.unique(aux)
	for i in range(n):
		arr[i] = indexOfSort(aux, 0, n - 1, arr[i]) + 1
	return arr, len(aux)
if __name__ == "__main__":
	n = int(input())
	arr, rang = coordinateCompression(list(map(int, input().split())), n)
	q = int(input())
	while q > 0:
		query = list(map(int, input().split()))
		if(query[0] == 2):
			i, j = 0, n/2
		q -= 1

arr, j = coordinateCompression([1, 500, 423, 3242, 4254354, 3234], 6)
print(arr)