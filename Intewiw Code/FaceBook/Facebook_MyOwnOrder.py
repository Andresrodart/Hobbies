def wordSum(word, letValue):
    result = 0
    for item in word:
        result += letValue[item]
    return result

def inOrder(words, order):
    auxOrder = {}
    for i in range(len(order)):
        auxOrder[order[i]] = i
    for x in range(len(words) -1 ):
        for y in range( min(len(words[x]), len(words[x + 1])) ):
            if auxOrder[words[x][y]] < auxOrder[words[x + 1][y]]:
                break
            elif auxOrder[words[x][y]] == auxOrder[words[x + 1][y]]:
                continue
            else:
                return False
    return True

order = ['a', 'd', 'g', 'f', 'c', 'b']
words_1 = ['ac','dc','gb','fd']                                     #True
words_2 = ['ac','fd','gb','ds']                                     #False
words_3 = ['acd','acf','acfff','acffa']                             #False
words_4 = ['add','add','adddddddddddddddddddddddddd','afffff']      #true

print(inOrder(words_1, order))
print(inOrder(words_2, order))
print(inOrder(words_3, order))
print(inOrder(words_4, order))