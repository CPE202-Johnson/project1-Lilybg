#generate all the permutations of the characters in a string
#str(lowercase letters in alphabetical order) => list of strings 
def perm_gen_lex(a): 
    if len(a) == 0:   
        return []
    elif len(a) == 1:
        return [a]
    
    n = len(a)
    hold = a[0]  
    
    y = perm_gen_lex(a[1:])

    r = y[0] + hold
    print(r)
    y[0] = hold + y[0]
    y.append(r)
    
    
  
    return y

print(perm_gen_lex('abc'))