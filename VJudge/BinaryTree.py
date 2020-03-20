cases = int(input())
for _ in range(cases):
	nodes = int(input())
	for edge in range(nodes - 1): root, child = map(int, input().split())
	print('Alice' if nodes % 2 != 0 else 'Bob')