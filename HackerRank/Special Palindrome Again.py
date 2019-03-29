# Complete the substrCount function below.
import math

def	isPalindrome(n,s):
	specialChar = s[0]
	if n == 1:
		return True
	for i, j in zip(range(int(n/2)), range(n - 1, int(math.ceil(n/2)) - 1, -1)):
		if s[i] != s[j] or s[j] != specialChar:
			return False
	return True				
	

def substrCount(n, s):
	mem = {}
	res = substrPal(n, list(s), mem, 0)
	print(res)
	for i, j in zip(mem, mem.values()):
		if j == True:
			print(i, j)

def substrPal(n, s, mem, i):
	res = 0
	newString = []
	newStringLen = 0
	auxWord = s[:]
	space = ['\t']*i
	space = ''.join(space)
	for item, j in zip(s, range(i + 1, n + 1)):
		newString.append(item)
		auxWord.remove(item)
		newStringLen += 1
		if str(newString) + ':' + str(i) in mem:
			continue
		else:
			mem[str(newString) + ':' + str(i)] = isPalindrome(newStringLen, newString)
			res += 1 if mem[str(newString) + ':' + str(i)] else 0
		res += substrPal(n, auxWord, mem, j)
	return res


print(substrCount(7, 'abcbaba'))