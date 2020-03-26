# BS = Better space, BT = Better time
def checkPermutationBS(stringA, stringB):
	# stringA.lower() if case sensitive not needed
	# stringB.lower() if case sensitive not needed
	lenA, lenB = len(stringA), len(stringB)         # O(1)
	if lenA != lenB: return False                   # O(1)
	stringA, stringB =  sorted(stringA), sorted(stringB) # O(n log(n)) <- strings in python are not mutable so we need to use sorted
	for i in range(lenA):                           # O(n)
		if stringA[i] != stringB[i]: return False   # O(1)
	return True

def checkPermutationBT(stringA, stringB):
	# stringA.lower() if case sensitive not needed
	# stringB.lower() if case sensitive not needed
	lenA, lenB = len(stringA), len(stringB)         # O(1)
	if lenA != lenB: return False                   # O(1)
	hashTable = {}                                  # O(1)
	for char in stringA:                            # O(n)
		if char in hashTable: hashTable[char] += 1      # O(1)
		else: hashTable[char] = 1                       # O(1)
	for char in stringB:                            # O(n)
		if char not in hashTable: return False      	# O(1)
		else: hashTable[char] -= 1                  	# O(1)
	for value in hashTable.values():				# O(n)
		if value != 0: return False						# O(1)
	return True

print(checkPermutationBS('asdfg', 'gasfd'), checkPermutationBT('asdfg', 'gasfd'))
print(checkPermutationBS('asdf', 'addf'), checkPermutationBT('asdf', 'addf'))
print(checkPermutationBS('', ''), checkPermutationBT('', ''))
print(checkPermutationBS('', 'qwer'), checkPermutationBT('', 'qwer'))
print(checkPermutationBS('CAT', 'ACT'), checkPermutationBT('CAT', 'ACT'))