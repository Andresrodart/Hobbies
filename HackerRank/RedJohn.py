#!/bin/python3

import math
import os
import random
import re
import sys
import operator as op
from functools import reduce

primes = []

def ncr(n, r):
	r = min(r, n-r)
	numer = reduce(op.mul, range(n, n-r, -1), 1)
	denom = reduce(op.mul, range(1, r+1), 1)
	return numer / denom


def criba_eratostenes(n):
	multiplos = set()
	for i in range(2, n+1):
		if i not in multiplos:
			primes.append(i);
			multiplos.update(range(i*i, n+1, i))

# Complete the redJohn function below.
def redJohn(n):
	if n < 4:
		return 0
	elif n == 4:
		return 1
	else:
		total = 0
		result = 0
		for i in range(int(n / 4) + 1):
			total = int(total + ncr(n - i*4  + i, i))
		for i in primes:
			if i > total:
				break
			result = result + 1
		return result

if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')
	criba_eratostenes(217287)
	t = int(input())

	for t_itr in range(t):
		n = int(input())

		result = redJohn(n)

		fptr.write(str(result) + '\n')

	fptr.close()
