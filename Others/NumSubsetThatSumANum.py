import random

def count_sets(arr, total):
    mem = {}
    return rec(arr, total, len(arr) - 1, mem)

def rec(arr, total, i, mem):
    key = str(total) + ':' + str(i)
    toReturn = 0
    if key in mem:
        return mem[key]
    elif total == 0:
        return 1
    elif total < 0 or i < 0:
        return 0
    elif total < arr [i]:
        toReturn = rec(arr, total, i - 1, mem)
    else:
        toReturn = rec(arr, total - arr[i], i - 1, mem) + rec(arr, total, i - 1, mem)
    mem[key] = toReturn
    print(arr)
    return toReturn

arr = random.sample(range(1, 20), 10)
result = count_sets(arr, 10)
print(result, end = '\n')