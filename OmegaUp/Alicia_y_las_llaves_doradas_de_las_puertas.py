chapa = {}

chapas = int(input(""))
aux = input().split(" ")
llaves = int(input())
llave = input().split(" ")
for i in range(chapas):
    chapa[aux[i]] = i
for i in llave:
    try:
        print(int(chapa[i]) + 1,  sep='', end=' ')
    except:
        print('0',  sep='', end=' ')