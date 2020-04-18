import sys
#Onnly case 1 and 2 works
def isEqual(A, B):
	return A == B

def isNegated(A, B):
	aux = []
	for val in A:
		if val == '1': aux.append('0')
		else: aux.append('1')
	return isEqual(aux, B)

def isReversed(A, B):
	lenaux = len(B)
	aux = ['2'] * lenaux
	for i in range(lenaux):
		aux[i] = A[len(A) - i - 1]
	# print(A, lenaux, aux, B)
	return isEqual(aux, B)

def getComparators(A, C, size):
	a, c = ['2']*size, ['2']*size
	for i in range(size):
		a[i], c[i] = A[i], C[i]
	return a, c

def case10():
	A = ['2'] * 10
	for i in range(1, 11):
		print(i)
		sys.stdout.flush()
		A[i - 1] = input()
	print(''.join(A))
	sys.stdout.flush()

def case20():
	A, C = ['2']*20, ['2']*20
	# Because of swap we have to take from out to in (1 - 20), (2 - 19), ..., (10 - 11) 
	for i in range(1, 11):
		print(i)
		sys.stdout.flush()
		A[i - 1] = input()
		print(20 - i + 1)
		sys.stdout.flush()
		A[20 - i] = input()

	#For each chunk take only the max numbers before making a change
	for i in range(1, 6):
		print(i)
		sys.stdout.flush()
		C[i - 1] = input()
		print(i + 5)
		sys.stdout.flush()
		C[i + 5 - 1] = input()

	# getFirstPart
	a, c = getComparators(A, C, 5)
	if isEqual(a, c):
		for i in range(5): C[19 - i] = A[19 - i]
	elif isReversed(A, c):	
		for i in range(5): C[19 - i] = A[i]
	elif isNegated(a, c): 
		for i in range(5): C[19 - i] = '1' if A[19 - i] == '0' else '0'
	else: 
		for i in range(5): C[19 - i] = '1' if A[i] == '0' else '0'
	
	X = A[5:15]
	Y = C[5:]
	a, c = getComparators(X, Y, 5)
	# getSecondPart
	if isEqual(a, c):
		for i in range(5, 10): C[19 - i] = A[19 - i]
	elif isNegated(a, c): 
		for i in range(5, 10): C[19 - i] = '1' if A[19 - i] == '0' else '0'
	elif isReversed(X, c):	
		for i in range(5, 10): C[19 - i] = A[i]
	else:
		for i in range(5, 10): 
			C[19 - i] = '1' if A[i] == '0' else '0'
	print(''.join(C))
	sys.stdout.flush()

T, B = map(int, input().split())
for case in range(1, T + 1):
	if B == 10: case10()
	elif B == 20: case20()
	else:
		A, C = ['2']*100, ['2']*100
		needReversed, needComplemented, needBoth = False, False, False
		# Because of swap we have to take from out to in (1 - 20), (2 - 19), ..., (10 - 11) 
		for i in range(1, 51):
			print(str(i))
			sys.stdout.flush()
			A[i - 1] = input()
			print(str(100 - i + 1))
			sys.stdout.flush()
			A[100 - i] = input()
		for chunk in range(5):
			# Get the first not changing part
			for i in range(1 + chunk * 10, (chunk + 1) * 10 + 1):
				print(str(i))
				sys.stdout.flush()
				C[i - 1] = input()

			# if chunk != 0:
			# 	auxA, auxB  = getComparators(X, Y, 5)
			# 	for i in range(50):
			# 		if needReversed: C[99 - i], C[i] = C[i], C[99 - i]
			# 		elif needBoth: C[99 - i], C[i] = '1' if C[i] == '0' else '0', '1' if C[99 - i] == '0' else '0'
			# 		else: break
			# 	for i in range(100):
			# 		if needComplemented:  C[99 - i] = '1' if C[99 - i] == '0' else '0'
			# 		else: break

			X = A[chunk * 10:]
			Y = C[chunk * 10:]
			a, c = getComparators(X, Y, 2)
			if isEqual(a, c): pass
			elif isReversed(X, c):needReversed = True
			elif isNegated(a, c): needComplemented = True
			else: needBoth = True

			for i in range(chunk * 10, chunk * 10 + 5): 
				if needReversed: C[99 - i] = A[i]
				elif needComplemented:  C[99 - i] = '1' if A[99 - i] == '0' else '0'
				elif needBoth: C[99 - i] = '1' if A[i] == '0' else '0'
				else: C[99 - i] = A[99 - i]
			
			a, c = getComparators(X[5:], Y[5:], 2)
			if isEqual(a, c): pass
			elif isReversed(X[5: 100 - (chunk * 10 + 5)], c):needReversed = True
			elif isNegated(a, c): needComplemented = True
			else: needBoth = True
			
			for i in range(chunk * 10 + 5, chunk * 10 + 10): 
				if needReversed: C[99 - i] = A[i]
				elif needComplemented:  C[99 - i] = '1' if A[99 - i] == '0' else '0'
				elif needBoth: C[99 - i] = '1' if A[i] == '0' else '0'
				else: C[99 - i] = A[99 - i]

		print(''.join(C))
		sys.stdout.flush()

	res = input()
	if res == 'N': sys.exit(0)