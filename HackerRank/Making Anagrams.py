def makeAnagram(a, b):
    listA = [item for item in a]	#because string are unmutable we want to use a list
    listB = [item for item in b]
    listA.sort()					#sort to make comparasion simplier
    listB.sort()
    lenA = len(a)
    lenB = len(b)
    j = i = res = 0
    while i < lenA and j < lenB:	#So we iterate till we reach the end of any list, worst case O(A-1+B)
        if listA[i] == listB[j]:
            i += 1
            j += 1
            continue
        else:
            if listA[i] < listB[j]:
                i += 1
            elif listA[i] > listB[j]:
                j += 1
            res += 1				#So if A isnt B we need to push out the char
    res += lenA + lenB - j - i 		#Last we add the chars that we dont iterate 
    return res

a = input()
b = input()
res = makeAnagram(a, b)
print(res)


#Simpler way from internet with Counter we can make sets operations
#So the elements are the intersection complement of the elements
#from collections import Counter   
#a = Counter(raw_input())
#b = Counter(raw_input())
#c = a - b
#d = b - a
#e = c + d
#print len(list(e.elements()))
