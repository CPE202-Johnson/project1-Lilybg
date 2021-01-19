#generate all the permutations of the characters in a string
#str(lowercase letters in alphabetical order) => list of strings 
def perm_gen_lex(a): 
    if len(a) == 0:   
        return []
    elif len(a) == 1:
        return [a]
    
    n = len(a)  #3
    last = a[-1] 

    
    for i in range(n-1):
        y = perm_gen_lex(a[0:-1])
        #print(y)
        r = y[i] + last
        b = last + y[i]
        y.append(r)
        y.append(b)
    
    return y[1:]
print(perm_gen_lex('abc'))