def eulerSum(num):
	return num*(num + 1)/2
#This code what makes is first chechs all substring that equal then  get the total number of substrimngf from that that is len(len + 1)2
#Then we check for that substrings for the ones with middle char and take the one with lesc cahracters
#For simler code waht we can make is make another auclist with has the lenght of the first while, then chckin thart lsit from pos 1 with index as i if it is 1 and i - 1 and 1 + 1 are from the same char 
#eg { a-0:2, x-1:1, a-2:3} then we can sum the min(2, 3)
def substrCount(n, cad):
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
				inRowL += 1
		else:
			res += eulerSum(inRowL)
			inChar = cad[i]
			inRowL = 1
		i += 1
	
	inChar = cad[0]
	i, inRowL = 1, 1
	for i in range(1, n + 1):
		if i == n:
			if aBreak:
				res += min(inRowL, inRowR)	
			i += 1
			continue	
			
		if inChar == cad[i]:
			if not aBreak:		
				inRowL += 1
			else:
				inRowR += 1
						
		else:	
			if not aBreak:
				aBreak = True
				if i + 1 < n and inChar == cad[i + 1]:
					if i + 2 < n and cad[i] == cad[i + 2]:
						res += 1
				else:
					inChar = cad[i]
					inRowL, inRowR= 1, 0
					aBreak = False
			else:
				res += min(inRowL, inRowR)
				if i + 1 < n and inChar == cad[i + 1]:
					if i + 2 < n and cad[i] == cad[i + 2]:
						res += 1
					inRowL, inRowR = inRowR, 0
				else:
					inChar = cad[i]
					inRowL, inRowR = 1, 0
					aBreak = False
		#print(res, inRowL, inRowR, cad[i], inChar)
	return int(res)


print(substrCount(5,'asasd'))
print(substrCount(7,'abcbaba'))
print(substrCount(4,'aaaa'))
print(substrCount(6,'ccacac'))


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
