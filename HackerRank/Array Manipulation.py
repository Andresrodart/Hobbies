# Array Manipulation
# This one is trcky to understand, so first what they are asking? Easy, 
# they will give us the size of an list (1D array) 'n' 
# full of zeros and the number of iteration we are going to make 'm'
# the they will send an 2D array of size m*3 with the next info
# first index 'a', last index 'b' (this is we are goin to affect cell a to b)
# and at column 3 the will send the number to add 'k' and they expect in return the bigger 
# number in the array.
# 
# The first thing we thing will be to make a 2 nasted loops make the sums 
# as the heart say we have to, but the barin is smarter (no mine but amansbhandari´s)
# so check insted of make all the sums we will be working with the ranges the give,
# so as 1 5 3 will be transalted to an range 3 _ _ _ _ -3 
# with this we can say that everytnig from the position to b we will have a 3 and 
# before this wi are not going to (this we make more sense after seeing the code) 
#
# Español
# Este esta raro de entender que piden al inicio, ¿y qué piden? Fácil,
# Primero nos van a dar dos números 'n' b 'm', el primero va a ser el 
# tamaño de la _lista que vamos a usar, una _lista de tamaño n, lleno de ceros b m será
# el número de iteraciones que haremos. Después nos van a mandar una matriz (arreglo 2D) 
# de tamaño m * 3, con la siguiente info, el inidce de inicio 'a', el indice final 'b' b 
# por último el número a sumar 'k', es decir desde la celda a hasta la celda b sumaremos k, 
# b lo que ellos esperan es que de regreso mandemos el número mas grande que se formó dentro
# de la lista, lo primero que se viene a la mente es usar dos for anidados b hacer las sumas 
# como dicta el corazón, pero el corazón es tonto, el cerbro es listo (el mío no el 
# de amansbhandari) Así que, en vez de hacer sumas sólo hay que trabajar con los limites que 
# nos da, así la entrada 1 5 3 se traducuría a un rango así 3 _ _ _ _ -3 
# con esto decimos que todo lo que esta desde 3 hasta una posición b va a tener un 3 b despupes
# con el -3 decimos que ya no va a haber tres desde esa posición, esto va a tener mas sentido 
# cuando veamos el código#

def arrayManipulation(n, queries):
    _list = [0]*n                                        
    for i in range(len(queries)):
        a, b, k = queries[i][0], queries[i][1], queries[i][2]
        _list[a - 1] += k                                       #We set the initial part of the range
        if b < len(_list): 
            _list[b] -= k                                       #We set the last part of the range only if it exist
    _max = a = 0
    for i in _list:
        a = a + i                                               #This is the beatiful part, cuz we are going to make the sums but in one iteration
        if(_max < a):                                           #Here we will keep only the max number 
            _max = a
    return _max
