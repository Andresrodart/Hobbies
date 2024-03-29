MAXN = 20
log2 = [0]*(MAXN + 1)
for i in range(2, MAXN + 1):
  log2[i] = log2[int(i/2)] + 1

class SparseTable:
	def __init__(self, arr, length = None):
		self.arr = arr
		self.length = length if length else len(arr)
		self.k = log2[MAXN] + 1
		self.ST = [[[1 for _ in range(3)] for _ in range(self.k + 1)] for _ in range(MAXN)]
		self.build()
	def build(self, arr = None):
		#ToDo if arr reset k and length
		for j in range(1, self.k + 1):
			i = 0
			while(i + (1 << j) <= self.length):
				a = self.ST[i][j - 1][1]
				al = self.ST[i][j - 1][0] 
				ar = self.ST[i][j - 1][2]
				b = self.ST[i + (1 << (j - 1))][j - 1][1]
				bl = self.ST[i + (1 << (j - 1))][j - 1][0] 
				br = self.ST[i + (1 << (j - 1))][j - 1][2]
				if self.arr[i + (1 << (j - 1)) - 1] == self.arr[i + (1 << (j - 1))]:
					if(self.arr[i] == self.arr[i + (1 << (j - 1)) + j - 1]):
						self.ST[i][j][1] = (a + b)
						self.ST[i][j][0] = (a + b) 
						self.ST[i][j][2] = (a + b)
					elif self.arr[i] == self.arr[i + (1 << (j - 1))]:
						self.ST[i][j][1] = max(b, a + bl)
						self.ST[i][j][0] = (al + bl)
						self.ST[i][j][2] = br
					elif self.arr[i + (1 << (j - 1))] == self.arr[i + (1 << (j - 1)) + j - 1]:
						self.ST[i][j][1] = max(a, b + ar)
						self.ST[i][j][0] = al
						self.ST[i][j][2] = (br + ar)
					else:
						self.ST[i][j][1] = max(a, max(b, ar + bl))
						self.ST[i][j][0] = al 
						self.ST[i][j][2] = br
				else:
					self.ST[i][j][1] = max(a, b)
					self.ST[i][j][0] = al
					self.ST[i][j][2] = br
				i += 1

	def query(self, L, R):
		j = log2[R - L + 1];
		resA = self.ST[L][j];
		resB = self.ST[R - (1 << j) + 1][j];
		if resA == resB and resA == (1 << j):
			return resA + resB - (L - R + 2 * (1 << j) - 1);
		return max(resA, resB);

if __name__ == '__main__':
	n, query = map(int, input().split())
	while True:
		elements = list(map(int, input().split()))
		elements = SparseTable(elements, length = n)
		for i in elements.ST:
			print(i)
		while(query != 0):
			l, r = map(int, input().split())
			query -= 1
			print(elements.query(l - 1, r - 1))
		nxt = list(map(int, input().split()))
		if len(nxt) == 1: break
		test = nxt[0]
		query = nxt[1]

# import math
# MAXN = 10**5 + 1
# log = [0]*(MAXN+1)
# log[1] = 0;

# for i in range(2, MAXN + 1):
# 	log[i] = log[int(i/2)] + 1;

# class sparseTable:
# 	def __init__(self, F, n = None, k = None):
# 		self.n = MAXN if not n else n
# 		self.k = int(math.log2(self.n) + 2 if not k else k)
# 		self.F = F
# 		self.sparseTable = [[0] * self.k for i in range(self.n)] 
# 	def generate(self, array, length = None):
# 		size = length if length else len(array)
# 		for i in range(size):							# Init values
# 			self.sparseTable[i][0] = array[i]
# 		for j in range(1, self.k + 1):					# Iterate for each range in K
# 			i = 0
# 			while i + (1 << j) <= self.n:				# while i + 2**j less than n
# 				self.sparseTable[i][j] = self.F(self.sparseTable[i][j - 1], self.sparseTable[i + (1 << (j - 1))][j - 1])	# Compute F from both parts of range
# 				i += 1
# 	def query(self, R, L):
# 		j = log[R - L + 1];
# 		return min(self.sparseTable[L][j], self.sparseTable[R - (1 << j) + 1][j]);

# if __name__ == '__main__':
# 	test, query = map(int, input().split())
# 	while True:
# 		elements = sparseTable(min) 
# 		elements.generate(list(map(int, input().split())), length = test)
# 		while(query != 0):
# 			l, r = map(int, input().split())
# 			query -= 1
# 			print(elements.query(r, l))
# 		nxt = list(map(int, input().split()))
# 		if len(nxt) == 1: break
# 		test = nxt[0]
# 		query = nxt[1]