#Not tested
def goodArray(lenA, arr):
    k = 0
    jIndexs = []
    sumAr = sumArr(arr)
    for i in range(lenA):
        for y in range(lenA):
            if i != y and arr[y] == sumAr - arr[i] - arr[y]:
                k += 1
                jIndexs.append(i + 1)
    print(k)
    if k != 0:
        print(*jIndexs, sep=' ')

def sumArr(arr):
    ans = 0
    for i in arr:
        ans += i
    return ans

if __name__ == '__main__':
    lenA = int(input())
    arr = list(map(int, input().rstrip().split()))
    goodArray(lenA, arr)