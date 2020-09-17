def checkString(string, size):
	aux = {'1': 0, '2':0, '3':0}
	for j in range(size): aux[string[j]] += 1
	for i in range(len(string) - size):
		if aux['1'] > 0 and aux['2'] > 0 and aux['3'] > 0: return True
		aux[string[i]] -= 1
		aux[string[i + size]] += 1
	if aux['1'] > 0 and aux['2'] > 0 and aux['3'] > 0: return True
	return False
cases = int(input())
for _ in range(cases):
	string = input()
	l, r = 0, len(string)
	while l <= r:
		mid = (l + r) // 2
		res = checkString(string, mid)
		if l == r and res: l = r + 1
		if res: r = mid
		else: l = mid + 1
	print(0 if not res else mid)