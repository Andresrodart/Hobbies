; This program inputs a string from the keyboard and 
; redisplays it on the screen. Demonstrates DOS 
; functions 0Ah and 9. 1 0 1 0 1 1
;  1 1 0 1 0 1
.model small
.stack 100h
.data
stringSize   db  80            ; tamano de la cadena de entrada
keysTyped    db  ?             ; numeros de caracteres
inputString  db  80 dup(0)     ; vector para guardar caracteres
vec_binario  db  80 dup(7)     ; vector para en binario
crlf         db  0Dh,0Ah,"$"   ; cadena de salto de linea
ES_BINARIO   db "Binario: ", "$"
ES_DECIMAL   db "Decimal: ", "$"
numero_decimal dw 0
aux          db 0
d1 dw 655 
.code
main proc
    mov   ax, @data             ; pasamos al registro ax la referencia del grupo data
    mov   ds, ax                ; (contiene la dirección del segmento de memoria en el cual se almacenan los datos introducidos.)ahora damos de alta todo el grupo .data pasando la referencia al registro DataSegment
    call ingresar_numero
    call _atoi
    call binario
    call hexadecimal
; The string contains a carriage return, but we 
; need to insert an additional linefeed character so 
; it can be displayed correctly.  
    call salto_de_linea
    lea dx, ES_DECIMAL     ; imprimimos la cadena Bianrio: 
    mov ah, 09H 
    int 21H
    mov   ax,0
    mov   al,keysTyped
    mov   si,ax
    mov   inputString[si + 1],0Ah  ; linefeed character
; Echo the string to the console.
    mov   ah,9                   ; output $-terminated string
    mov   dx,offset inputString
    int   21h
    mov   ax,4C00h               ; end program
    int   21h
main endp

ingresar_numero proc
    mov   ah, 0Ah               ; (preparamos lectura de linea) interrupcion del tipo buffer, a diferencia del 01h lee mas de un caracter hasta el retorno 
    mov   dx, offset stringSize ; (contiene la dirección del offset de la zona de memoria del segmento anterior en la que se almacenanlos datos.)
    int   21h                   ; llamada a interrupcion
    call salto_de_linea
    ret
ingresar_numero endp

_atoi proc
    mov ax, 0                   ; inicializamos el ergistro con el valor 0
    mov al, keysTyped           ; el tope del ultimo caracter
    mov si, ax                  ; lo pasamos al registro de iterador, i = len(strinput)
    xor ax, ax                  ; ax = 0
    mov al, inputString[si - 1] ; obtenemos el utlimo caracter leido
    sub ax, 48                   ; al codigo ascci le restamo 48 '0' - 48 es 0
    add numero_decimal, ax       ; agregamos el numero a nuestra variable
    mov bx, 10                   ; el contador de unidades, empezando en decenas
    dec si                       ; movemo el indice i--
    cmp si, 1                    ; comparamos con 1
    jl _end                      ; si es menor a 1 ya leimos todos los carcateres
    next:
        mov ax, 0                   ; limpiamos el registro ax para multiplicar
        mov al, inputString[si - 1] ; obtenemos el siguiente caracter en la parte baja de ax
        sub al, 48d                 ; al codigo ascci le restamo 48 '0' - 48 es 0
        ; ax = ax * bx
        mul bx                      ; multiplicamos por su unidad correspondiente
        add numero_decimal, ax      ; agregamos el numero
        mov cx, 10                  ; auxiliar para aumnetar decimal
        mov ax, bx                  ; para la multipliacion pasamos bx a ax
        mul cx                      ; aumentamos la unidad (ax = ax * cx => ax = bx * 10)
        mov bx, ax                  ; regresamos el valor al contador de unidad
        dec si                      ; i --
        cmp si, 1
        jge next                    ; mientras no sea 0 continuamos
    _end:
        ; debug para saber si si se guardaba bien el numero
        ; mov ax, numero_decimal
        ; call PRINT
        ret
_atoi endp

binario proc
	mov bx, 2               ; nuestro divisor
	mov si, 0               ; i = 0
    mov ax, numero_decimal  ; nustro dividendo
	continue_:
        mov dx, 0           ; limpiamos la parte alta del divisor
		div bx              ; ax / bx = numero_decimal / 2
        mov vec_binario[si], dl ; guardamos el residuo
		inc si              ; i ++
		cmp ax, 1           ; mientras el dividendo no sea 0
		jge continue_
    lea dx, ES_BINARIO      ; imprimimos la cadena Bianrio: 
    mov ah, 09H 
    int 21H  
	imprime_bin:
		mov dx, 0                   ; limpiamos dx
		mov ah, 2h                  ; imprimir caracter
		mov dl, vec_binario[si - 1] ; dl es el caractar a impirmi, tomamos de atras a adelante
                                    ; es si - 1 porque en el loop de arriba i quedo una psocion por delnte del final
		add dl, 48d                 ; obtenrmos el valor ascci del nuemro a imprimir
		int 21h                     ; llamada a interrupcion
		dec si                      ; i --
		cmp si, 1                   ; misntras i no sea 0
		jge imprime_bin
    ret
binario endp
hexadecimal proc
    ret
hexadecimal endp
salto_de_linea proc
    mov   ah,9                  ; llamada para imprimir cadena
    mov   dx,offset crlf        ; preparamo la cadena de salto de linea
    int   21h                   ; llamada a interrupcion
    ret 
salto_de_linea endp
PRINT PROC            
      
    ;initilize count 
    mov cx,0 
    mov dx,0 
    label1: 
        ; if ax is zero 
        cmp ax,0 
        je print1       
          
        ;initilize bx to 10 
        mov bx,10         
          
        ; extract the last digit 
        div bx                   
          
        ;push it in the stack 
        push dx               
          
        ;increment the count 
        inc cx               
          
        ;set dx to 0  
        xor dx,dx 
        jmp label1 
    print1: 
        ;check if count  
        ;is greater than zero 
        cmp cx,0 
        je exit
          
        ;pop the top of stack 
        pop dx 
          
        ;add 48 so that it  
        ;represents the ASCII 
        ;value of digits 
        add dx,48 
          
        ;interuppt to print a 
        ;character 
        mov ah,02h 
        int 21h 
          
        ;decrease the count 
        dec cx 
        jmp print1 
exit: 
ret 
PRINT ENDP 
end  main
