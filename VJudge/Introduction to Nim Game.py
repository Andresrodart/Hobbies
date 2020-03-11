
def nimGame(pile):
	res = 0
	for rocks in pile:
		res ^= rocks
	return 'Second' if res == 0 else 'First'

g = int(input())
for g_itr in range(g):
	n = int(input())
	pile = list(map(int, input().rstrip().split()))
	print(nimGame(pile))