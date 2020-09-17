def getNext(n:'int') -> 'int':
	temp = n
	c0 = c1 = 0
	while (temp & 1) == 0 and temp != 0:
		c0 += 1
		temp >>= 1 
	while (temp & 1) == 1:
		c1 += 1
		temp >>=1
	if c0 + c1 >= 31 or c0 +c1 == 0: return -1
	p = c0 + c1
	n |= 1 << p
	n &= ~((1 << p) - 1)
	n |= (1 << (c1 - 1)) - 1
	return n
def getPrev(n: 'int') -> 'int':
	temp = n
	c0 = c1 = 0
	while (temp & 1) == 1:
		c1 += 1
		temp >>=1
	if temp == 0: return -1
	while (temp & 1) == 0 and temp != 0:
		c0 += 1
		temp >>= 1
	p = c0 + c1
	n &= ~((1 << p + 1) - 1)
	n |= ((1 << c1 + 1) - 1) << c0 - 1
	return n
print('{0:b}'.format(13948))
print('{0:b}'.format(getNext(13948)))
print('{0:b}'.format(getPrev(int('10011110000011', base=2))))