def minimumBribes(q):
    ans = 0
    for i in range(0, len(q)):
        if q[i] - (i + 1) > 2:                  #Cuz every one has his number, we can know how much people teh person bride with de substraction of his original place less de position it is in/ Como todos mantieen la etiqueta de su lugar original podemos saber cuantas personas soborno haciendo la resta de su lugar original menos la posicion dodne se encuntra actualmente
            print("Too chaotic")                #If she moves more tha two places is too chaotics / Si se movió mas de 2 veces es muy caótico
            return
        for j in range(max(0, q[i] - 2), i):    #See that we only have to count the number bigger than us from behind, that is acomplish when my position is bigger than me (some cases like in position in order also happens ams has to be take in count)* and the far that a number can over pass us is one cuz he can just bride twice, so this for loop jus goint to count from one position behind the overcome till one position behind the current position/Sólo nos interesa contar los números que estan detrás de mi si mi posocion es ma grande que mi valor (algunos casos como que estar en mi posicion tambien suceden y deben tomar sen cuenta)*, y lo mas lejos que puede llegar un numero a soibre pasarnos es una posicion atras, pues solo puede sobornar dos veces, entonces solo tenemos que checar los numeros desde un lugar antes de nuestra posicion original hasta la posicion atras de nuestro lugar actual, si el numero es mas grande que su pósicion no entrara en el bucle.   
                if q[j] > q[i]:                 #So now we check how many brides she had made, by counting the number of numbers that are smaller than she / PAra saber cuantos sobornos dió sólo hay que ver cuantops números mas pequeños hay detrás de él.
                    ans += 1
    print(ans)
                                                #*[1,2,3,4,5] -> [1,2,3,5,4] -> [1,2,5,3,4] -> [1,2,5,4,3]