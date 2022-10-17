def addOdd(K: int) -> str:
	if K == 1: return '2'
	else:
		return '(2*' + (addEven(K - 1) if (K - 1) % 2 == 0 else addOdd(K - 1)) + ')'
def addEven(K: int) -> str:
	if K == 1: return '2'
	else:
		return '(' + (addEven(K // 2) if (K//2) % 2 == 0 else addOdd(K // 2))  + ')^2'
if __name__ == "__main__":
	T = int(input())
	stringBuilder = ''
	while T:
		K = int(input())
		if K == 1 or K % 2 == 0:
			stringBuilder = addEven(K)
		else:
			stringBuilder = '(2*' + addEven(K - 1) + ')'
		print(stringBuilder)
		T -= 1