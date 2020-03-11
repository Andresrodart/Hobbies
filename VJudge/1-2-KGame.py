T = int(input())
for _ in range(T):
	n, k = map(int, input().split())
	if k % 3 != 0 or n < k: print('Alice' if n % 3 != 0 else 'Bob')
	else:
		if n % (k + 1) == 0: print('Bob')
		elif (n + 1) % (k + 1) == 0: print('Alice')
		else: print('Bob' if (n % (k + 1)) % 3 == 0 else 'Alice')