def makeAnagram(a, b):
    listA = [item for item in a]
    listB = [item for item in b]
    listA.sort()
    listB.sort()
    lenA = len(a)
    lenB = len(b)
    minLen = min(lenA,lenB)
    j = i = res = 0
    while i < minLen and j < minLen:
        if listA[i] == listB[j]:
            i += 1
            j += 1
            continue
        else:
            if listA[i] < listB[j]:
                i += 1
            elif listA[i] > listB[j]:
                j += 1
            res += 1
    res += lenA -  if (i < j) else lenB - j
    return res

a = input()
b = input()
res = makeAnagram(a, b)
print(res)
