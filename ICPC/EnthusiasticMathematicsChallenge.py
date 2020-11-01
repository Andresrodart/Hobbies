from itertools import permutations
import math
import sys

def isPrime(n):
    if (n % 2 == 0 and n > 2) or n <= 1: return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0: return False
    return True

def findPrime(S):
	primesStart = [[] for _ in range(len(S) + 1)]
	for i in range(len(S)):
		for j in range(i + 1, len(S) + 1):
			num = int(S[i: j])
			if isPrime(num) and S[i] != 0: primesStart[i].append((num, j))
	return primesStart
def makeThreesomes(S):
	res = sys.maxsize
	primesStart = findPrime(S)
	for num, end in primesStart[i]:
		for num2, end2 in primesStart[end]:
			for num3, end3 in primesStart[end2]:
				# print(num, num2, num3, end, end2, end3)
				if end3 >= len(S): res = min(res, num * num2 * num3)
	return res

S = input()
i = 0
res = makeThreesomes(S)
if res == sys.maxsize: print('Bob lies')
else: print(res)