T = int(input())
for case in range(1, T + 1):
	N = int(input())
	activities, res, aux = [], [], []
	cameron, james = 0, 0
	for i in range(N):
		numbers = list(map(int, input().split()))
		activities.append(tuple((*numbers, i)))
	activities.sort(key=lambda tup: tup[0])
	for activity in activities:
		if activity[0] >= cameron: 
			aux.append(('C', activity[2]))
			cameron = activity[1]
		elif activity[0] >= james: 
			aux.append(('J', activity[2]))
			james = activity[1]
		else:
			res = list('IMPOSSIBLE')
			break

	if len(res) == 0:
		aux.sort(key=lambda tup: tup[1])
		for item in aux: res.append(item[0])

	print('Case #{}: {}'.format(case, ''.join(res)))