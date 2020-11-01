from typing import List
import sys
import math  
import bisect				# Para hacer inserciones ordenadas en tiempo logaritmico
import typing				# Para anotaciones de funciones

# El algoritmo esta basado en la busqueda binaria
# Como T debe estar completa para que se cumpla que S = T * K
# Tenemos dos observaciones, la primera es que Para cualquier solucion A
# A debe estar al menos en los primeros len(A) caracteres de S
# La segunda es que K existe en el domninio de todos los divisores de la longitud de S, pares o impares (pero no mezclados)
# Ahora para agilizar la busqueda sabemos que si un divisor k es solicion, tambien puede serlo un divisor mas pequeno
# caso contrario debe ser un divisor mas grande, cumpliendo con la propiedad de ser monotonicamente creciente
# 
# Eg:
# abcabcabc -> divisores [1, 3, 9]
# el divisor en medio del dominio es 3, la cadena abc cumple con poder ser repetida 3 veces para formar S
# Ahora nuestro dominio de busqueda se reduce a [1, 3], la parte entera de posicion (0 + 1) / 2 es 0, 
# pero como 1 no es solucion el rango queda solo en [3], siendo T = abc 


# Funcion auxiliar para obtener todos los divisores de la longitud de S
# O(sqrt(s)*log(d))
def getDivisors(n: int) -> List[int]: 
	i = 1	# contador
	divisors_pair = [] 	# contendor para divisores pares
	divisors_odd = []	# contendor para divisores impares
	while i <= math.sqrt(n): 	  
		if n % i == 0: 
			if n / i == i:
				bisect.insort(divisors_pair if i % 2 == 0 else divisors_odd, i)
			else: 
				bisect.insort(divisors_pair if i % 2 == 0 else divisors_odd, i)
				bisect.insort(divisors_pair if (n // i) % 2 == 0 else divisors_odd, n // i)
		i = i + 1
	return divisors_pair, divisors_odd

# Funcion auxiliar para saber si una ventana es solucion
# O(s)
def windowCheck(S: str, subS: int) -> bool:
	for i in range(0, len(S), subS): # checamos todas las subcadenas de tamano subS sean iguales
		for j in range(subS):
			if S[j] != S[i + j]: return False
	return True

# Busqueda binaria
# O(log(d) * s)
def binarySearch(domain: List[int], S:str) -> int:
	if not domain: return sys.maxsize
	l, r = 0, len(domain) - 1		# rango derecho e izquierdo por sus iniciales en ingles
	while l < r: 
		mid = (l + r) // 2
		divisor = domain[mid]
		if windowCheck(S, divisor): r = mid
		else: l = mid + 1
	return domain[r] if windowCheck(S, domain[r]) else sys.maxsize

# Funcion para encontrar la cadena mas pequena T
# O(sqrt(s) * log(d) + log(d) * s ) -> O(log(d) * (s + sqrt(s))) -> O(s*log(d))
# donde d es el numero de divisores y s es el tamano de la cadena S
def smallestString(S: str) -> str:
	if len(S) == 0: return S
	# Usaremos busqueda binaria para encontrar la cadena mas pequena
	# El dominio son todas las cadenas que podemos formar, esto es con
	# todos los numeros en los que podemos dividirlo
	pair, odd = getDivisors(len(S))
	res = min(binarySearch(pair, S), binarySearch(odd, S))
	return S[:res] if windowCheck(S, res) else S

if __name__ == "__main__":
	print(smallestString(sys.argv[1]))