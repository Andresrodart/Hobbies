#Minimum Swaps 2
#So at first it will be naive to go an swap every value as it appears like this
#Al inicio es muy sencillo llegar y hacer los cambios conforme van apareciendo los valores, así.

def minimumSwaps(arr):
    swaps = 0
    for i in range(0, len(arr)):
        if i + 1 != arr[i]:             #Check if the elementt is in his position/checamos que el elemento este en su posición
            j = i                      
            while i + 1 != arr[j]:
                j += 1
            arr[j], arr[i] = arr[i], arr[j]
            swaps +=1
    return swaps

#But this aproch will be problematic, because in the worst case the complecity will be O(n^2)
#Pero este acercamiento será rpoblematica, ya que al iterar dos vesce podemos tener  O(n^2)
#We can imporove this one with less code 
#Se puede mejeroar con menos código

def minimumSwaps(arr) :    
    swaps = 0
    i = 0
    while i < len(arr):
        if arr[i] == (i+1):
            i += 1
            continue
        arr[arr[i]-1], arr[i] = arr[i], arr[arr[i]-1]
        swaps += 1
    return swaps

#This will work just fine for n consecutive numbers, but if they aren't? So what if we just compare the indexes to swap the number to his real position?
#Esto funcionará bien para n numeros consecutivos, pero ¿si no lo son? Así que, ¿qué tal si sólo comparamos los valores numpericos con su posición real?

def minimumSwaps(arr):
    arrWPos = [(arr[x], x) for x in range(0, len (arr))]    #So first we make an array with the elements and position/primero hacemos una lista con los elementos y sus posiciones
    arrWPos.sort(key=lambda value: value[0])                #Then we sort this list as it should be, but with out losing the original positiosn/Después ordenamos esta lista, sin perder las posiciones originales
    visited = [0] * len(arr)                                #To keep track of visited elements
    ans = 0
 
    for i in range(0, len(arr)):
        if visited[i] or ( arrWPos[i][1] == i ):
            continue
        cycle_size = 0                                      #So see, some times we can make the changes with only two elements and they will be in order and some times we will need more swaps / mira, aveves con cmabiar dos elementos tendremos el estado resuelto, otras necesitaremso mas movimeintos
        j = i
        while not visited[j]:
            visited[j] = 1
            j = arrWPos[j][1]
            cycle_size += 1                                 #So we will be counting the number of "jumps" we make / contaremos el número de "saltos" que haremos 

        ans += (cycle_size - 1)                             # Update answer by adding current cycle.
    return ans
#This will be O(nlogn) because we only be moving the values to its position already stablished on sort
#Note that in this case we do not have to make the change
#Taste case 2 3 4 1 5 = 3
#Just in case you wonder WTF is cyclye_size, if the number of elements that consist in the loop that takes to move from the element to element till we retunr to the element we first move, and we have to rest 1 to dont count ir double
#En caso de que te preguntes que diablos es cyclye_size es el numero de elementos que conforman el ciclo que va de elemento a elemento hasta qeu regresamos al inicial, por eso restamos uno, para no contarlo dos veces