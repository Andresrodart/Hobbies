;ProgramaParaTablasDeMultiplicar
;Tabla de syscall: https://filippo.io/linux-syscall-table/
;Contador de bytes para cadenas: https://lingojam.com/ByteCounter
;Funciones en NASM: https://www.cs.virginia.edu/~evans/cs216/guides/x86.html
;nasm -felf64 Tablamultiplicar.asm && ld Tablamultiplicar.o && ./a.out
;https://cs.lmu.edu/~ray/notes/nasmtutorial/

			section 		.data                                           		;The data section is used for declaring initialized data or constants
			CadPideNum 		db		"De que numero quiere ver la tabla?: "		;dEFINDING dATA Guardamos la cadena en la varaible	
			Resultado		db		"Resultado: "					;Variable que gaurda la cadena Resultado
			SaltoLinea		db		13,10,'$'						;Para hacer el salto de linea necesitamos dos bytes uno para /r y otro para /n
			
			section			.bss 									;The bss section is used for declaring variables.
			Numero			resb	1								;Reserba 4 bytes a Numero 1 para el numero y lso tros para que alamcene ambiél el caracater de escape (enter)								
			
			section			.text									;The text section is used for keeping the actual code.
			global _start

_start:			call 		_ImpPedNum									;Llamamos a la subrutina _ImpPedNum "imprimir pedir numero"
			call 		_ObtenrNum									;Llamamos a la subrutina _ObtenrNum "Obtener numero" que se guardara en la variable Numero
			call 		_ImpTituRs									;Imprimimos la palabra resulrado
			call 		_ImpSaltoL									;Llamamos a al subrutina auxiliar para imprimir lo que metió el suaurio <-Esta nos ayudará a imprimir, meteremos a Numero lo que queramos imprimir
			mov 		r13, [Numero]									;Ponemos en el r13 lo que hay en memoria en la varibale Numero, la cual se lleno anyeriormente, notese que para acceder a lo que guarda ponemos numero entre corchetes
			sub 		r13, '0'									;Pasamos del valor ascci al valor nuemrico
			mov		r15, 0										;Usaremos R15 como el contador para or de 1 a 10
			call		_TabDeMult									;Subrutina para sacar la tabla
			mov 		rax, 60										;Al registro 0 (rax) le guardamos 60 el cual es el código para la la salida del porgrama sys_exit
			mov 		rdi, 0										;sys_exit solo recive un parametro, si es '0' quiere decir que todo se ejecuto bien
			syscall												;llamamos a la función del sistema para que se ejecute

_TabDeMult:		add 		r15, 1										;En r15 vamos aumentando de 1 en 1
			mov		r14, r15									;R14 nos ayudará para guardar la multiĺicaion le pasmo el valor de r15 que sera el valor por el cualmultiplicaremos
			imul		r14, r13									;Multiplicamos r14 por r13 que es el nuemro que se nos pidio
			mov		r8, r14										;Guardamos en r8 lo que queremos imprimir, en este caso guardamos lo que hay en r14
			call		_getDec										;Obtenemos las partes decimales y unidades coon esta subrutina									
			cmp		r15, 9										;Comparamos si r15 es menor o igual a 9, si es así volveremos a irerar, el resultado de esta operacion se va directo a la siguiente isntrucción									
			jle 		_TabDeMult									;JLE JumpLessEqual slata a donde estela etiqueta si se cumple que la operacion anterior es menor o igual
			ret
					
_ImpPedNum:		mov 		rax, 1										;rax es un registro especial que al momento de llamar a syscall leerá su contenido y ejecutará la función con el codigo que tenga (1 queire decir que imprimiremos en pantalla)
			mov 		rdi, 1										;rdi es usado como el valor del primer argumento de la función
			mov 		rsi, CadPideNum									;rsi es usado como el valor del segundo argumento de la función
			mov 		rdx, 36										;rdx es usado como el valor del tercer argumento de la función
			syscall												;ya que tenemos todo lo necesario mandamos a llamar a la función en este caso queremos llamar a la función write del sistema para que imprima en pantalla el mensaje
			ret												;con ret 'retrocedemos' a la rutina que mandó a llamar a esta subrutina, en este caso la sigueinte isntrucción en ejecutarse sería la de la linea

_ObtenrNum:		mov 		rax, 0										;rax ahora vale 0 porquemandaremos a llamara a la función del sistema 0, la que sirve para leer de consola
			mov 		rdi, 0
			mov 		rsi, Numero
			mov 		rdx, 1
			syscall
			ret

_ImpTituRs:		mov		rax, 1
			mov 		rdi, 1
			mov 		rsi, Resultado
			mov 		rdx, 11
			syscall
			ret

_ImpNumUsu:		mov 		rax, 1
			mov 		rdi, 1
			mov 		rsi, Numero
			mov 		rdx, 1
			syscall
			ret
			
_ImpSaltoL:		mov 		rax, 1
			mov 		rdi, 1
			mov 		rsi, SaltoLinea
			mov 		rdx, 2
			syscall
			ret

_getDec:		mov 		edx, 0										;Para sacar el decimal tenemos que dividir por 10, edx es la parte alta del nuemro a dividir
			mov 		eax, r8d									;eax es la parte baja del nuemro a dividir Es decir el nuemro esta escho de adx y aex para formar un nuermo de 64 bits, r8d es son los primero 32 bits de r8, lo que nos importa
			mov		r10d, 10									;e9d será nuestro divisor
			idiv		r10d										;esto es r8/10
			mov		r8d, eax									;en eax se guardó el resultado de la división y es lo que nos interesa, el valor decimal
			mov		r9d, edx									;en edx se guardó el residuo, o sea a las unidades
			add		r8, '0'										;Lo regresamos a valor ascci para imprimirlo
			add		r9, '0'										;Ascci de las unidades
			mov 		[Numero], r8									;Para imprimir pasamos a la variable nuemro lo que que hay en r8 que son las decenas
			call 		_ImpNumUsu									;Llamamos a al subrutina auxiliar para imprimir			
			mov 		[Numero], r9									;Ahora guardamos las unidades
			call 		_ImpNumUsu									;Llamamos a al subrutina auxiliar para imprimir lo que metió el suaurio			
			call 		_ImpSaltoL									;Imprimimos un salto de linea
			mov		r8, 0
			ret	


;Una función del sistema es una función queimplementa el sistema operativo para hacer rutinas usuales como imprimir en pantalla o leer del perifericos

;int 0x80 es equivalente a syscall

;sys_read (rxa=0, arguemno1, arguemnto2, arguemnto3) =  ssize_t read(int fd, void *buf, size_t count);
	;El primer arguemnto es el descriptor de archivos. Puede ser 0, 1 y 2 para una entrada estandar, para una salida estandar y para un error estandard respectivamente
	;El segundo argumento es un buffer que sirve para alamcenar o leer lo entrada o salida
	;El tercer argumento es un contador que especifica el numwro de bytes a leer o escribir 	

;sys_write (rxa=1, arguemno1, arguemnto2, arguemnto3)
	;El primer arguemnto es el descriptor de archivos. Puede ser 0, 1 y 2 para una entrada estandar, para una salida estandar y para un error estandard respectivamente
	;El segundo argumento es un buffer que sirve para alamcenar o leer lo entrada o salida
	;El tercer argumento es un contador que especifica el numwro de bytes a leer o escribir 
