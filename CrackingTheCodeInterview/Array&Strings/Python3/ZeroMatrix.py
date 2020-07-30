def zeroMatrix(matrix):
	for i in range(len(matrix[0])):
		for j in range(len(matrix[0])):
			if matrix[i][j] == 0:
				#Note it will just work for n*n matrix
				for k in range(len(matrix[0])):
					matrix[i][k] = '-'
					matrix[k][j] = '-'
	for i in range(len(matrix[0])):
		for j in range(len(matrix[0])):
			if matrix[i][j] == '-': matrix[i][j] = 0
	return matrix
def print_matrix(matrix):
	print('----------------')
	for i in matrix: print(*i, sep='\t')

print_matrix(zeroMatrix([
[1, 2, 3, 0, 5],
[16, 17, 18, 19, 6],
[15, 24, 25, 20, 7],
[14, 0, 22, 0, 8],
[13, 12, 11, 10, 9],
]))