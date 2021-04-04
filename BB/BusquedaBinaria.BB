/*  Definimos la función
		Recibimos una lista de enteros y el entero que queremos buscar en la lista
		Regresamos el indice donde se encuentra el objetivo o -1 en caso de no encontrarlo
*/
/*Definimos las varibles que necesitaremos*/
/*Definimos un ciclo que se cumpla miestra puntoMenor sea menor a puntoMayor*/
/*Calculamos el punto medio*/
/*Determinamos si el punto medio es el objetivo*/
/*Regresamos el indice donde se encuentra*/
/*Preguntamos si puntomedio es mayor al objetivo*/
/*Movemos el puntoFinal*/
/*Si puntoMedio es menor*/
entero busquedaBinaria(lista<entero> arreglo, entero objetivo):
	entero puntoMenor
	entero puntoMedio
	entero puntoFinal
	mientras puntoMenor < puntoFinal:
		puntoMedio = (puntoFinal + puntoMenor) / 2
		si arreglo[puntoMedio] == objetivo: 
			regresa puntoMedio
		o si arreglo[puntoMedio] > objetivo:
			puntoFinal = puntoMedio - 1
		sino:
			puntoMenor = puntoMedio + 1