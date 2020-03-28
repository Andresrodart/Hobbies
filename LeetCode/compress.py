def compress(text:list) -> int:
	auxChar, count = None, 1												# O(1)
	for index, char in enumerate(text):										# O(n)
		if char != auxChar or auxChar is None: auxChar, count = char, 1			# O(1)
		else: 																	# O(1)
			count += 1																# O(1)
			text[index] = count														# O(1)
	for i in range(len(text) - 1):											# O(n)
		if isinstance(text[i], int) and isinstance(text[i + 1], int): text[i] = '\t' # O(1)
	for i in range(len(text)):												# O(n)
		if isinstance(text[i], int): 											# O(1)
			num = list(str(text[i]))												# O(1) X <= len(text) < 19 (19 is the number of digits supported by int)
			for j in range(i - len(num) + 1, i + 1): text[j] = num.pop(0)		# O(1) X <= len(text) < 19 (19 is the number of digits supported by int)
	text[:] = [x for x in text if x != '\t']									# O(n)
	return text

# Just for the length
# def compress(text) -> int:
#  	auxChar, count, res = text[0], 1, len(text)								# O(1)
# 	for i in range(1, len(text)):											# O(n)
# 		if text[i] != auxChar:													# O(1)
# 			res -= max(0, count - 1 - len(str(count)))								# O(1) X <= len(text) < 19 (19 is the number of digits supported by int)
# 			auxChar, count = text[i], 0												# O(1)
# 		count += 1																# O(1)
# 	res -= max(0, count - 1 - len(text(count)))
# 	return res

print(compress(["a","a","b","b","c","c","c"]))
print(compress(["a"]))
print(compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))