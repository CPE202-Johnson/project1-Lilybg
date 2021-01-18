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
    for i in range(n):
        r = perm_gen_lex(a[0:-2]) + a[i]
        b = a[i] + perm_gen_lex(a[0:-2])
        list1[i] = r
        list1[-i] = b
    return list2


    #n.replace(b,c)

    #if len(list1) <= len(a))!:
     #   list1.append(n)
    #else:
     #   return list1
print(perm_gen_lex('ab'))