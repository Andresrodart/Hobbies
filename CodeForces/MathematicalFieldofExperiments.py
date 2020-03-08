p = int(input())
print('0', end='')
for x in range(1, p):
    if x ** 2 < p: print(' ', x, end='')
    for s in range(p-1, 0, -1):
        if (s ** 2 - x) % p == 0:
            print(' ', s, end='')
            break
        if s == 1:
            print(' ', -1, end='')