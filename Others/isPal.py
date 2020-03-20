def isPal(string):
    length = len(string)
    for i in range( length ):
        if(string[i] != string[length - i - 1]): return False
    return True

print(isPal('jsknf'))
print(isPal('jsknfjsknf'))
print(isPal('abbbba'))