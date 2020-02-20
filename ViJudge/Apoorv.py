class fenwick:
	def __init__(self, n):
		self.maxList = n
		self.fenwick = [0] * n
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

def cordRed(arr, n):
	mapper = {}
	aux = sorted(arr)
	for i in range(n):
		if aux[i] not in mapper:
			mapper[aux[i]] = i
	for i in range(n):
		arr[i] = mapper[arr[i]]
	return arr

if __name__ == "__main__":
	n, p = map(int, input().split())
	arr = cordRed(list(map(int, input().split())), n)
	fenwickNum = fenwick(p)
	fenwickPos = fenwick(n)
	resI = 0
	resMax = 0
	j = 0
	k = 0
	for i in range(n - 1, n - p - 1, -1):
		fenwickNum.update(arr[i], 1)
		resMax += fenwickNum.add(arr[i] - 1)
		fenwickPos.update(i, resMax)
	for i in range(n - p - 1, -1, -1):
		fnwick.update(arr[n - 1 - j], - 1)
		auxRes = 0
		for ii in range(p):
			auxRes += fnwick.add(arr[i + ii] - 1)
		
	print(resI + 1, resMax)

# if __name__ == "__main__":
# 	n, p = map(int, input().split())
# 	arr = list(map(int, input().split()))
# 	resI = 0
# 	resMax = 0
# 	if(p > 1):
# 		arrAux = [0] * (p + 1)
# 		for i in range(p):
# 			for j in range(i + 1, p):
# 				arrAux[i] += 1 if arr[i] > arr[j] else 0
# 			resMax += arrAux[i]
# 		if p < n:
# 			for i in range(1, n - p + 1):
# 				auxRes = 0
# 				for j in range(p):
# 					arrAux[j] = arrAux[j + 1] + (1 if arr[i + j] > arr[i + p - 1] else 0)
# 					auxRes += arrAux[j]
# 				if auxRes > resMax:
# 					resMax = auxRes
# 					resI = i 
# 	print(resI + 1, resMax)


# if __name__ == "__main__":
# 	n, p = map(int, input().split())
# 	arr = cordRed(list(map(int, input().split())), n)
# 	resI = 0
# 	resMax = 0
# 	for i in range(n - p):
# 		auxAc = 0
# 		for j in range(p):
# 			ac = arr[i + j]
# 			for k in range(j + 1, p):
# 				auxAc += 1 if ac > arr[k + i] else 0
# 		resI, resMax = i, auxAc if auxAc > resMax else resMax
# 	print(resI + 1, resMax)

			