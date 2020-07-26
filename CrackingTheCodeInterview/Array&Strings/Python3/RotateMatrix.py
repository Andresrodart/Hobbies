def rotateMatrix(matrix):
	N = len(matrix[0]) 
	for j in range(N // 2):				# O(n^2)
		for i in range(N - 1 - 2 * j):		# O(n)
			matrix[j][i + j], matrix[i + j][N - 1 - j] =  matrix[i + j][N - 1 - j], matrix[j][i + j]					# O(1)
			matrix[j][i + j], matrix[N - 1 - j][N - i - 1 - j] =  matrix[N - 1 - j][N - i - 1 - j], matrix[j][i + j]	# O(1)
			matrix[j][i + j], matrix[N - i - 1 - j][j] =  matrix[N - i - 1 - j][j], matrix[j][i + j]					# O(1)
	return matrix

def print_matrix(matrix):
	print('----------------')
	for i in matrix:
		print(i)

# print_matrix(rotateMatrix([
# 	[1, 2, 3, 4],
# 	[5, 6, 7, 8],
# 	[9, 10, 11, 12],
# 	[13, 14, 15, 16],
# ]))
print_matrix(rotateMatrix([
[1, 2, 3, 4, 5],
[16, 17, 18, 19, 6],
[15, 24, 25, 20, 7],
[14, 23, 22, 21, 8],
[13, 12, 11, 10, 9],
]))