import math
def simpson(r, m, a, b, n):
	dx = (b-a)/n
	sum1 = f(a + dx/2, r, m)
	sum2 = 0;
	for i in range(1, n):
		sum1 += f1(a + dx*i + dx/2, r, m)
		sum2 += f1(a + dx*i, r, m)
	return (dx/6) * (f1(a, r, m) + f1(b, r, m) + 4*sum1 + 2*sum2)

def f1(x, r, m):
	return ( math.exp(-.5 * Math.pow( (x-m) / r, 2)) / (r * math.sqrt(math.pi * 2)) )

r = float(input()) #Lo que meta el usaurio Creo que esta es sigma
m = float(input()) #Lo que meta el usaurio Creo que esta es miu8
a = float(input()) #Lo que meta el usaurio Esta es limite inferiro
b = float(input()) #Lo que meta el usaurio Esta es limite superios
n = float(input()) #Lo que meta el usaurio Este el nuemro de iteraciones

print(simpson(f1, r, m, a, b , n));

