#int => str
def convert(num, b):
    """Recursive function that returns a string 
    representing num in the base b"""
    if int(num/b) == 0:
        return str(num%b)

    reduced = num//b
    y = convert(reduced,b)
    
    return y + str(num%b)

    

print(convert(30,4))