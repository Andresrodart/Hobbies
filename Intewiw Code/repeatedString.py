import math

def repeatedString(s, n):
    if len(s) == 1 and s == 'a':
        return n
    if len(s) < n:
        s = s* int(math.ceil(n/len(s)))
    print(s)

repeatedString("abac", 100000)