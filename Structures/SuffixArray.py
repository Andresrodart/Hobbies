class SuffixArray:
	"""
	Implementation of suffix array of O(nlgn)
	"""
	def __init__(self, string: str):
		self.string = string
		self.array = self.suffixArrayBuilder(self.string)
	 
	def suffixArrayBuilder(self, s: str) -> 'list(str)':
		s += '$'
		size = len(s)
		alphabet = 256
		
		# permutations, es el arreglo que mantiene los indices de incio de los sufijos, 
		# 	y en cada iteracíon se asegura que mantendrán el orden lexicográfico  
		# classes, es un arreglo auxiliar, que nos permite indicar el valor de orden
		# 	de cada sufijo, lo cuál nos permitira hacer comparacion en O(1)
		permutations, classes, cnt = [0] * size, [0] * size, [0] * max(size, alphabet)
		pn, cn = [0] * size, [0] * size
		
		
		# Aplicamos count sort, a las cadenas de tamaño 1
		
		for i in range(size): cnt[ord(s[i])] += 1
		for i in range(1, alphabet): cnt[i] += cnt[i - 1]
		for i in range(0, size): 
			cnt[ord(s[i])] -= 1
			permutations[cnt[ord(s[i])]] = i
		
		# Asignamos clases a cada cadena. 
		# Si la cadena es igual, tendrán la misma clase 
		
		classes[permutations[0]] = 0
		class_ = 1
		for i in range(1, size):
			if s[permutations[i]] != s[permutations[i - 1]]: class_ += 1
			classes[permutations[i]] = class_ - 1
		
		# Reorganizamos las permutaciones, cada vez con un tamaño el doble de grande
		#	Algoritmos de organización usan tiempos logaritmicos, pero como tenemos información previa de las cadenas de tamaño 2^(k-1), es decir las cadenas mas pequeñas
		#	podemos usar esta información, primero notemos que:
		#		* Permutations, contienen el indice donde empiezan las cadenas de tamaño 2^(k - 1), ordenadas
		#		* Las cadenas de tamaño 2^(k) esta compuesta de 2 cadenas 2^(k - 1), que ya están ordenas
		#			-> por lo tanto, las nuevas comparaciones pueden basarse con la segunda cadena primero
		#				i.e. c  = a + b; donde a = p[i] y b = p[i - 2 ^ (k - 1)]
		#		* La segunda cadena empieza en la posicion i - (1 << h)

		h = 0
		while (1 << h) < size:
			# Si la nueva cadena c = a + b, buscamos el indice de la cadena b de tamaño 2 ^ h
			for i in range(0, size):
				pn[i] = permutations[i] - (1 << h)
				# Como es cirular la busqueda de prefijso en la cadena, mandamos a positivo el indice
				if pn[i] < 0: pn[i] += size
			
			for i in range(class_ + 1): cnt[i] = 0
			
			# Aplicamos count sort, a las cadenas de tamaño 2 ^ h

			for i in range(size): cnt[classes[pn[i]]] += 1
			for i in range(1, class_): cnt[i] += cnt[i - 1]
			for i in range(size - 1, -1, -1): 
				cnt[classes[pn[i]]] -= 1
				permutations[cnt[classes[pn[i]]]] = pn[i]
			cn[permutations[0]] = 0
			class_ = 1
			for i in range(1, size):
				cur = (classes[permutations[i]], classes[(permutations[i] + (1 << h)) % size])
				prev = (classes[permutations[i - 1]], classes[(permutations[i - 1] + (1 << h)) % size])
				if cur != prev: class_ += 1
				cn[permutations[i]] = class_ - 1
			classes, cn = cn, classes
			h += 1
		permutations.pop(0)
		return permutations
	def __repr__(self):
		res = []
		for i in self.array: res.append(self.string[i:])
		return '\n'.join(res)

print(SuffixArray('aaba'))