def value(chart):
	if chart == 'A': return 1
	else: return -1

def thresome(colors, N):
	print(colors)
	i = 0
	if len(colors) == 1: return True
	while i + 2 < N:
		res = value(colors[i]) + value(colors[i + 1]) + value(colors[i + 2])
		if abs(res) < 3:
			new = colors[:i] + ['B' if res < 0 else 'A'] + colors[i + 3:]
			is_good = thresome(new, len(new))
			if is_good: return True
		i += 1 
	return False

if __name__ == "__main__":
	f = open("res.txt", "w")
	T = int(input())
	for case in range(T):
		N = int(input())
		colors = list(input())
		A = colors.count('A')
		B = colors.count('B')
		res = abs(A - B)
		f.write('Case #{}: '.format(case + 1) + ('Y' if thresome(colors, N) else 'N') + '\n')
	f.close()