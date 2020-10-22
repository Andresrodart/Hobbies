t =  int(input())
while t:
	n, b = map(int, input().rstrip().split())
	a = list(input().rstrip().split())
	countWalls = time = 0
	for tye in a:
		if tye == '#': countWalls += 1
	for i in range(len(a)):
		tye = a[i]
		if tye == '0': time += 1
		elif tye == '#': 
			if countWalls <= b: time += 1
			elif a[i + 1] == '0': time += 2
			elif b <= 0: 
				time = 'Impossible'
				break
			b -= 1
	print(time)