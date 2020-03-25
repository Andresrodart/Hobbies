a = []
for i in range(10):
    a.insert(0, i)
print(a)
str1 = "Apples are red     "
print(str1[11 : 11 + 1])
print(str1[9 :])
print(list(str1))
a[0], a[-1] = a[-1], a[0]
print(a)
HT = {}
for i in range(10): HT[i] = a[i]
for item in HT: print(item, end = ' ')
print()
for item in HT.values(): print(item, end = ' ')
print()
print(bool(123 & 1), not(100000 & 1), bool(100000 & 1))