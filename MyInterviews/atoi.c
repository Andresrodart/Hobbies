#include <stdio.h>
#include <assert.h>
#include <ctype.h>
// Incluir limits para checar que la cadena no desborde
#include <limits.h>
// Códigos de error
#include <errno.h>
// Para poder usar la funcion de exponencial
#include <math.h> 
// Para usar strlen
#include <string.h>

extern int errno;

/* Considere que para no romper la ejecución del programa solo muestro 
 los errores pero la ejecución continua, regresando 0 en caso de error  */
long long int my_atoi(const char *c){
    // Si la cadena esta vacía
	if(*c == '\0'){ 
		// Si no se puede representar como valor entero regresamos EINVAL, argumento invalido
		errno = EINVAL; perror("Not a interger value in string");
		return (0); 
	}

	long long int value = 0, digit;
    int sign = 1;

	/* Si el primer carcater es un guión se indica como negativo
	 No se consideran las prefijos "-"+, es decir si el usuario ingresa algo como "---6"
	 No regresamos +6 puesto que la funcion no deberia realizar cálculos matemáticos, solo cambiar el tipo de dato */
	if (*c == '-') sign = -1, c = c + 1;
	/* Sin embargo esta clase de comportamiento se aceptaría con el siguiente código comentado
	 while (*c == '-') sign *= -1, c = c + 1;*/
	
	if(*c == '\0'){
		errno = EINVAL; perror("Not a interger value in string");
		return (0); 
	}

	// Para deshacernos de los ceros a la izquierda
	while (*c == '0') c++;

	while(isdigit(*c)){
        // Creo la variable digito para poder usar el valor en la comprobación
		digit = (int) (*c-'0');
		// Si la variable ya es el maximo valor posible y sumado el siguiente digito 
		// causa "overflow" arrojamos error
		if(value == LONG_MAX || value + digit < 0 || value * 10 < 0){
			errno = ERANGE; perror("integer overflow");
			return (0);
		}
        value *= 10;
        value += digit;
		c++;
    }

	// Si no terminamos de leer la cadena es porque nos encontramos con un carcater no numérico
	if(*c != '\0'){
		errno = EINVAL; perror("Not a interger value in string");
		return (0); 
	}

	return (value * sign);
}

/* Para transformar cadenas en diferentes bases de binario hasta hexadecimal,
 Aunque en base 2 un numero negativo es complemento a dos,
 para fines prácticos será negativo si empieza con el carácter '-' 

 De igual forma cadenas como 0xAF4 no son válidas.
*/

long long int my_atoi_base(const char *c, unsigned int base){
	//Errores de argumentos
	if(base > 16){
		errno = EINVAL;
		perror("Base out of range");
		return (0); 
	}
	if(*c == '\0'){
		errno = EINVAL;
		perror("Not a interger value in string");
		return (0); 
	}

	long long int value = 0, digit, exponent = 0;
    int sign = 1;
	
	if (*c == '-') sign = -1, c = c + 1;
	
	if(*c == '\0'){
		errno = EINVAL;
		perror("Not a interger value in string");
		return (0); 
	}
	
	while (*c == '0') c++;

	// Buscamos el numero menos significativo iterando desde el ultimo caracater hacía atrás
    long long int head = strlen(c) - 1;
	const char * it = (c + head);
	
	while( head >= 0 && (isdigit(*it) || (*it >= 'A' && *it <= 'F') || (*it >= 'a' && *it <= 'f'))){
		// Si es hexadecimal tomamos el valor necesario
		if (*it >= 'A' && *it <= 'F')
			digit = (int) *it - 'A' + 10;
		else if(*it >= 'a' && *it <= 'f')
			digit = (int) *it - 'a' + 10;
		else
			digit = (int) (*it-'0');
		if(value == LONG_MAX || value + digit < 0 || value * 10 < 0){
			errno = ERANGE;
			perror("integer overflow");
			return (0);
		}
        value += digit * (long long int) pow(base, exponent);
        exponent += 1; head--; it = c + head;
    }

	// Si no terminamos de leer la cadena es porque nos encontramos con un carcater no numérico
	if( head >= 0 ){
		// imprimimos el error
		errno = EINVAL;
		perror("Not a interger value in string");
		// Si no se puede representar como valor entero regresamos EINVAL, 
		// argumento invalido
		return (0); 
	}
	return (value * sign);
}

int main(void){
    //Ejemplos de pruebas. Assert lo que hace es que marca como SUCCESS si la condición es verdadera
	//ERROR cuando la condición es falsa.

    assert(0 == my_atoi("-"));											// Cadena erronea -> Not a interger value in string: Invalid argument
    assert(0 == my_atoi(""));											// Cadena vacía -> Not a interger value in string: Invalid argument
    assert(0 == my_atoi("22sasdasd"));									// Cadena erronea -> Not a interger value in string: Invalid argument
    assert(73980709871235 == my_atoi("00073980709871235")); 			// Ceros a la izquierda
    assert(-1098273980709871235 == my_atoi("-1098273980709871235")); 	// Valor negativo
    assert(0 == my_atoi("-1098273980709871235-")); 						// Carácter no numérico -> Not a interger value in string: Invalid argument
    assert(0 == my_atoi("92233720368547758071"));  						// Overflow de enetero -> integer overflow: Result too large
    assert(122 == my_atoi_base("1111010", 2));  						// 122 en binario
    assert(43541 == my_atoi_base("Aa15", 16));  						// 43541 en hexadecimal
    assert(0 == my_atoi_base("AaG15", 16));  							// Cadena erronea -> Not a interger value in string: Invalid argument
    assert(-22927 == my_atoi_base("-00054617", 8));  					// -22927 en octal
    assert(0 == my_atoi_base("00054617", 17));  						// Base mayor a la hexadecimal -> Base out of range: Invalid argument
    puts("Finish.");
}