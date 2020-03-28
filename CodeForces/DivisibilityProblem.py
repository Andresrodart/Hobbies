from math import ceil
cases = int(input())
while cases:
	a, b = map(int, input().split())
	print(int(ceil(a / b)) * b - a)
	cases -= 1