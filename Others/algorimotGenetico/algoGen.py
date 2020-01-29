import os
import json
import numpy
import math

class AlgoGen:
	def __init__(self, rules):
		self.rules = rules									#Reglas del algoritmo genético
		self.individuos = []								#Aqui guadaremos los vectores [representacion binaria, valor z, valor y, ...]
		self.biVectors = {}									#Aquí pondremos los bits que coresponden a cada variable en el orden en que viene en Rules
		self.resultado = None
		self.iterations = []
		self.__vecBit()										#Función para calcular el nuemro de bits de cada variable
		self.__individuos()									#Función para crear a los individuos
		self.algoritmo()
	
	def __vecBit(self):
		for i in self.rules['variables']:					#Para cada variable sacamos el numero de bits qeu necesitamos para representarlo en binario
			self.biVectors[i] = math.ceil( math.log((self.rules["rangos"][i][1] - self.rules["rangos"][i][0]) * 10**self.rules["bitPrecision"], 2) )			#ceil( log((b_j-a_j) * 10^n) / log(2))
			if self.biVectors[i] < 0: self.biVectors[i] = 1
	def __individuos(self):
		for i in range(self.rules["individuos"]):			#Para cada uno de los individuos
			variabls = {}									#Este diccionario nos ayuda para evaluar el valor de cada variable
			varVecAux = []									#Esta lista gurdara todo el vector binario [...x...,...y...,etc]
			accpetavleVar = True							#Esta varibale nos ayuda a seguir buscando individuos que cumplan las condiciones
			for j in self.rules["variables"]:				#Por cada variable
				vecInDec = int(numpy.random.random() * 2**self.biVectors[j])	#Valor de la parte binaria e.g. 1 (1)
				longVec = '0' + str(self.biVectors[j]) + 'b'			#Logitud que tendra nuentro número binario e.g. 2 (2)
				varVecAux += list(format(vecInDec,  longVec))			#Guardamos la parte de la primera incognita e.g. de (1) y (2) [0,1]
				variabls[j] = self.rules["rangos"][j][0] + (vecInDec*(self.rules["rangos"][j][1]-self.rules["rangos"][j][0]))/(2**self.biVectors[j] - 1) #Calculamos el valor de la varible e.g. x = a_j + dec[01]*((b_j-a_j)/2^mj - 1)
			for strs in self.rules["condiciones"]:			#Evaluamos si nuestras variables cumplen con las condiciones
				accpetavleVar = accpetavleVar and eval(strs, variabls)
			#print('Buscando valores que se acepten')
			while not accpetavleVar:						#Si no cumple volvemos a hacer lo mismo hasat qeu cumplan todas las condiciones 
				variabls = {}
				varVecAux = []
				accpetavleVar = True
				for j in self.rules["variables"]:			#Por cada variable
					vecInDec = int(numpy.random.random() * 2**self.biVectors[j])	#Valor de la parte binaria e.g. 1 (1)
					longVec = '0' + str(self.biVectors[j]) + 'b'			#Logitud que tendra nuentro número binario e.g. 2 (2)
					varVecAux += list(format(vecInDec,  longVec))			#Guardamos la aprte de la primera incognita e.g. de (1) y (2) [0,1]
					variabls[j] = self.rules["rangos"][j][0] + (vecInDec*(self.rules["rangos"][j][1]-self.rules["rangos"][j][0]))/(2**self.biVectors[j] - 1) #Calculamos el valor de la varible e.g. x = a_j + dec[01]*((b_j-a_j)/2^mj - 1)
				for strs in self.rules["condiciones"]:		#Evaluamos si nuestras variables cumplen con las condiciones
					accpetavleVar = accpetavleVar and eval(strs, variabls)
			tempVars = {}
			#print('Encontrados valores que se acepten')
			for x in self.rules["variables"]:				#Al usar la funcion eval nuestro duccionario se llena de basura por lo que extraeremos solo los valores de las variables
				tempVars[x] = variabls[x]
			self.individuos.append([varVecAux, tempVars])	#Agregamos los valores que entraron [Vector, variables y valores, id vector]
	
	
	def algoritmo(self, indi=None, pobls=None, bitPres=None):				#Podemos recalcular el mejor valor con nuevos individuos, o mas poblaciones o con otro bit de presicion
		self.rules["poblaciones"] = pobls if pobls else self.rules["poblaciones"]
		if bitPres:
			self.rules["bitPrecision"] = bitPres
			self.__vecBit()
		if indi:
			self.rules["individuos"] = indi
			self.__individuos()
		
		for i in range(self.rules["poblaciones"]):
			indiFrts = {}											#Aquí guardaremos los id de los invividuos que salgan despues de elegir el numero aleaotrio
			resultFO = 0											#La última posición guarda la suma de todas las evaluaciones en F.O.
			numOfCol = len(self.rules["variables"]) + 6
			iteration = [[None]*numOfCol for each in range(self.rules["individuos"] + 1)]
			iteration[0][0] = 'Vector'
			iteration[0][numOfCol - 5] = 'Z'
			iteration[0][numOfCol - 4] = '%Z'
			iteration[0][numOfCol - 3] = '%Z acm'
			iteration[0][numOfCol - 2] = 'Num Ale'
			iteration[0][numOfCol - 1] = 'V Fuerte'
			
			for i, value in zip(range(numOfCol - 6),self.rules["variables"]):
				iteration[0][i + 1] = value
		
			for j in range(len(self.individuos)):					#Cramos Z acumulado y agregamos los i ndividuos
				varHelp = self.individuos[j][1].copy()				#Auxiliar para evaluar en la F.O.
				iteration[j + 1][numOfCol - 5] = eval(self.rules['FO'], None, varHelp)	#Evaluamos al individuo en F.O.
				resultFO += iteration[j + 1][numOfCol - 5]			#Z acumulado
				iteration[j + 1][0] = ''.join(self.individuos[j][0])
				for k, val in zip(range(len(self.rules["variables"])), self.rules["variables"]):
					iteration[j + 1][k + 1] = self.individuos[j][1][val]
			iteration[1][numOfCol - 4] = iteration[1][numOfCol - 5]/resultFO			#Z% = resZ_j / Zacumulado
			iteration[1][numOfCol - 3] = iteration[1][numOfCol - 4]						#Z% acumulado	
			for j in range(1, len(self.individuos)):
				iteration[j + 1][numOfCol - 4] = iteration[j + 1][numOfCol - 5]/resultFO						#Z% = resZ_j / Zacumulado
				iteration[j + 1][numOfCol - 3] = iteration[j + 1][numOfCol - 4]	+ iteration[j][numOfCol - 3]	#Z% acumulado
			
			for j in range(len(self.individuos)):					#Buscamos los individuos mas fuertes
				iteration[j + 1][numOfCol - 2] = numpy.random.random()
				for k in range(len(self.individuos)):				#Buscamos en cual de los rangos entra la variable
					if iteration[j + 1][numOfCol - 2] <= iteration[k + 1][numOfCol - 3]:
						if k not in indiFrts:						#Guardamos los vectores que han sido seleccinados
							indiFrts[k] = 1							#Guardamos las veces que han aparecido para ver cual es el mas fuerte
						else:
							indiFrts[k] += 1
						iteration[j + 1][numOfCol - 1] = ''.join(self.individuos[k][0])
						break

			individuosAux = []										#Auxiliar para crear a la nueva población
			auxStronger = [0, 0]									#Auxiliar para buscar al individuo mas fuerte
			
			for j in indiFrts:											
				individuosAux.append(self.individuos[int(j)])		#Copiamos al individuo que si pasó
				if indiFrts[j] > auxStronger[1]:					#Vemos si el individuo mas fuerte ya apareció
					auxStronger[0] = j
					auxStronger[1] = indiFrts[j]

			for j in range(len(self.individuos) - len(indiFrts)):	#Rellenamos los espacio faltantes con mutaciones del individio
				variabls = {}										#Auxiliar para verificar qeu cumpla las condiciones
				newVect = self.individuos[auxStronger[0]][0][:]		#Copiamos el vector mas fuerte
				indexToChange = numpy.random.randint(0, len(newVect) - 1)			#Seleccionamos un indice al azar para mutar
				newVect[indexToChange] = '0' if newVect[indexToChange] == '1' else '1'	#Si es uno se hace 0 si es 0 se hace uno
				startIndex = 0										#Esta variable nos ayuda a obtener el valor de nuestra variable que esta revuleto en la lista
				accpetavleVar = True
				for each in self.rules["variables"]:				#Calculamos los nuevos valores de cada variable
					currentVec = newVect[ startIndex : (startIndex + self.biVectors[each]) ]	#Nuestra variable va desde el indice qeu empiza hasta el ultimo bit que lo representa
					variabls[each] = self.rules["rangos"][each][0] + (int(''.join(currentVec), 2)*(self.rules["rangos"][each][1]-self.rules["rangos"][each][0])) / (2**self.biVectors[each] - 1)
				for strs in self.rules["condiciones"]:				#Evaluamos si nuestras variables cumplen con las condiciones
					accpetavleVar = accpetavleVar and eval(strs, None, variabls)
				#print('Buscando valores que se acepten')
				while not accpetavleVar:
					variabls = {}									#Auxiliar para verificar qeu cumpla las condiciones
					newVect = self.individuos[auxStronger[0]][0][:]	#Copiamos el vector mas fuerte
					indexToChange = numpy.random.randint(0, len(newVect) - 1)	#Seleccionamos un indice al azar para mutar
					newVect[indexToChange] = '0' if newVect[indexToChange] == '1' else '1'	#Si es uno se hace 0 si es 0 se hace uno
					startIndex = 0									#Esta variable nos ayuda a obtener el valor de nuestra variable que esta revuleto en la lista
					accpetavleVar = True
					for each in self.rules["variables"]:			#Calculamos los nuevos valores de cada variable
						currentVec = newVect[ startIndex : (startIndex + self.biVectors[each]) ]	#Nuestra variable va desde el indice qeu empiza hasta el ultimo bit que lo representa
						variabls[each] = self.rules["rangos"][each][0] + math.floor(int(''.join(currentVec), 2)*(self.rules["rangos"][each][1]-self.rules["rangos"][each][0])) / (2**self.biVectors[each] - 1)
						startIndex = startIndex + self.biVectors[each]
					for strs in self.rules["condiciones"]:			#Evaluamos si nuestras variables cumplen con las condiciones
						accpetavleVar = accpetavleVar and eval(strs, None, variabls)
				#print('Encontrados valores que se acepten')
				tempVars = {}
				for x in self.rules["variables"]:					#Al usar la funcion eval nuestro duccionario se llena de basura por lo que extraeremos solo los valores de las variables
					tempVars[x] = variabls[x]
				individuosAux.append([newVect, tempVars])			#Agregamos los valores que entraron [Vector, variables y valores, id vector]
			
			self.individuos = individuosAux
			self.iterations.append(iteration[:])
			furt = iteration[1]
			auxRes = {}
			for j in iteration[1:]:	
				if float(j[numOfCol - 5]) > float(furt[numOfCol - 5]):			#Vemos si el individuo mas fuerte ya apareció
					furt = j
			
			for each, val in zip(iteration[0], furt[:numOfCol - 5]):
				auxRes[each] = val
			self.resultado = auxRes
