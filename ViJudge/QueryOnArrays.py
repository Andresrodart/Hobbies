class fenwick:
	def __init__(self, n, arr = None):
		self.maxList = (n + 1)
		self.fenwick = [0] * (n + 1)
		if arr:
			for i in range(n):
				self.add(i, arr[i])
	def update(self, pos, delta):
		l = pos
		prevDelta = self.addition(pos) - self.addition(pos - 1)
		while l < self.maxList:
			self.fenwick[l] -= prevDelta
			l = l | (l + 1)
		l = pos
		while l < self.maxList:
			self.fenwick[l] += delta
			l = l | (l + 1)
	def add(self, l, delta):
		while l < self.maxList:
			self.fenwick[l] += delta
			l = l | (l + 1)
	def addition(self, r):
		if r < 0:
			return 0
		res = 0
		while r >= 0:
			res += self.fenwick[r]
			r = (r & (r + 1)) - 1
		return res

if __name__ == "__main__":
	n = int(input())
	arr = list(map(int, input().split()))
	q = int(input())
	fnwick = fenwick(n, arr=arr)
	for i in range(n):
		print(fnwick.addition(i), end=" ")
	print("")
	while q > 0:
		query = list(map(int, input().split()))
		if(query[0] == 2):
			i, j = 0, -1
			res = "NO"
			while i < fnwick.maxList and j < fnwick.maxList:
				suffix = fnwick.addition(i) - fnwick.addition(j)
				if(suffix == query[1]):
					res = "YES"
					break
				if suffix < query[1]:
					x = int((n - i)/2) + 1
					if x + i < n:
						auxSuffix = fnwick.addition(i + x) - fnwick.addition(j)
						i += (x + 1) if auxSuffix < query[1] else 1
					else:
						i += 1
				if suffix > query[1]:
					x = int((i - j)/2) + 1
					auxSuffix = fnwick.addition(i) - fnwick.addition(j + x)
					j += x + 1 if suffix > query[1] else 1
			print(res)
		else:
			fnwick.update(query[1] - 1, query[2])
		q -= 1

# if __name__ == "__main__":
# 	n = int(input())
# 	arr = list(map(int, input().split()))
# 	q = int(input())
# 	while q > 0:
# 		query = list(map(int, input().split()))
# 		if(query[0] == 2):
# 			suffix = 0
# 			i = 0
# 			res = "NO"
# 			for elem in arr:
# 				if suffix + elem < query[1]:
# 					suffix, i = (suffix + elem), i  
# 				else:
# 					suffix, i = (suffix + elem - arr[i]), (i + 1)
# 				if suffix == query[1]:
# 					res = "YES"
# 					break
# 			for j in range(i, n):
# 				suffix = (suffix - arr[j])
# 				if suffix == query[1]:
# 					res = "YES"
# 					break
# 			print(res)
# 		else:
# 			arr[query[1] - 1] = query[2]
# 		q -= 1

#  if __name__ == "__main__":
# 	n = int(input())
# 	arr = list(map(int, input().split()))
# 	q = int(input())
# 	while q > 0:
# 		query = list(map(int, input().split()))
# 		if(query[0] == 2):
# 			suffix = arr[0]
# 			i = 0
# 			j = 1
# 			res = "NO"
# 			while(i < n):
# 				if suffix > query[1] or j == n:
# 					suffix -= arr[i]
# 					i += 1
# 				elif suffix < query[1] and j < n:
# 					suffix += arr[j]
# 					j += 1
# 				if suffix == query[1]:
# 					res = "YES"
# 					break
# 			print(res)
# 		else:
# 			arr[query[1] - 1] = query[2]
# 		q -= 1