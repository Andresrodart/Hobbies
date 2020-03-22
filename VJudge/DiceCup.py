from sys import stdin, stdout
def maxIndex(lis):
    res = -1
    for i in range(len(lis)):
        if lis[i] > res: res = lis[i]
    return res

if __name__ == "__main__":
    lines = stdin.readlines()
    length = len(lines)
    for index in range(length):
        diceA, diceB = map(int, lines[index].split())
        nums = [0]*1000
        for i in range(diceA):
            for j in range(diceB):
                nums[i + j + 2] += 1
        maxNum = maxIndex(nums)
        for i in range(len(nums)):
            if nums[i] == maxNum: print(i)
        if index + 1 != length: print()