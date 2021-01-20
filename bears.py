#int => True or False
#imput a certain amount of bears that will go through the algorithm and output 42 bears

def bears(n):
    #base cases
    
    if n/2 == n//2:
        t = 1
    else:
        t = 0
    if n/3 == n//3 or n/4 == n//4:
        t = t + 1
    if n/5 == n//5:
        t = t + 1
    
    
    if n == 42:
        return True
    #elif n < 42 and t == 0:
     #   return False

    for i in range(0,t):
        print(t)
        if n/2 == n//2:
            return bears(n/2)
        if n/3 == n//3 or n/4 == n//4:
            lval = n%10
            lval_2 = (n%100 - n%10)/10
            return bears(lval * lval_2)
        if n/5 == n//5:
            return bears(n-42)

print(bears(520))