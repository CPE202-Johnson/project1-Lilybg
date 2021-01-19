#int => str
def convert(num, b):
    """Recursive function that returns a string 
    representing num in the base b"""
    if num < b:
        return num

    reduced = num/b
    dig = str(num%b)

    return dig + convert(reduced,b)

print(convert(20,2))