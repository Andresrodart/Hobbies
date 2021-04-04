T = int(input())
while T:
    n, k = map(int, input().rstrip().split())
    n += 1
    k += 1
    n = n * (n + 1)
    n = n // 2
    n = n * k
    n = n % 1000000007
    print(n)
    T -= 1
