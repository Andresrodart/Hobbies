#BAD
from collections import deque
digits = deque([1, 2, 3, 4, 5, 6, 7, 9])

def MakeNumber(n):
    i = 0
    res = 0
    while n > 0:
        res += digits[i] * (10**i)
        i = (i + 1) if i + 1 < 9 else 0
        n-= 1
    return res

if __name__ == "__main__":
    cases = int(input())
    while cases > 0:
        n = int(input())
        res = 0
        correct = False
        while not correct:
            res = MakeNumber(n)
            for i in range(min(9, n)):
                if res % digits[i]: 
                    correct = False
                    break
                correct = True
            digits.rotate(1)
        print(res)
        cases -= 1