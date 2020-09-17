import sys
def flipBit(num):
	if ~num == 0: return int.bit_length(sys.maxsize)
	prevLength = currLength = maxSize = 0
	while num != 0:
		if num & 1 == 1: currLength += 1
		else:
			prevLength = 0 if num & 2 == 0 else currLength
			currLength = 0
		maxSize = max(prevLength + currLength + 1, maxSize)
		num >>= 1
	return maxSize

print(flipBit(sys.maxsize))
print(flipBit(1775))
print(flipBit(883))