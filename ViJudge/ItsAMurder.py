maxList = 10**6 + 10
fenwick = [0] * maxList

def update(l, delta):
	while l < maxList:
		fenwick[l] += delta
		l = l | (l + 1)

def add(r):
	res = 0;
	while r >= 0:
		res += fenwick[r];
		r = (r & (r + 1)) - 1
	return res

if __name__ == '__main__':
	T = int(input())
	aux = []
	for _ in range(T):
		res = 0
		leng = int(input()) - 1
		stairs = list(map(int, input().split()))
		for num in stairs:
			res += add(num - 1)
			update(num, num)
		print(int(res))