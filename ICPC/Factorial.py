import math

max_n = int(10 ** 5)
b = 1
c = math.factorial(b)
facs = [c]
while c < max_n:
	b += 1
	c = math.factorial(b)
	facs.append(c)
N = int(input())
l = 0
r = len(facs) - 1
print(min_n(N, facs))