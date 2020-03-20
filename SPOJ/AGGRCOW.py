def binary(lis, N, minElement, maxElement):
    mid = int((minElement + maxElement)/2)
    aux = False
    if minElement > maxElement or mid == 0: return 0
    for i in range(N - 1):
        if mid <= lis[i] - lis[i - 1] - 1: aux = True
    if aux == True: return min(mid, binary(lis, N, minElement, mid - 1))
    else: return binary(lis, N, minElement, mid - 1)

cases = int(input())
for _ in range(cases):
    N, C = map(int, input().split())
    stallLocation = []
    for each in range(N):
        stallLocation.append(int(input()))
    if N == C: print(1)
    else:
        stallLocation.sort()
        print(binary(stallLocation, N, 2, stallLocation[-1]))