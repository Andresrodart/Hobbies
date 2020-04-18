T = int(input())
for case in range(1, T + 1):
	digits = list(map(int, list(input())))
	res = []
	currentDepth = 0
	for index in range(len(digits)):
		num = digits[index]
		if num > currentDepth:
			res.extend(['(' for i in range(num - currentDepth)])
			currentDepth = num
		res.append(str(num))
		if index < len(digits) - 1 and digits[index + 1] < currentDepth:
			res.extend([')' for i in range(currentDepth - digits[index + 1])])
			currentDepth = digits[index + 1]
	res.extend([')' for i in range(num)])
	print('Case #{}: {}'.format(case, ''.join(res)))