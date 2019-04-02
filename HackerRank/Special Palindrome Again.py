def eulerSum(num):
	return num*(num + 1)/2

def anagrama(n, cad):
	inChar = cad[0]
	inRowL, inRowR = 1, 0
	res, i = 0, 1
	aBreak = False
	while i <= n:
		if i == n:
			res += eulerSum(inRowL) + eulerSum(inRowR)
			i += 1
			continue	

		if inChar == cad[i]:
			if not aBreak:
				inRowL += 1
			else:
				if inRowR < inRowL:
					res += 1
				inRowR += 1
			i += 1	
		
		else:
			aBreak = True
			res += eulerSum(inRowR) + eulerSum(inRowL)
			if i + 1 < n and inChar == cad[i + 1]:
				if i + 2 < n and cad[i] == cad[i + 2]:
					res += 1
				res += 2
				inRowR = 1
				i += 2 if i + 2 <= n else 1
			else:
				inChar = cad[i]
				inRowL, inRowR = 1, 0
				i += 1
				aBreak = False
			
	return res

print(anagrama(6,'ccaccc'))
print(anagrama(5,'asasd'))
print(anagrama(7,'abcbaba'))

# Complete the substrCount function below.
#import math
#
#def	isPalindrome(n,s):
#	specialChar = s[0]
#	if n == 1:
#		return True
#	for i, j in zip(range(int(n/2)), range(n - 1, int(math.ceil(n/2)) - 1, -1)):
#		if s[i] != s[j] or s[j] != specialChar:
#			return False
#	return True				
#	
#
#def substrCount(n, s):
#	mem = {}
#	res = substrPal(n, list(s), mem, 0)
#	print(res)
#	for i, j in zip(mem, mem.values()):
#		if j == True:
#			print(i, j)
#
#def substrPal(n, s, mem, i):
#	res = 0
#	newString = []
#	newStringLen = 0
#	auxWord = s[:]
#	space = ['\t']*i
#	space = ''.join(space)
#	for item, j in zip(s, range(i + 1, n + 1)):
#		newString.append(item)
#		auxWord.remove(item)
#		newStringLen += 1
#		if str(newString) + ':' + str(i) in mem:
#			continue
#		else:
#			mem[str(newString) + ':' + str(i)] = isPalindrome(newStringLen, newString)
#			res += 1 if mem[str(newString) + ':' + str(i)] else 0
#		res += substrPal(n, auxWord, mem, j)
#	return res


#print(substrCount(7, 'abcbaba'))