cases = int(input())
for _ in range(cases):
	wins = 0
	palaces = int(input())
	for _cord in range(palaces):
		row, col = map(int, input().split())
		if row % 2 == 0 and col % 2 != 0: wins += 1
		elif row % 2 != 0 and col % 2 == 0: wins += 1
	print('Ada' if wins % 2 != 0 else 'Vinit')