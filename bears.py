#int => True or False
#imput a certain amount of bears that will go through the algorithm and output 42 bears

def bears(n):
    #base case
    if n == 42:
        return True
    if n<42:
        return False

    if n/2 == n//2:
        if n//2 > 42:
            t = q = 1   #allows it to run the divide by 2 case only once
            r = 3 = 0
        else:
            t = q = r = s = 0
    else:
        t = q = r = s = 0

    if n/3 == n//3 or n/4 == n//4:
        lval = n%10
        lval_2 = (n%100 - n%10)//10 
        lval_3 = lval * lval_2
        if lval_3 != 0:         #stops it from allowing it to run that case if it will only add 0 to itself
            r = 1               #allows it to run the subtract by last 2 digits multiplied case only once
            t = t + 1
        else:
            r=0
    else:
        r=0
    
    if n/5 == n//5:
        t = t + 1            
        s = 1           #allows it to run the subtract by 42 case only once

    if r == q == s == 0:    #fails if it can't do any of the cases
        return False

    while t != 0:
        if (n/3 == n//3 or n/4 == n//4) and r == 1:
            r = 0
            lval = n%10
            lval_2 = (n%100 - n%10)/10
            lval_3 = int(lval * lval_2)
            bears(int(n - lval_3)) 
        if n/5 == n//5 and s == 1:
            s = 0
            bears(n-42)
        if n/2 == n//2 and q == 1:
            q = 0
            bears(n//2)
        t = t - 1   
    return n
