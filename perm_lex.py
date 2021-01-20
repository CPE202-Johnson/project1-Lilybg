#generate all the permutations of the characters in a string
#str(lowercase letters in alphabetical order) => list of strings 
def perm_gen_lex(a): 
    if len(a) == 0:   
        return []
    elif len(a) == 1:
        return [a]
    
    hold = []

    for c in a: 
        char = c
        per = a.replace(c,'')

        perms = perm_gen_lex(per)

        for p in perms:
            hold.append(char + p)
    
    return hold
    

print(perm_gen_lex('abc'))