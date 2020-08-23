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
vec_binario  db  80 dup(0)     ; vector para en binario
crlf         db  0Dh,0Ah,"$"   ; cadena de salto de linea
numero_decimal dw 0
aux          db 0
.code
main proc
    mov   ax, @data             ; pasamos al registro ax la referencia del grupo data
    mov   ds, ax                ; (contiene la dirección del segmento de memoria en el cual se almacenan los datos introducidos.)ahora damos de alta todo el grupo .data pasando la referencia al registro DataSegment
    call ingresar_numero
    call _atoi
    call binario
    call salto_de_linea
; The string contains a carriage return, but we 
; need to insert an additional linefeed character so 
; it can be displayed correctly.  
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
    ; ax = ah + al
    mov ax, 0
    mov al, keysTyped
    mov si, ax
    mov ax, 0
    mov al, inputString[si - 1]
    sub al, 48d                  ; al codigo ascci le restamo 48 '0' - 48 es 0
    add numero_decimal, ax       ; agregamos el numero
    mov bx, 10d                  ; el contador de unidades, empzando en decenas
    dec si
    cmp si, 1
    jl _end
    next:
        mov ax, 0                   ; limpiamos el registro ax para multiplicar
        mov al, inputString[si - 1] ; obtenemos el siguiente caracter en la parte baja de ax
        sub al, 48d                  ; al codigo ascci le restamo 48 '0' - 48 es 0
        ; ax = ax * bx
        mul bx                      ; multiplicamos por su unidad correspondiente
        add numero_decimal, ax      ; agregamos el numero
        mov cx, 10                  ; auxiliar para aumnetar decimal
        mov ax, bx                  ; para la multipliacion pasamos bx a ax
        mul cx                      ; aumentamos la unidad (ax = ax * cx => ax = bx * 10)
        mov bx, ax                  ; regresamos el valor al contador de unidad
        dec si
        cmp si, 1
        jge next
    _end:
        ret
_atoi endp
binario proc
	mov bx, 2d
	mov si, 0
	mov ax, numero_decimal
	continue_:
		div bx
		mov vec_binario[si], ah
		mov ah, 0
		inc si
		cmp al, 1
		jge continue_
	imprime_bin:
		mov dx, 0
		mov ah, 2h                  ; imprimir caracter
		mov dl, vec_binario[si - 1]
		add dl, 48d
		int 21h
		dec si
		cmp si, 1
		jge imprime_bin
    ret
binario endp
salto_de_linea proc
    mov   ah,9                  ; llamada para imprimir cadena
    mov   dx,offset crlf        ; preparamo la cadena de salto de linea
    int   21h                   ; llamada a interrupcion
    ret 
salto_de_linea endp
end  main
