if __name__ == "__main__":
	f = open("res.txt", "w")
	T = int(input())
	for case in range(T):
		N = int(input())
		incoming = list(input())
		outgoing = list(input())
		res = [[0] * N for i in range(N)]
		for i in range(N):
			for j in range(N):
				if i == j: res[i][j] = 'Y'
				elif outgoing[i] == 'N' or incoming[j] == 'N': res[i][j] = 'N'
				elif i > j:
					for distance in range(1, i - j + 1):
						if incoming[i - distance] == 'N' or outgoing[i - distance + 1] == 'N': 
							res[i][j] = 'N'
							break
						else: res[i][j] = 'Y'
				elif j > i:
					for distance in range(1, j - i + 1):
						if incoming[i + distance] == 'N' or outgoing[i + distance - 1] == 'N': 
							res[i][j] = 'N'
							break
						else: res[i][j] = 'Y'
		f.write('Case #{}:'.format(case + 1) + '\n')
		for i in range(N):
			f.write(''.join(res[i]) + '\n')
	f.close()