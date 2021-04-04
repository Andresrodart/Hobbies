def sockMerchant(n, ar):
    aux_1 = [ar[0]]
    aux_2 = [1]
    for i in range(1, len(ar)):
        if(ar[i] in aux_1):
            aux_2[aux_1.index(ar[i])] += 1
        else:
            aux_1.extend([ar[i]])
            aux_2.extend([1])
    res = 0
    for i in range(0, len(aux_2)):
        res += int(aux_2[i]/2)
    return res

sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20])
