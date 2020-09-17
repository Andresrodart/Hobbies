def insertion(N, M, i, j):
	right = (1 << i) - 1
	left = ~0 << j + 1
	mask = right | left
	return (N & mask) | (M << i)

print('{0:b}'.format(insertion(1 << 10, 19, 2, 6)))