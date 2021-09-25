from functools import reduce

def fitsInStorage(arry:list, arrySize: int, maxSize: int, nItems: int) -> bool:
	for idx in range(0, arrySize - nItems):
		if reduce(lambda a, b: a + b, arry[idx: idx + nItems]) > maxSize:
			return False
	return True

def searchMaxR(arry: list, arrySize: int, maxSize: int) -> int:
	L, R = 0, arrySize
	ans = 0
	while L <= R:
		mid = (L + R) // 2
		if(fitsInStorage(arry, arrySize, maxSize, mid)):
			L = mid + 1
			ans = mid
		else: 
			R = mid - 1
	return ans

def searchMinL(arry: list, arrySize:list, maxSize: int, RElements: int) -> int:
	for idx in range(arrySize - RElements - 1):
		if reduce(lambda a, b: a + b, arry[idx: idx + RElements + 1]) > maxSize:
			return idx + 1
	return -1

if __name__ == "__main__":
	N, C = input().rstrip().split()
	sizes = list(map(int, input().rstrip().split()))
	N = int(N)
	if(C[-1] == 'M'): C = int(C[:-1])
	elif(C[-1] == 'G'): C = int(C[:-1]) * 1024
	elif(C[-1] == 'T'): C = int(C[:-1]) * 1024 * 1024

	R = searchMaxR(sizes, N, C)
	L = searchMinL(sizes, N, C, R)
	print(R, L)
