T = int(input())
for cases in range(T):
	matrix = []
	N = int(input())
	repeatedCols, repeatedRows, det = 0, 0, 0
	for line in range(N):
		matrix.append(list(map(int, input().split())))
	
	for i in range(N):
		check = set()
		for j in range(N): check.add(matrix[i][j])
		if len(check) < N: repeatedRows += 1
	
	for i in range(N):
		check = set()
		for j in range(N): check.add(matrix[j][i])
		if len(check) < N: repeatedCols += 1
	
	for i in range(N): det += matrix[i][i]
	
	print('Case #{}: {} {} {}'.format(T + 1, det, repeatedRows, repeatedCols))
	# rows = [set() for i in range(N)]
	# rowC = [False for i in range(N)]
	# cols = [set() for i in range(N)]
	# colC = [False for i in range(N)]
	# for i in range(N):
	# 	for j in range(N):
	# 		num = matrix[i][j]
	# 		rep = 0
	# 		for k in range(N):
	# 			if
	# 		# if num in rows[i] and not rowC[i]: 
	# 		# 	repeatedRows += 1
	# 		# 	rowC[i] = True
	# 		# else: rows[i].add(num)			
	# 		# if num in cols[j] and not colC[j]: 
	# 		# 	repeatedCols += 1
	# 		# 	colC[j] = True
	# 		# else: cols[j].add(num)
			
	# 		if i == j: det += num			
