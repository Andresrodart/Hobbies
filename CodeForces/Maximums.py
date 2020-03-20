x = [0]
a = []
n = int(input())
b = list(map(int, input().split()))
for num in b:
    a.append(num + x[-1])
    x.append(max(x[-1], a[-1]))
print(*a, sep = ' ')