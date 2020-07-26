# T = int(input())
# for _ in range(T):
# 	n, k = map(int, input().split())
# 	arry = list(map(int, input().split()))
# 	res = 0
# 	if arry == sorted(arry) or (arry == sorted(arry, reverse = True) and k >= int(n / 2)): print('Yes')
# 	else:
# 		for i in range(1, n):
# 			if arry[i - 1] > arry[i]: res += 1
# 			if arry[i - 1] > arry[-i] and arry[-i] < arry[i]: arry[i - 1], arry[-i] = arry[- i], arry[i - 1]
# 			if arry[i - 1] > arry[-i] and arry[-i] < arry[i]: arry[i - 1], arry[-i] = arry[- i], arry[i - 1]
# 			if res > k: 
# 				res = 'N'
# 				break
# 		if res == 'N': print('No')
# 		else: print('Yes')

n = int(input())
numbers = []
res = 'N'
def first(string):
	return string[0]
def bigger(a, b):
	for i in range(len(a)):
		if a[i][0] > b[0]: return True
		elif a[i][0] < b[0]: return False
	return True

for _ in range(n):
	number = list(input())
	number.sort(reverse=True)
	number = ''.join(number)
	numbers.append(number)
numbers.sort(key = first)
for number in numbers:
	if res == 'N': res = [number]
	elif bigger(res, number): res.append(number) 
	else: res.insert(0, number)
	print(res)
print(''.join(res))

# m = int(input())
# forbidden = set()
# i, j = 1, 1
# res = -1
# for _ in range(m): forbidden.add(int(input()))
# ith_number = int(input())
# while i < ith_number:
#     j += 1
#     if j in forbidden: continue
#     i += 1
#     res = j
# print(res)