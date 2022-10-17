def criba_eratostenes(n):
	multiplos = set()
	multiplos.update(range(i*i, n+1, i))