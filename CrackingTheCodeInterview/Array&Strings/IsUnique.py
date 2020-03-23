# Is necessary to start the iteration from 1 and not in zero, because if string is empty the size - 1 is negative
def isUnique(string):
	auxStr = sorted(string)                             # O(n log(n))
	for i in range(1, len(auxStr)):                    # O(n)
		if auxStr[i] == auxStr[i - 1]: return False         # O(1)
	return True

print(isUnique('sdadsa'), isUnique(''), isUnique('asdfghjk'), isUnique('asdffghjklzz'), sep = '\n')