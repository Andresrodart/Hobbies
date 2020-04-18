def hasA4(N1, N2):
	for i in range(len(N1)):
		if N1[i] == 4: return True, i
	for i in range(len(N2)):
		if N2[i] == 4: return True, i
	return False, -1
		
T = int(input())
for i in range(1, T + 1):
	N = int(input())
	N1 = int(N/2)
	N2 = list(map(int, str(N - N1)))
	N1 = list(map(int, str(N1)))
	eitherHasAFour, index = hasA4(N1, N2)
	while eitherHasAFour:
		if N1[index] > 0 and N2[index] < 9:
			N1[index] -= 1
			N2[index] += 1
		else:
			N1[index] += 1
			N2[index] -= 1
		eitherHasAFour, index = hasA4(N1, N2)
	print('Case #{}: {} {}'.format(i, ''.join(map(str, N1)), ''.join(map(str, N2))))