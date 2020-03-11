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

def compression(sett):
	sett.sort()
	vals = {}
	i = 0
	for num in sett:
		vals[num] = i
		i += 1
	return vals, i

if __name__ == "__main__":
	sett = set() 
	points = []
	test = int(input())
	nPoints, k = map(int, input().split())
	pars, res = 1, 0
	for _ in range(nPoints):
		points.append(tuple(map(int, input().split())))
		sett.append(points[-1][0], points[-1][1])
	hashT, maxNum = compression(sett)
	maxNum2 = maxNum
	fenwickx = fenwick(k)
	fenwicky = fenwick(k)
	for point in points:
		fenwickx.update(hashT[point[0]], 1)
		fenwicky.update(hashT[point[1]], 1)
	while pars > res:
		pars = fenwickx.add(maxNum) + fenwicky.add(maxNum) - nPoints - 1