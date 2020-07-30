def stringCompression(string):
	newString, auxChar, count = [], None, 1									# O(1)
	for char in string:														# O(n)
		if char != auxChar or auxChar is None:									# O(1)
			auxChar, count = char, 1												# O(1)
			newString.append(auxChar)												# O(1)
			newString.append('1')														# O(1)
		else:																	# O(1)
			count += 1																# O(1)
			newString[-1] = str(count)												# O(1)
	return string if len(newString) >= len(string) else ''.join(newString)	# O(1)

def stringCompressionList(string):
	auxChar, count = None, 1																# O(1)
	for index, char in enumerate(string):													# O(n)
		if char != auxChar or auxChar is None:													# O(1)
			auxChar, count = char, 1																# O(1)
		else:																					# O(1)
			count += 1																				# O(1)
			string[index] = count																	# O(1)
	for i in range(len(string) - 1):														# O(n)
		if isinstance(string[i], int) and isinstance(string[i + 1], int): string[i] = '_'		# O(1)
	for i in range(len(string)):															# O(n)
		if isinstance(string[i], int): string[i] = str(string[i])								# O(1)
	return ''.join(string).replace('_', '')
print(stringCompressionList(["a","a","b","b","c","c","c"]))
print(stringCompression('aabcccccaaa'))