# BAD
import sys
indexes = []
N = int(input())
head = 1
for i in range(1, N):
    print('? ', head, ' ', i + 1)
    sys.stdout.flush()
    res = input()
    if res == '>':
        indexes.append(i + 1)
    elif res == '<':
        indexes = []
        head = i
head = indexes[0]
for i in range(1, len(indexes)):
    print('? ', head, ' ', indexes[i])
    sys.stdout.flush()
    res = input()
    if res == '<':
        head = indexes[i]
print('! ', head)