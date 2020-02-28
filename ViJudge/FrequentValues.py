import math
MAXN = 10**5 + 1
log = [0]*(MAXN+1)
log[1] = 0;

for i in range(2, MAXN + 1):
	log[i] = log[int(i/2)] + 1;

class sparseTable:
	def __init__(self, F, n = None, k = None):
		self.n = MAXN if not n else n
		self.k = int(math.log2(self.n) + 2 if not k else k)
		self.F = F
		self.sparseTable = [[0] * self.k for i in range(self.n)] 
	def generate(self, array, length = None):
		size = length if length else len(array)
		for i in range(size):							# Init values
			self.sparseTable[i][0] = array[i]
		for j in range(1, self.k + 1):					# Iterate for each range in K
			i = 0
			while i + (1 << j) <= self.n:				# while i + 2**j less than n
				self.sparseTable[i][j] = self.F(self.sparseTable[i][j - 1], self.sparseTable[i + (1 << (j - 1))][j - 1])	# Compute F from both parts of range
				i += 1
	def query(self, R, L):
		j = log[R - L + 1];
		return min(self.sparseTable[L][j], self.sparseTable[R - (1 << j) + 1][j]);

if __name__ == '__main__':
	test, query = map(int, input().split())
	while True:
		elements = sparseTable(min) 
		elements.generate(list(map(int, input().split())), length = test)
		while(query != 0):
			l, r = map(int, input().split())
			query -= 1
			print(elements.query(r, l))
		nxt = list(map(int, input().split()))
		if len(nxt) == 1: break
		test = nxt[0]
		query = nxt[1]