def countingValleys(n, s):
    valleys = 0
    aux = 0
    for i in range(0, n):
        if s[i] == 'U':
            aux +=1
        else:
            aux -= 1
        if aux == 0 and s[i] != 'D':
            valleys += 1
    return valleys