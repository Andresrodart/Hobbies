houses = int(input())
photos = list(map(int, input().split()))
numStudents = 0
parStudents = 0
minSeen = 0
for i in range(1, houses):
    if photos[i - 1] > photos[i]:
        numStudents += parStudents - minSeen
        parStudents = 0
        minSeen = photos[i]
    else:
        parStudents = photos[i]
numStudents += parStudents - minSeen
print(numStudents)
