def bitSwapRequired(a: 'int', b: 'int') -> 'int':
	res = 0
	while a != 0 or b != 0:
		res += (a & 1) ^ (b & 1)
		a, b = a >> 1, b >> 1
	return res

def bitSwapRequiredBook(a: 'int', b: 'int') -> 'int':
	res, c = 0, a ^ b
	while c != 0:
		res += 1
		c = c & c - 1
	return res

print(bitSwapRequired(29, 15))
print(bitSwapRequiredBook(29, 15))
