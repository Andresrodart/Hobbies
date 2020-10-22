def maxRepOpt1(text: str) -> int:
	arr, rev = [], []
	last = None
	count = res = i = 0
	isUnion = False
	for char in text:
		if char != last and last is not None:
			arr.append((count, last))
			count = 0
		last = char
		count += 1
	arr.append((count, last))       
	res = max_subString(arr)
	arr.reverse()
	return max(res, max_subString(arr))

def max_subString(arr):
	i = res = 0
	hasSeen = set()
	while i < len(arr):
		if i + 2 < len(arr) and arr[i + 1][0] == 1 and arr[i][1] == arr[i + 2][1]:
			res = max(arr[i][0] + arr[i + 2][0] + (1 if arr[i][1] in hasSeen else 0), res)
		else: 
			res = max(res, arr[i][0] + (1 if arr[i][1] in hasSeen else 0))
		hasSeen.add(arr[i][1])
		i += 1
	return res

print(maxRepOpt1('aaaabeeeaeebbbbbb'))
print(maxRepOpt1('ababa'))
print(maxRepOpt1('aaabbaaa'))
print(maxRepOpt1('bbababaaaa'))
print(maxRepOpt1('aabaaabaaaba'))
print(maxRepOpt1('aabbaba'))