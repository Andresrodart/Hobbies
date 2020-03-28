def addCharDistance(stringA, stringB):
	lenA, lenB, i, j, dif = len(stringA), len(stringB), 0, 0, 0		# O(1)
	while i < lenA and j < lenB:									# O(A)
		if dif > 1: return False										# O(1)
		if stringA[i] != stringB[j]:									# O(1)
			if lenA > lenB: i += 1										# O(1)
			else: i, j = i + 1, j + 1									# O(1)
			dif += 1													# O(1)
		else:															# O(1)
			i += 1														# O(1)
			j += 1
	dif += lenA - i													# O(1)
	return True if dif == 1 else False 								# O(1)

def changeCharDistance(stringA, stringB):
	lenA, lenB, i, j, dif = len(stringA), len(stringB), 0, 0, 0		# O(1)
	while i < lenA and j < lenB:									# O(N)
		if dif > 1: return False										# O(1)
		if stringA[i] != stringB[j]: dif += 1							# O(1)					
		i += 1															# O(1)
		j += 1															# O(1)
	return True if dif == 1 else False									# O(1)

def oneEditDistance(stringA, stringB):
	lenA, lenB, i, j = len(stringA), len(stringB), 0, 0				# O(1)
	dif = lenA - lenB												# O(1)
	if abs(dif) > 1: return False									# O(1)
	if dif == 0: return changeCharDistance(stringA, stringB)		# O(N)
	elif dif < 0:													# O(1)
		lenA, lenB = lenB, lenA											# O(1)
		stringA, stringB = stringB, stringA								# O(1)
	return addCharDistance(stringA, stringB)						# O(N) N = maxLength(lenA, lenB)

print(oneEditDistance('a', 'ab'))
print(oneEditDistance('ab', 'a'))
print(oneEditDistance('ab', 'ab'))
print(oneEditDistance('aDb', 'adb'))
print(oneEditDistance("bcde", "abcde"))
	