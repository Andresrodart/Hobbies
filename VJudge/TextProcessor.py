from sys import stdin, stdout

def subStrings(text):
    dp = set()
    indexes = []
    generateSubsString(dp, indexes, text, '', 0, 0)
    print(indexes)
    return len(dp)
    

def generateSubsString(dp, indexes, text, unused, begin, end):
    if end == len(text): return
    unused += str(text[end])
    textRange = str(begin) + '-' + str(end)
    if textRange in indexes: return
    dp.add(unused)
    indexes.append(textRange)
    generateSubsString(dp, indexes, text, unused, begin, end + 1)
    generateSubsString(dp, indexes, text, '', end + 1, end + 1)

if __name__ == "__main__":
    lines = stdin.readlines()
    while lines:
        text = lines.pop(0)
        Q, W = map(int, lines.pop(0).split())
        while Q > 0:
            index = int(lines.pop(0))
            res = 0 #subStrings(text[index - 1: index + W - 1 ])
            print(res)
            Q -= 1