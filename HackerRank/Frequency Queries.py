import math
import os
import random
import re
import sys

def freqQuery(queries):
	res = []
	maphash = {}
	freq = {}
	for query in queries:
		if query[0] == 1 or  query[0] == 2:
			if query[1] in maphash and maphash[query[1]] in freq and freq[maphash[query[1]]] > 0: freq[maphash[query[1]]] -= 1
			if query[0] == 1:
				if query[1] in maphash: maphash[query[1]] += 1
				else: maphash[query[1]] = 1
			elif query[0] == 2:
				if query[1] in maphash and maphash[query[1]] > 0: maphash[query[1]] -= 1
				else: maphash[query[1]] = 0
			if maphash[query[1]] in freq: freq[maphash[query[1]]] += 1
			else: freq[maphash[query[1]]] = 1
		else: res.append(1 if query[1] in freq else 0)
	return res

if __name__ == '__main__':
	q = int(input().strip())

	queries = []

	for _ in range(q):
		queries.append(list(map(int, input().rstrip().split())))

	ans = freqQuery(queries)

	print('\n'.join(map(str, ans)))