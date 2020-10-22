n = int(input())
a = list(map(int, input().rstrip().split()))
res = [0]
multiplayer = 1
# TrianguleMaker(a, 0, res, None, None, None)
for i in range(len(a) - 2):
	for j in range(i + 1, len(a) - 1):
		for k in range(j + 1, len(a)):
			if a[i] != a[j] and a[j] != a[k] and a[i] != a[k] and a[i] + a[j] > a[k] and a[k] + a[j] > a[i] and a[i] + a[k] > a[j]:
				res[0] += 1
print(res[0]) 

