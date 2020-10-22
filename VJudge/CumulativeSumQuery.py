n = int(input())
a = list(map(int, input().rstrip().split()))
q = int(input())
prefix = []
res = 0
for num in a:
	res += num 
	prefix.append(res)
print(prefix)
while q:
	i, j = map(int, input().rstrip().split())
	if i == 0: print(prefix[j])
	else: print(prefix[j] - prefix[i - 1])
	q -= 1