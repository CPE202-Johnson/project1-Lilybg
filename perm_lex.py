#generate all the permutations of the characters in a string
#str(lowercase letters in alphabetical order) => list of strings 
def perm_gen_lex(a): 
    if len(a) == 0:   
        list1 = []
        return list1
    elif len(a) == 1:
        list1 = [a]
        return list1
    
    n = len(a)
    last = a[-1]
    for i in range(n-1):
        y = perm_gen_lex(a[0:-1])
        print(y)
        r = y[i] + last
        b = last + y[i]
        print(r)
        print(b)
    return [r, b]

print(perm_gen_lex('ab'))