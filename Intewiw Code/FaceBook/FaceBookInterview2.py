# Given a string with alpha-numeric characters and parentheses, return a string with balanced parentheses by removing the fewest characters possible. You cannot add anything to the string.
# balance("abc") -> "abc"
# balance("a(b)cc)") -> "a(b)cc"   
# balance(")(") -> ""
# balance(")))))(((((") -> ""
# balance("(()()(") -> "()()"
# balance(")(())(") -> "(())"
# balance(")())(()()(") -> "()()()"
  
There can be multiple correct results per input

balance("(())())") -> "(()())" or "(())()"
        
        
        ())**********
        
def mathClossig(strng):
    stac = []
    string = list(strng)
    cont = {'(':0, ')':0}
    
    for i in strng:
        if i ==  '(':
            cont['('] = cont['('] + 1
        elif  i ==  ')':
            cont[')'] = cont[')'] + 1
    
    if len(strng) == 0: 
        return strng
    
    for i in range(len(string)):
        if string[i] == ')':
            if len(stac) == 0:
                string.delete(i)
                pop
        elif i == '(':
            stac.append(i)
            
    if len(stac) == 0:
        return True
    else:
        return False
        
(
)