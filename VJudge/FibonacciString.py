q = int(input())
F = ['a', 'b']
i = 2
while i <= 45:
	F.append(F[i - 2] + F[i - 1])
	print(*F, sep='\n')
	i += 1
while q:
	n, k = map(int, input().rstrip().split())
	q -= 1