import math

def Divisors(n): 
	i = 1
	res = 0
	while i <= math.sqrt(n):       
		if n % i == 0 :
			if (n / i == i) : res += 1 
			else : res += 2 
		i += 1
	return res

t = int(input())
while t:
	n = int(input())
	res = Divisors(n)
	if res % 2 == 0: print(0)
	else: print(1)
	t -=1