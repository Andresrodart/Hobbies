fibo = 3 
a = 1
b = 2
val = int(input(""))
for i in range(3, val):
    if i == fibo:
        a = b
        b = fibo
        fibo = a + b
    else:
        print(i, sep='', end=' ')