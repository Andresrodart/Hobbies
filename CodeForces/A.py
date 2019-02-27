def frogJumps(a, b, k):
    if a == b:
        return 0 if k % 2 == 0 else a
    else:
        return int (a*k/2 - b*k/2 if k % 2 == 0 else a*(k+1)/2 - b*(k + 1)/2  + b)

if __name__ == '__main__':
    t = int(input())
    ans = []
    for _ in range(t):
        abk = input().split()
        a = int(abk[0])
        b = int(abk[1])
        k = int(abk[2])
        ans.append(frogJumps(a, b, k))
    print(*ans, sep='\n')
