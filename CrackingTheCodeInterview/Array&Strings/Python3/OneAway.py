def addCharDistance(stringA, stringB):
	lenA, lenB, i, j, dif = len(stringA), len(stringB), 0, 0, 0		# O(1)
	while i < lenA and j < lenB:									# O(A)
		if dif > 1: return False										# O(1)
		if stringA[i] != stringB[j]:									# O(1)
			i += 1														# O(1)
			dif += 1													# O(1)
		else:															# O(1)
			i += 1														# O(1)
			j += 1
	dif += lenA - i													# O(1)
	return True if dif <= 1 else False 								# O(1)

def changeCharDistance(stringA, stringB):
	lenA, lenB, i, j, dif = len(stringA), len(stringB), 0, 0, 0		# O(1)
	while i < lenA and j < lenB:									# O(N)
		if dif > 1: return False										# O(1)
		if stringA[i] != stringB[j]: dif += 1							# O(1)					
		i += 1															# O(1)
		j += 1															# O(1)
	return True if dif <= 1 else False									# O(1)

def oneAwaySimple(A, B):
	lenA = len(A)					# O(1)
	lenB = len(B)					# O(1)
	i, j, dif = 0, 0, 0				# O(1)
	while i < lenA and j < lenB:	# O(A)
		if dif > 1: return False				# O(1)
		if A[i] != B[j]:						# O(1)
			if lenA > lenB:						# O(1)
				i, dif = i + 1, dif +1 				# O(1)
			else:								# O(1)
				i, j, dif = i + 1, j + 1, dif +1	# O(1)
		else:									# O(1)
			i, j = i + 1, j + 1						# O(1)
	dif += lenA - i;						# O(1)
	return True if dif <= 1 else False; 	# O(1)


def oneAway(stringA, stringB):
	lenA, lenB, i, j = len(stringA), len(stringB), 0, 0				# O(1)
	dif = lenA - lenB												# O(1)
	if abs(dif) > 1: return False									# O(1)
	elif dif < 0: 	return oneAwaySimple(stringB, stringA)		# O(N) N = maxLength(lenA, lenB)
	return oneAwaySimple(stringA, stringB)						# O(N) N = maxLength(lenA, lenB)
	# if dif == 0: return changeCharDistance(stringA, stringB)		# O(N)
	# elif dif < 0: 	return addCharDistance(stringB, stringA)		# O(N) N = maxLength(lenA, lenB)
	# return addCharDistance(stringA, stringB)						# O(N) N = maxLength(lenA, lenB)

s = "aDb"
t = "adb"

print(oneAway(s, t))
print(oneAway("bcde", "abcde"))
print(oneAway('pale', 'ple'))
print(oneAway('pales', 'pale'))
print(oneAway('pale', 'bale'))
print(oneAway('pale', 'bake'))
print(oneAway('pal', 'palee'))
