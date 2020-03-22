from sys import stdin, stdout

sheldonNumbers = set()

def generateOne(n, m, k):
    res = ''
    for i in range(n):
        res += '1'
    for _ in range(k):
        for i in range(m):
            res += '0'
        for i in range(n):
            res += '1'
    return res

def generateTwo(n, m, k):
    res = ''
    for i in range(n):
        res += '1'
    for _ in range(k):
        for i in range(m):
            res += '0'
        for i in range(n):
            res += '1'
    for i in range(m):
        res += '0'
    return res

def generateSheldonNumbers():
    for n in range(1, 64):
        for m in range(0, 64 - n):
            k = 0
            while n + k * (n + m) <= 63:
                sheldonNumbers.add(int(generateOne(n, m, k), base = 2))
                k += 1
    for n in range(1, 64):
        for m in range(0, 64 - n):
            k = 0
            while n + k * (n + m) + m <= 63:
                sheldonNumbers.add(int(generateTwo(n, m, k), base = 2))
                k += 1
generateSheldonNumbers()
validAnswers = sorted(list(sheldonNumbers))
if __name__ == "__main__":
    lines = stdin.readlines()
    length = len(lines)
    for line in lines:
        X, Y = map(int, line.split())
        i, j = 0, 0
        while X > validAnswers[i]: i += 1
        while i < len(validAnswers) and Y >= validAnswers[i]: 
            j += 1
            i += 1
        print(j)