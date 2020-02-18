numbers = [0] * (10**5)

def updateNumbers(num):
	for i in range(num, (10**5)):
		numbers[i] = numbers[i] + num

if __name__ == "__main__":
	res = 0
	T = int(input())
	for _ in range(T):
		leng = int(input()) - 1
		stairs = list(map(int, input().split()))
		for num in stairs:
			res = res + numbers[num - 1]
			updateNumbers(num)
		print(res)