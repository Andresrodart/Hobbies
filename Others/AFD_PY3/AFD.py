#El json qeu cargasmo es un archivo que nos permite guardar las reglas de la tupla
#Esta en orden Q siendo los estados, etc.
#d representa la delta que es la función de trnasición, en ella ponemos un diccionario (que en escencia funciona como una tabla hash)
#	Así la primera linea es para el estado uno, la seguda para el dos etc,

import json

class Estado:																									#La clase Estado nos permite crear un nuevo estado 
	def __init__(self, delta, isFinal):
		self.delta = delta																						#Aquí guardaremos la tabla de transiciones
		self.isFinal = isFinal																					#Determianmos si es o no un estado final

class AFD:																										#Este será nuestro automata
	def __init__(self, rules):
		self.Estados = []
		self.Estadoinicial = rules["Q_0"] - 1
		self.Alfabeto = rules["Z"]
		for i in range(rules["Q"]):																				#Al inicializarlo vamos a crear un estado segun el numero de estados cargado del archivo
			self.Estados.append(Estado(rules["d"][i], 'Pertenece' if i + 1 in rules["F"]  else 'No pertenece'))	#Le mandamos su función de transición y con el operador ternario le mandamos true si es estado final y false si no lo es

	def isSGood(self, strin):																					#Función que nos permite saber si una cadena pertenece al 
		auxEstado = self.Estadoinicial																			#Auxiliar para movernos en entre los estados
		for item in strin:																						#Leemos cada caracter de la cadena
			if item in self.Alfabeto:
				auxEstado = self.Estados[auxEstado].delta[item]	- 1												#El estado en que estamos va a cambiar depemndiendo de la regal que tienen el estado en que estamos, con self estados recuperamos el estado en que estamos y con su propiedad del ta le amndamos el carcarter para ver a qeu estado nos manda -1 porque usaremos su indice
			else:
				return 'Existe un caracter que no pertenece al alfabeto'										#Regremos eso si la cadena contiene un caracter que no esta en el alfabeto
		return 	self.Estados[auxEstado].isFinal																	#Regreamos si es estado final o no

if __name__ == '__main__':
	tests = {}
	rules = {}
	resul = {}
	ourAFD = None
	with open('./Tests.json', 'r') as inputFile:												#Abrimos el archivos de pruebas
		tests = json.load(inputFile)															#Con esta linea cargamos las pruebas en la varibale rules
	with open('./AFD.json', 'r') as inputFile:													#Abrimos el archivos de reglas
		rules = json.load(inputFile)															#Con esta linea cargamos las reglas en la varibale rules
	
	ourAFD = AFD(rules)
	for item in tests["pruebas"]:
		resul[item] = ourAFD.isSGood(item)
	
	with open('resultados.json', 'w') as outFile:  												#Escribimos la respuesta en un archivo
		json.dump(resul, outFile, indent=4)